import pandas as pd
import matplotlib.pyplot as plot

class part1():
    """1)	Load all three datasets into separate Dataframes. Keep the Dataframe variable name as summer, winter, country_codes.
    2)	Display a subset of Summer Dataframe with 8 rows (after 6th index) with columns Year, Athlete and Medal
    Expected output:
    3)	Replace all commas with space in the 'Athlete' column of Summer and winter Dataframe.
        Expected output:
    4)	Modify Summer Dataframe by merging Summer Dataframe with country_codes Dataframe based on the country code.
    5)	Modify Winter dataframe by merging Winter Dataframe with country_codes Dataframe based on the country code.
    6)	Create a function to find the male athlete & female Athlete who won the highest number of medals.
        You should pass the Summer/Winter Dataframe object to the function. Also pass the gender to the function.
        The function should return the name of the male/female athlete who won the highest number of medals.
        Function Definition:
    7)	Create a function to find the athlete who won the highest number of medals in each medal category (Gold, Bronze, Silver).
    8)	Calculate the number of medals by year and column in a pivot table for Summer and Winter Dataframe. [Use count as aggfunc]
    9)	Extract a series with total number of medals won by each country in Summer and Winter.
    10)	 Combine Summer and Winter Olympics data and create a bar chart showing the top 10 highest medal winning countries.
    """
    def __init__(self):
        """1)	Load all three datasets into separate Dataframes. Keep the Dataframe variable name as summer, winter, country_codes."""
        self.dfSummer = pd.read_csv("summer.csv")
        self.dfWinter = pd.read_csv("winter.csv")
        self.dfCountryCodes = pd.read_csv("country_codes.csv")
        #pd.set_option('display.max_columns', None)
        #print(self.dfCountryCodes.head(5))

    def displaySummer(self):
        """2)	Display a subset of Summer Dataframe with 8 rows (after 6th index) with columns Year, Athlete and Medal
            Expected output:"""
        print(self.dfSummer[6:14])
        #print(self.dfSummer.iloc[[6::]])

    def replaceCommas(self):
        """    3)	Replace all commas with space in the 'Athlete' column of Summer and winter Dataframe.
        Expected output:"""
        self.dfSummer["Athlete"] = self.dfSummer["Athlete"].str.replace(",", " ")
        self.dfWinter["Athlete"] = self.dfWinter["Athlete"].str.replace(",", " ")
        #print(self.dfSummer["Athlete"].head(5))
        #print(self.dfWinter["Athlete"].head(5))

    def mergeSummer(self):
        """4)	Modify Summer Dataframe by merging Summer Dataframe with country_codes Dataframe based on the country code."""
        #self.dfSummer = pd.concat([self.dfSummer, self.dfCountryCodes], axis=1, sort=False)
        self.dfSummer = pd.merge(self.dfSummer, self.dfCountryCodes, left_on='Country', right_on='Code')
        #print(self.dfSummer.head(5))
    
    def mergeWinter(self):
        """5)	Modify Winter dataframe by merging Winter Dataframe with country_codes Dataframe based on the country code."""
        self.dfWinter = pd.merge(self.dfWinter, self.dfCountryCodes, left_on='Country', right_on='Code')
        #print(self.dfWinter.head(5))

    def findAtheletes(self, dataframe, gender):
        """6)	Create a function to find the male athlete & female Athlete who won the highest number of medals.
        You should pass the Summer/Winter Dataframe object to the function. Also pass the gender to the function.
        The function should return the name of the male/female athlete who won the highest number of medals."""
        #print(dataframe.head(5))
        print("   ")
        df = dataframe["Athlete"].value_counts().where(dataframe["Gender"] == gender).head(1)
        print(df)
        return df
        #print(dataframe.head(1).where(dataframe["Gender"] == gender).where(dataframe["Athlete"].value_counts()))

    def findHighestMetals(self):
        """7)	Create a function to find the athlete who won the highest number of medals in each medal category (Gold, Bronze, Silver)."""
        print(self.dfSummer[["Athlete", "Medal"]].where(self.dfSummer["Medal"] == "Gold").value_counts().head(1))
        print()
        print(self.dfSummer[["Athlete", "Medal"]].where(self.dfSummer["Medal"] == "Silver").value_counts().head(1))
        print()
        print(self.dfSummer[["Athlete", "Medal"]].where(self.dfSummer["Medal"] == "Bronze").value_counts().head(1))

    def numberOfMedalsWonByCountry(self):
        """9)	Extract a series with total number of medals won by each country in Summer and Winter."""
        print("Summer Winners")
        print(self.dfSummer["Code"].value_counts().head(5))
        print("Winter medals")
        print(self.dfWinter["Code"].value_counts().head(5))

    def highestMedalWinningCountries(self):
        self.summerAndWinter = pd.concat([self.dfWinter, self.dfSummer])
        self.summerAndWinter = self.summerAndWinter["Code"].value_counts().head(10)
        self.summerAndWinter.plot.bar()
        plot.show()

    def getSummer(self):
        return self.dfSummer
    
def problem1():
    problem = part1()
    #problem.displaySummer()
    problem.replaceCommas()
    problem.mergeSummer()
    problem.mergeWinter()
    
    #df = problem.getSummer()
    #problem.findAtheletes(df, 'Men')

    #problem.findHighestMetals()

    #problem.numberOfMedalsWonByCountry()
    problem.highestMedalWinningCountries()


problem1()