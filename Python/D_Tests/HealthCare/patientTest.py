import unittest

from B_Logic.HealthCare.patient import Patient
from B_Logic.HealthCare.prescription import Prescription
from B_Logic.Calculator.timeCalculator import TimeCalculator

class PatientTest(unittest.TestCase):

    def noClashWithNoPrescriptions(self):
        patient = Patient(prescriptions=[])
        self.assertSetEqual(set(), patient.clash([]))

    def noClashWithOneIrrelevantPrescription(self):
        patient = Patient(prescriptions=[Prescription("Codine",
                                                      dispenseDate = TimeCalculator.daysAgo(days=2),
                                                      daysSupply=2)])
        self.assertSetEqual(set(), patient.clash(["Prozac"]))

    def oneClashWithOnePrescription(self):
        patient = Patient(prescriptions=[Prescription("Codine",
                                                      dispenseDate = TimeCalculator.daysAgo(days=2),
                                                      daysSupply=2)])
        self.assertSetEqual({TimeCalculator.daysAgo(days=2), TimeCalculator.daysAgo(days=1)}, patient.clash(["Codine"]))


