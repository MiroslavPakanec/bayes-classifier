import traceback
from fastapi import HTTPException
from loguru import logger

class SampleValidationException(HTTPException):
    def __init__(self, detail: str, status_code: int = 400):
        self.log_error(detail)
        super().__init__(status_code=status_code, detail=detail)
    
    @staticmethod
    def log_error(detail: str):
        logger.error('[VALIDATION ERROR]')
        logger.error(detail)
        logger.error(traceback.format_exc())

class InvalidSampleLengthException(SampleValidationException):
    def __init__(self, actual_len):
        super().__init__(detail=f'Sample length must be 784 ({actual_len} given).')

class InvalidSamplePixelValueException(SampleValidationException):
    def __init__(self, detail: str = 'Every sample pixel value must be between 0-255 (inclusive).'):
        super().__init__(detail=detail)