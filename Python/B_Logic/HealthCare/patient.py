class Patient:

    def __init__(self, prescriptions=None):
        self.prescriptions = prescriptions or []

    def addPrescription(self, prescription):
        self.prescriptions.append(prescription)

    def daysTaking(self, medicineName):
        prescriptions = filter(lambda p: p.name == medicineName, self.prescriptions)
        days = set()
        for prescription in prescriptions:
            days.update(prescriptions.daysTaken())
        return days

    def clash(self, medicineNames):
        daysTaking = [self.daysTaking(medicineName)
                      for medicineName in medicineNames] \
                     or [set()]
        return set.intersection(*daysTaking)
