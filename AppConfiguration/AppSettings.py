from enum import Enum
import os


class AppSettings(Enum):
    user = os.environ['MYSQL_USER']
    password = os.environ['MYSQL_PASSWORD']
    host = os.environ['MYSQL_HOST']
    database = os.environ['MYSQL_DATABASE']
    port = os.environ['MYSQL_PORT']
    kompetence = os.getenv('COMPETENCE_ID', None)
    advert = os.getenv('ADVERT_ID', None)

