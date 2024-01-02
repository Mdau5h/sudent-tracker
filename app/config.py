import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    TOKEN: str = os.getenv('TOKEN')
    ACCESS_CODE: str = os.getenv('ACCESS_CODE')
    APP_NAME: str = 'student-tracker'
    CODE_ATTEMPTS: int = 5


config = Config()
