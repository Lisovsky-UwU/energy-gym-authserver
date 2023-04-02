from typing import List


class AvailableTimeAccess:

    '''Права доступов для информации по дням для записи'''
    CREATE  = 'available time create'
    GET     = 'available time get'
    DELETE  = 'available time delete'

    @classmethod
    def get_all_rights(cls) -> List:
        return [
            cls.CREATE,
            cls.GET,
            cls.DELETE,
        ]


class UserAccess:

    '''Права доступов для информации по пользователям'''
    EDITANY = 'user edit any'
    CREATE  = 'user create'
    GET     = 'user get'
    DELETE  = 'user delete'

    @classmethod
    def get_all_rights(cls) -> List:
        return [
            cls.EDITANY,
            cls.CREATE,
            cls.GET,
            cls.DELETE,
        ]


class EntyAccess:
    '''Права доступов для информации по записям'''

    EDITANY = 'entry edit any'
    CREATE  = 'entry create'
    GET     = 'entry get'
    DELETE  = 'entry delete'

    @classmethod
    def get_all_rights(cls) -> List:
        return [
            cls.EDITANY,
            cls.CREATE,
            cls.GET,
            cls.DELETE,
        ]


class AccesRights:
    '''Права доступов для редактирования и получения данных'''

    AVAILABLETIME = AvailableTimeAccess
    USER          = UserAccess
    ENTRY         = EntyAccess

    @classmethod
    def get_all_rights(cls) -> List:
        return [
            *cls.AVAILABLETIME.get_all_rights(),
            *cls.USER.get_all_rights(),
            *cls.ENTRY.get_all_rights(),
        ]
