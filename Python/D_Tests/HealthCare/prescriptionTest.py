import unittest
from datetime import date, timedelta

from B_Logic.HealthCare.prescription import Prescription
from B_Logic.Calculator.timeCalculator import TimeCalculator

class PrescriptionTest(unittest.TestCase):
    def daysTakenExcludesFutureDates(self):
        prescription = Prescription("Codine", dispenseDate=TimeCalculator.daysAgo(days=2), daysSupply=4)
        self.assertListEqual(([TimeCalculator.daysAgo(days=2), TimeCalculator.daysAgo(days=1)],
                              list(prescription.daysTaken())))



