class TelemetryClient:
    DIAGNOSTIC_MESSAGE = "AT#UD"

    def __init__(self):
        self.onlineStatus = False
        self._diagnosticMessageResult = ""

    def disconnect(self):
        pass

    def getOnlineStatus(self):
        pass

    def connect(self, DiagnosticChannelConnectionString):
        pass

    def send(self, DIAGNOSTIC_MESSAGE):
        pass

    def receive(self):
        pass
