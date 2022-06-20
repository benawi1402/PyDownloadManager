from pydantic import BaseModel, ValidationError, validator
from helpers import is_path_exists_or_creatable


class Config(BaseModel):
    default_memory_limit_per_download: int = 50
    logging_path: str = "./py_download_manager.log"
    default_speed_limit_per_download: int = 1000
    default_download_concurrent_limit: int = 3

    @validator('default_memory_limit_per_download')
    def memory_limit_per_download_constrains(self, v):
        if v not in range(20, 10000):
            raise ValueError('Supplied default_memory_limit_per_download must be between 20 and 10000')
        return v

    @validator('logging_path')
    def check_logging_path(self, v):
        if not is_path_exists_or_creatable(v):
            raise ValueError('Supplied logging_path is invalid')
        return v

    @validator('default_speed_limit_per_download')
    def default_speed_limit_per_download_constrains(self, v):
        if v < 1:
            raise ValueError('Supplied default_speed_limit_per_download needs to be positive')
        return v

    @validator('default_download_concurrent_limit')
    def default_download_concurrent_limit(self, v):
        if v < 1:
            raise ValueError('Supplied default_download_concurrent_limit needs to be positive')
        return v
