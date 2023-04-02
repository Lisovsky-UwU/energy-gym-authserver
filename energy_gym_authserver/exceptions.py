class EnergyGymAuthServerException(Exception):
    '''Базовое исключение сервера'''

class DataBaseException(EnergyGymAuthServerException):
    '''Исключение при при ошибке в работе с базой данных'''

class MainServerRequestException(EnergyGymAuthServerException):
    '''Исключение при возвращении ошибки от главного сервера'''

class InvalidRequestException(EnergyGymAuthServerException):
    '''Исключение при неверном запросе'''

class LoginError(EnergyGymAuthServerException):
    '''Исключение при ошибке входа'''
    status_code = 401

class RegistrationError(EnergyGymAuthServerException):
    '''Исключение при ошибке регистрации'''
    status_code = 401
