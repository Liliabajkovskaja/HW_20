from enum import Enum


class Enviroments(Enum):
    DEV = 'dev'
    STAGE = 'stage'
    PROD = 'prod'


if __name__ == '__main__':
    print(Enviroments.DEV.value)
