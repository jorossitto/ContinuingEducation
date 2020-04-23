from datetime import date, timedelta

class Prescription:

    def __init__(self, name, dispenseDate, daysSupply):
        self.name = name
        self.dispenseDate = dispenseDate
        self.daysSupply = daysSupply

    def daysTaken(self):
        allDays = (self.dispenseDate + timedelta(days=i)
                   for i in range(self.daysSupply))
        return (day for day in allDays if day < date.today())
    
