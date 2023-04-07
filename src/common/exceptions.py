class ApplicationError(Exception):
    def __init__(self, message, status=400, extra=None):
        super().__init__(message)

        self.message = message
        self.status = status
        self.extra = extra or {}
