
import datetime
import math

"""Assignment - #1:
All the codes need to have proper comments and explanation. Please show snapshot for the output.
Thanks!"""


def problem1():
    """1. Write a Python program which prompts the user for a Celsius temperature, converts the
    temperature to Fahrenheit, and prints out the converted temperature."""
    celsius()


def problem2():
    """2. The cover price of a book is $25, but bookstores get a 10% discount. Shipping costs $2
        for the first five copies and 2.75 cents for all rest of copies. Write a Python program to
        show what is the total wholesale cost for 40 copies display the result."""
    booksOrdered = 40
    price = bookPrice(booksOrdered)

def problem3():
    """3. I have started walking to home at 7:30 AM for the first mile at slow step (8 min:15 sec
    per mile), then 3 miles at speed (7 min:12 sec per mile), what time do I get home for
    breakfast? (format output in hh: min)"""
    TimeHome()

def problem4():
    """4. Write a Python code to calculate the speed for running a 10-kilometer race in 1 hours 5
        minutes 42 seconds. What is the average pace (time per mile in minutes and seconds)?
        What is the average speed in miles per hour?"""
    kilometers = 10
    minutes = 5
    hours = 1
    seconds = 42
    miles = KilometersToMiles(kilometers)
    time = ConvertHoursToSeconds(hours)
    time = time + ConvertMinutesToSeconds(minutes)
    time = time + seconds
    #print(time)
    AverageSpeedMPH(miles, time)
    AveragePaceInMinutesAndSeconds(miles, time)


def celsius():
    # (Fahrenheit – 32) * 5/9 Fahrenheit = (Celsius * 9/5) + 32
    celsius = float(input("What is the tempature in celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(fahrenheit)
def bookPrice(copiesOrdered):
    print("You ordered ", copiesOrdered, " books")
    coverPrice = 25
    print("Cover price is $", coverPrice)
    bookStoreDiscount = .90
    print("Your discount is ", round((1 - bookStoreDiscount),3)*100, "%")
    shipping = 0
    for copy in range(1, copiesOrdered):
        if (copy <= 5):
            shipping = shipping + 2
        else:
            shipping = shipping + 2.75
    print("Your shipping cost is $", shipping)
    totalPrice = copiesOrdered * coverPrice * bookStoreDiscount + shipping
    print("Your total price is $", totalPrice)
    return totalPrice

def TimeHome():
    currentTime = 7.5
    minutesInHour = 60
    secondsInMinute = 60
    currentTimeInToSeconds = currentTime * minutesInHour * secondsInMinute
    firstMile = 8.25
    firstMileInSeconds =  firstMile * secondsInMinute
    lastThreeMiles = 7.2 * 3
    lastThreeMilesInSeconds = lastThreeMiles * secondsInMinute
    timeHome = datetime.timedelta(seconds=currentTimeInToSeconds) + datetime.timedelta(seconds=lastThreeMilesInSeconds) \
               + datetime.timedelta(seconds=firstMileInSeconds)


    #timeHome = currentTimeInToSeconds + firstMileInSeconds + lastThreeMilesInSeconds
    #print(timeHome)
    #minutes = timeHome / (secondsInMinute)
    #print(minutes)
    #hours = minutes / (minutesInHour)
    print("You get home for breakfast at ", timeHome)

def ConvertHoursToSeconds(hours):
    return hours * 60 * 60

def ConvertMinutesToSeconds(minutes):
    return minutes * 60

def KilometersToMiles(totalKilometers):
    miles = round(totalKilometers * 0.62137, 2)
    print(totalKilometers, "kilometers equals ", miles, "miles")
    return miles

def AverageSpeedMPH(miles, timeInSeconds):
    milesPerSecond = miles / timeInSeconds
    milesPerMinute = (milesPerSecond * 60)
    milesPerHour = round(milesPerMinute * 60, 2)
    print("You ran ", milesPerHour, "miles per hour")
    return milesPerHour

def AveragePaceInMinutesAndSeconds(miles, timeInSeconds):
    secondsPerMile = timeInSeconds/ miles
    miniutesPerMile = (secondsPerMile / 60)
    minutes = math.trunc(miniutesPerMile)
    seconds = math.trunc((miniutesPerMile % 1) * 60)
    #print(minutes)
    #print(seconds)
    #print(miniutesPerMile)
    print("Your time per mile was ", minutes, " minutes and ", seconds, " seconds")

#problem1()
#problem2()
#problem3()
problem4()