from enum import Enum
from dataclasses import dataclass

from .access_rights import AccessRights


@dataclass
class ApiMethod:
    access   : str
    endpoint : str


class MainServerApiMethods(Enum):

    ADS_CREATE       = ApiMethod(access = AccessRights.ADS.CREATE,           endpoint = 'ads/create')
    ADS_GET          = ApiMethod(access = AccessRights.ADS.GET,              endpoint = 'ads/get')
    ADS_EDIT         = ApiMethod(access = AccessRights.ADS.EDIT,             endpoint = 'ads/edit')
    ADS_DELETE       = ApiMethod(access = AccessRights.ADS.DELETE,           endpoint = 'ads/delete')

    AVTIME_CREATE    = ApiMethod(access = AccessRights.AVAILABLETIME.CREATE, endpoint = 'avtime/create')
    AVTIME_GET       = ApiMethod(access = AccessRights.AVAILABLETIME.GET,    endpoint = 'avtime/get')
    AVTIME_EDIT      = ApiMethod(access = AccessRights.AVAILABLETIME.EDIT,   endpoint = 'avtime/edit')
    AVTIME_DELETE    = ApiMethod(access = AccessRights.AVAILABLETIME.DELETE, endpoint = 'avtime/delete')

    ENTRY_CREATE     = ApiMethod(access = AccessRights.ENTRY.CREATE,         endpoint = 'entry/create')
    ENTRY_CREATE_ANY = ApiMethod(access = AccessRights.ENTRY.EDITANY,        endpoint = 'entry/create-any')
    ENTRY_GET        = ApiMethod(access = AccessRights.ENTRY.GET,            endpoint = 'entry/get')
    ENTRY_GET_ANY    = ApiMethod(access = AccessRights.ENTRY.GETANY,         endpoint = 'entry/get-any')
    ENTRY_DELETE     = ApiMethod(access = AccessRights.ENTRY.DELETE,         endpoint = 'entry/delete')
    ENTRY_DELETE_ANY = ApiMethod(access = AccessRights.ENTRY.EDITANY,        endpoint = 'entry/delete-any')

    USER_CREATE      = ApiMethod(access = AccessRights.USER.CREATE,          endpoint = 'user/create')
    USER_GET         = ApiMethod(access = AccessRights.USER.GET,             endpoint = 'user/get')
    USER_GET_ANY     = ApiMethod(access = AccessRights.USER.GETANY,          endpoint = 'user/get-any')
    USER_EDIT        = ApiMethod(access = AccessRights.USER.EDIT,            endpoint = 'user/edit')
    USER_EDIT_ANY    = ApiMethod(access = AccessRights.USER.EDITANY,         endpoint = 'user/edit-any')
    USER_DELETE      = ApiMethod(access = AccessRights.USER.DELETE,          endpoint = 'user/delete')
    USER_DELETE_ANY  = ApiMethod(access = AccessRights.USER.EDITANY,         endpoint = 'user/delete-any')
