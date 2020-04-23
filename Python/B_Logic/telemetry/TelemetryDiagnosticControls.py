
from B_Logic.telemetry.TelemetryClient import TelemetryClient


class TelemetryDiagnosticControls:
    DiagnosticChannelConnectionString = "*111#"

    def __init__(self, client=None):
        self.telemetry_client = client or TelemetryClient()
        self.diagnosticInfo = ""

    def checkTransmission(self):
        self.reconnect()
        self.sendAndRecieve()

    def sendAndRecieve(self):
        self.diagnosticInfo = ""
        self.telemetry_client.send(TelemetryClient.DIAGNOSTIC_MESSAGE)
        self.diagnosticInfo = self.telemetry_client.receive()

    def reconnect(self):
        self.telemetry_client.disconnect()
        retriesLeft = 3
        while not self.telemetry_client.getOnlineStatus() and retriesLeft > 0:
            self.telemetry_client.connect(TelemetryDiagnosticControls.DiagnosticChannelConnectionString)
            retriesLeft -= 1
        if not self.telemetry_client.getOnlineStatus():
            raise Exception("Unable to connect.")
