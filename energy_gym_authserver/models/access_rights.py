from typing import List


class AdsAccess:

    '''Права допступов для информации по объявлениям'''
    CREATE = 'ads create'
    GET    = 'ads get'
    EDIT   = 'ads edit'
    DELETE = 'ads delete'

    @classmethod
    def get_all_rights(cls) -> List:
        return [
            cls.CREATE,
            cls.GET,
            cls.EDIT,
            cls.DELETE,
        ]


class AvailableTimeAccess:

    '''Права доступов для информации по дням для записи'''
    CREATE  = 'available time create'
    GET     = 'available time get'
    EDIT    = 'available time edit'
    DELETE  = 'available time delete'

    @classmethod
    def get_all_rights(cls) -> List:
        return [
            cls.CREATE,
            cls.GET,
            cls.EDIT,
            cls.DELETE,
        ]


class UserAccess:

    '''Права доступов для информации по пользователям'''
    EDITANY = 'user edit any'
    GETANY  = 'user get any'
    CREATE  = 'user create'
    GET     = 'user get'
    EDIT    = 'user edit'
    DELETE  = 'user delete'

    @classmethod
    def get_all_rights(cls) -> List:
        return [
            cls.EDITANY,
            cls.GETANY,
            cls.CREATE,
            cls.GET,
            cls.EDIT,
            cls.DELETE,
        ]


class EntyAccess:
    '''Права доступов для информации по записям'''

    EDITANY = 'entry edit any'
    GETANY  = 'entry get any'
    CREATE  = 'entry create'
    GET     = 'entry get'
    DELETE  = 'entry delete'

    @classmethod
    def get_all_rights(cls) -> List:
        return [
            cls.EDITANY,
            cls.GETANY,
            cls.CREATE,
            cls.GET,
            cls.DELETE,
        ]


class AccessRights:
    '''Права доступов для редактирования и получения данных'''

    ADS           = AdsAccess
    AVAILABLETIME = AvailableTimeAccess
    USER          = UserAccess
    ENTRY         = EntyAccess

    @classmethod
    def get_all_rights(cls) -> List:
        return [
            *cls.ADS.get_all_rights(),
            *cls.AVAILABLETIME.get_all_rights(),
            *cls.USER.get_all_rights(),
            *cls.ENTRY.get_all_rights(),
        ]
