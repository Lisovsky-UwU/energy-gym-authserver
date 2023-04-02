class EnergyGymAuthServerException(Exception):
    '''Базовое исключение сервера'''


class DataBaseException(EnergyGymAuthServerException):
    '''Исключение при при ошибке в работе с базой данных'''


class MainServerRequestException(EnergyGymAuthServerException):
    '''Исключение при возвращении ошибки от главного сервера'''

    def __init__(self, *args: object, status_code: int = 500) -> None:
        super().__init__(*args)
        self.status_code = status_code


class InvalidRequestException(EnergyGymAuthServerException):
    '''Исключение при неверном запросе'''


class LoginError(EnergyGymAuthServerException):
    '''Исключение при ошибке входа'''
    status_code = 401


class RegistrationError(EnergyGymAuthServerException):
    '''Исключение при ошибке регистрации'''
    status_code = 401


class AccessRightsException(EnergyGymAuthServerException):
    '''Исключение при недостаточных правах доступа'''
    status_code = 403
