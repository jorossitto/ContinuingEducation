import unittest

from B_Logic.telemetry.TelemetryDiagnosticControls import TelemetryDiagnosticControls


class MockTelemetryClient(object):
    pass


class TelemetryDiagnosticControlsTest(unittest.TestCase):

    def testCheckTransmissionShouldSendADiagnosticMessageAndRecieveAStatusMessageResponse(self):
        controls = TelemetryDiagnosticControls(MockTelemetryClient(online=True, recieveData = "foo"))
        controls.checkTransmission()
        self.assertEqual("foo",controls.diagnosticInfo)

    def testCheckTransmissionFailsIfTelemetryClientDoesntConnect(self):
        controls = TelemetryDiagnosticControls(MockTelemetryClient(online=False, recieveData = "foo"))
        self.assertRaises(Exception, controls.checkTransmission)
        self.assertEqual("", controls.diagnosticInfo)

    def testCheckTransmissionFailsIfTelemetryClientDisconnectsBeforeRecieve(self):
        controls = TelemetryDiagnosticControls(MockTelemetryClient(online=True, recieveData = "foo", goOfflineOnSend = True))
        self.assertRaises(Exception, controls.checkTransmission)
        self.assertEqual("", controls.diagnosticInfo)
