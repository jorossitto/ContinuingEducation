import matplotlib.pyplot as plt
import matplotlib.animation as ani
import numpy as np
from C_Data.configs import *

GREY = (0.78, .78,.78)
RED = (0.96, .15,.15)
GREEN = (0.0, .86,.03)
BLACK = (0.0, .0,.0)

COVID19_PARAMS = {
    "R0" :2.28,
    "incubation" :5,
    "percentMild" :.8,
    "mildRecovery": (7,14),
    "percentSevere" :.2,
    "SevereRecovery" :(21,42),
    "severeDeath" :(14,56),
    "fatalityRate" : .034,
    "serialInterval" :7,
}

class Covid19():
    def __init__(self, params):
        self.fig = plt.figure()
        self.axes = self.fig.add_subplot(111, projection="polar")
        self.axes.grid(False)
        self.axes.set_xticklabels([])
        self.axes.set_yticklabels([])
        self.axes.set_ylim(0,1)

        #create annotations
        self.dayText = self.axes.annotate("Day 0", xy=[np.pi/2,1], ha="center", va="bottom")
        self.infectedText = self.axes.annotate("Infected: 0", xy=[3* np.pi/2, 1], ha="center", va='top', color=RED)
        self.deathsText = self.axes.annotate("\nDeaths: 0", xy=[3*np.pi/2,1], ha='center', va='top', color=BLACK)
        self.recoveredText = self.axes.annotate('\n\nRecovered: 0', xy=[3*np.pi/2,1], ha='center', va='top', color=GREEN)

        #create member variables
        self.day = 0
        self.totalNumInfected = 0
        self.numCurrentlyInfected = 0
        self.numRecovered = 0
        self.numDeaths = 0
        self.r0 = params["R0"]
        self.percentMild = params['percentMild']
        self.percentSevere = params['percentSevere']
        self.fatalityRate = params['fatalityRate']
        self.serialInterval = params['serialInterval']

        self.mildFast = params['incubation'] + params['mildRecovery'][0]
        self.mildSlow = params['incubation'] + params['mildRecovery'][1]
        self.severeFast = params['incubation'] + params['SevereRecovery'][0]
        self.severeSlow = params['incubation'] + params['SevereRecovery'][1]
        self.deathFast = params['incubation'] + params['severeDeath'][0]
        self.deathSlow = params['incubation'] + params['severeDeath'][1]

        self.mild = {i: {configs.THETAS : [], 'rs': []} for i in range(self.mildFast, 365)}
        self.severe = {
            configs.RECOVERY : {i: {configs.THETAS : [], 'rs': []} for i in range(self.severeFast, 365)},
            configs.DEATH : {i: {configs.THETAS : [], 'rs': []} for i in range(self.deathFast, 365)}
        }

        self.exposedBefore = 0
        self.exposedAfter = 1
        self.initalPopulation()

    def initalPopulation(self):
        self.population = 4500
        self.numCurrentlyInfected = 1
        self.totalNumInfected = 1
        indices = np.arange(0, self.population) + 0.5
        self.thetas = np.pi * (1 + 5**.5) * indices
        self.rs = np.sqrt(indices / self.population)
        self.plot = self.axes.scatter(self.thetas, self.rs, s=5, color= GREY)

        #patient zero

        self.axes.scatter(self.thetas[0], self.rs[0], s=5, color = RED)
        self.mild[self.mildFast][configs.THETAS].append(self.thetas[0])
        self.mild[self.mildFast][configs.RS].append(self.rs[0])

    def spreadCovid(self, i):
        self.exposedBefore = self.exposedAfter
        if self.day % self.serialInterval == 0 and self.exposedBefore < self.population:
            self.numNewInfected = round(self.r0 * self.totalNumInfected)
            self.exposedAfter += round(self.numNewInfected * 1.1)
            if self.exposedAfter > self.population:
                self.numNewInfected = round((self.population- self.exposedBefore) * .9)
                self.exposedAfter = self.population
            self.numCurrentlyInfected += self.numNewInfected
            self.totalNumInfected += self.numNewInfected
            self.newInfectedIndicies = list(
                np.random.choice(
                    range(self.exposedBefore, self.exposedAfter),
                    self.numNewInfected,
                    replace = False
                )
            )
            thetas = [self.thetas[i] for i in self.newInfectedIndicies]
            rs = [self.rs[i] for i in self.newInfectedIndicies]
            self.anim.event_source.stop()
            if len(self.newInfectedIndicies) > 24:
                sizeList = round(len(self.newInfectedIndicies)/24)
                thetaChunks = list(self.chunks(thetas, sizeList))
                rChunks = list(self.chunks(rs, sizeList))
                self.anim2 = ani.FuncAnimation(
                    self.fig,
                    self.oneByOne,
                    interval=50,
                    frames=len(thetaChunks),
                    fargs=(thetaChunks, rChunks, RED)
                )
            else:
                self.anim2 = ani.FuncAnimation(
                    self.fig,
                    self.oneByOne,
                    interval=50,
                    frames=len(thetas),
                    fargs=(thetas,rs,RED)
                )
            self.assignSymptoms()
        self.day +=1
        self.updateStatus()
        self.updateText()

    def oneByOne(self, i, thetas, rs, color):
        self.axes.scatter(thetas[i], rs[i], s=5, color=color)
        if i == (len(thetas)-1):
            self.anim2.event_source.stop()
            self.anim.event_source.start()

    def chunks(self, aList, n):
        for i in range(0, len(aList), n):
            yield aList[i:i + n]


    def assignSymptoms(self):
        numMild = round(self.percentMild * self.numNewInfected)
        numSevere = round(self.percentSevere * self.numNewInfected)
        #choose random subset of newly infected to have mild symptoms

        self.mildIndicies = np.random.choice(
            self.newInfectedIndicies, numMild, replace=False
        )
        #assign the rest severe symptoms, either resulting in recovery or death
        remaningIndicies = [
            i for i in self.newInfectedIndicies if i not in self.mildIndicies
        ]
        percentSevereRecovery = 1-(self.fatalityRate/self.percentSevere)
        numSevereRecovery = round(percentSevereRecovery * numSevere)
        self.severeIndices = []
        self.deathIndices = []
        if remaningIndicies:
            self.severeIndices = np.random.choice(
                remaningIndicies, numSevereRecovery, replace=False
            )
            self.deathIndices = [
                i for i in remaningIndicies if i not in self.severeIndices
            ]

        #assign recovery/death day
        low = self.day + self.mildFast
        high = self.day + self.mildSlow
        for mild in self.mildIndicies:
            recoveryDay = np.random.randint(low, high)
            mildTheta = self.thetas[mild]
            mildR = self.rs[mild]
            self.mild[recoveryDay][configs.THETAS].append(mildTheta)
            self.mild[recoveryDay][configs.RS].append(mildR)

        low = self.day + self.severeFast
        high = self.day + self.severeSlow
        for recovery in self.severeIndices:
            recoveryDay = np.random.randint(low, high)
            recoveryTheta = self.thetas[recovery]
            recoveryR = self.rs[recovery]
            self.severe[configs.RECOVERY][recoveryDay][configs.THETAS].append(recoveryTheta)
            self.severe[configs.RECOVERY][recoveryDay][configs.RS].append(recoveryR)

        low = self.day + self.deathFast
        high = self.day + self.deathSlow
        for death in self.deathIndices:
            deathDay = np.random.randint(low, high)
            deathTheta = self.thetas[death]
            deathR = self.rs[death]
            self.severe[configs.DEATH][deathDay][configs.THETAS].append(deathTheta)
            self.severe[configs.DEATH][deathDay][configs.RS].append(deathR)

    def updateStatus(self):
        if self.day >= self.mildFast:
            mildThetas = self.mild[self.day][configs.THETAS]
            mildRS = self.mild[self.day][configs.RS]
            self.axes.scatter(mildThetas, mildRS, s=5, color=GREEN)
            self.numRecovered += len(mildThetas)
            self.numCurrentlyInfected -= len(mildThetas)

        if self.day >= self.severeFast:
            recoveryThetas = self.severe[configs.RECOVERY][self.day][configs.THETAS]
            recoveryRS = self.severe[configs.RECOVERY][self.day][configs.RS]
            self.axes.scatter(recoveryThetas, recoveryRS, s=5, color=GREEN)
            self.numRecovered += len(recoveryThetas)
            self.numCurrentlyInfected -= len(recoveryThetas)

        if self.day >= self.deathFast:
            deathThetas = self.severe[configs.DEATH][self.day][configs.THETAS]
            deathRS = self.severe[configs.DEATH][self.day][configs.RS]
            self.axes.scatter(deathThetas, deathRS, s=5, color=BLACK)
            self.numDeaths += len(deathThetas)
            self.numCurrentlyInfected -= len(deathThetas)

    def updateText(self):
        self.dayText.set_text("Day {}".format(self.day))
        self.infectedText.set_text("Infected: {}".format(self.numCurrentlyInfected))
        self.deathsText.set_text("\nDeaths {}".format(self.numDeaths))
        self.recoveredText.set_text("\n\nRecovered {}".format(self.numRecovered))

    def gen(self):
        while self.numDeaths + self.numRecovered < self.totalNumInfected:
            yield

    def animate(self):
        self.anim = ani.FuncAnimation(
            self.fig,
            self.spreadCovid,
            frames=self.gen,
            repeat=True
        )

def main():
    coronavirus = Covid19(COVID19_PARAMS)
    coronavirus.animate()
    plt.show()

if __name__ == "__main__":
    main()


#Covid19(COVID19_PARAMS)
#plt.show()
