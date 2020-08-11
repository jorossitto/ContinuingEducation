
def compoundInterest(years, rate, amount):
    return (years ** rate) * amount

#Roth Vs Ira

amount = 12

iraAmount = amount
rothAmount = amount * .5
tenPercentPenalty = amount * .9
doubleTaxes = amount * .5

rate = 2
years = 60
iraAmount = compoundInterest(years, rate, iraAmount)
rothAmount = compoundInterest(years, rate, rothAmount)
tenPercentPenalty = compoundInterest(years, rate, tenPercentPenalty)
doubleTaxes = compoundInterest(years, rate, doubleTaxes)

iraAmount = iraAmount * .5
doubleTaxes = doubleTaxes *.5

print("Ira " + str(iraAmount))
print("Roth " + str(rothAmount))
print("Penalty " + str(tenPercentPenalty))
print("Double Taxes " + str(doubleTaxes))