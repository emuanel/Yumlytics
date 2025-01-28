class InvalidURLException(BaseException):
    def __init__(self, file_type, message="Invalid file type"):
        self.message = f"{message}: {file_type}"
        super().__init__(self.message)


class VideoPreprocessingException(BaseException):
    def __init__(self, error_details, message="Error occurred while preprocessing document file"):
        self.message = f"{message}: {error_details}"
        super().__init__(self.message)


class VideoTranscriptionException(BaseException):
    def __init__(self, error_details, message="Error occurred during ROI detection"):
        self.message = f"{message}: {error_details}"
        super().__init__(self.message)


class ProviderInvalidApiKeyException(BaseException):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class ProviderModelException(BaseException):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class ProviderRateLimitExceededException(BaseException):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class ProviderTimeoutException(BaseException):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class ProviderApiException(BaseException):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
