import logging

class ErrorLogger:
    def __init__(self, name='MathCafeLogger'):
        self.logger = self.setup_logger(name)

    def setup_logger(self, name):
        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)
        handler = logging.FileHandler('math_cafe_errors.log')
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        return logger

    def log_error(self, message):
        self.logger.error(message)

    def log_warning(self, message):
        self.logger.warning(message)

    def log_info(self, message):
        self.logger.info(message)

class MathCafeException(Exception):
    pass

class DatabaseException(MathCafeException):
    pass

class AuthenticationException(MathCafeException):
    pass

class ValidationException(MathCafeException):
    pass

class ServerException(MathCafeException):
    pass
