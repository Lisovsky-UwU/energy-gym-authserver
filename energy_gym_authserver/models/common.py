from enum import Enum
from dataclasses import dataclass

from .access_rights import AccessRights


@dataclass
class ApiMethod:
    access   : str
    endpoint : str
    needjson : bool


class MainServerApiMethods(Enum):

    ADS_CREATE        = ApiMethod(access = AccessRights.ADS.CREATE,           endpoint = 'ads/create',        needjson = True)
    ADS_GET           = ApiMethod(access = AccessRights.ADS.GET,              endpoint = 'ads/get',           needjson = False)
    ADS_GET_ANY       = ApiMethod(access = AccessRights.ADS.GETANY,           endpoint = 'ads/get-any',       needjson = False)
    ADS_EDIT          = ApiMethod(access = AccessRights.ADS.EDIT,             endpoint = 'ads/edit',          needjson = True)
    ADS_DELETE        = ApiMethod(access = AccessRights.ADS.DELETE,           endpoint = 'ads/delete',        needjson = True)

    AVTIME_CREATE     = ApiMethod(access = AccessRights.AVAILABLETIME.CREATE, endpoint = 'avtime/create',     needjson = True)
    AVTIME_GET        = ApiMethod(access = AccessRights.AVAILABLETIME.GET,    endpoint = 'avtime/get',        needjson = False)
    AVTIME_GET_ANY    = ApiMethod(access = AccessRights.AVAILABLETIME.GETANY, endpoint = 'avtime/get-any',    needjson = False)
    AVTIME_EDIT       = ApiMethod(access = AccessRights.AVAILABLETIME.EDIT,   endpoint = 'avtime/edit',       needjson = True)
    AVTIME_DELETE     = ApiMethod(access = AccessRights.AVAILABLETIME.DELETE, endpoint = 'avtime/delete',     needjson = True)

    ENTRY_CREATE      = ApiMethod(access = AccessRights.ENTRY.CREATE,         endpoint = 'entry/create',      needjson = True)
    ENTRY_CREATE_ANY  = ApiMethod(access = AccessRights.ENTRY.EDITANY,        endpoint = 'entry/create-any',  needjson = True)
    ENTRY_CHECK_OPEN  = ApiMethod(access = AccessRights.ENTRY.CREATE,         endpoint = 'entry/check-open',  needjson = False)
    ENTRY_CHANGE_OPEN = ApiMethod(access = AccessRights.ENTRY.EDITANY,        endpoint = 'entry/change-open', needjson = True)
    ENTRY_GET         = ApiMethod(access = AccessRights.ENTRY.GET,            endpoint = 'entry/get',         needjson = False)
    ENTRY_GET_ANY     = ApiMethod(access = AccessRights.ENTRY.GETANY,         endpoint = 'entry/get-any',     needjson = False)
    ENTRY_DELETE      = ApiMethod(access = AccessRights.ENTRY.DELETE,         endpoint = 'entry/delete',      needjson = True)
    ENTRY_DELETE_ANY  = ApiMethod(access = AccessRights.ENTRY.EDITANY,        endpoint = 'entry/delete-any',  needjson = True)

    USER_CREATE       = ApiMethod(access = AccessRights.USER.CREATE,          endpoint = 'user/create',       needjson = True)
    USER_GET          = ApiMethod(access = AccessRights.USER.GET,             endpoint = 'user/get',          needjson = False)
    USER_GET_ANY      = ApiMethod(access = AccessRights.USER.GETANY,          endpoint = 'user/get-any',      needjson = False)
    USER_EDIT         = ApiMethod(access = AccessRights.USER.EDIT,            endpoint = 'user/edit',         needjson = True)
    USER_EDIT_ANY     = ApiMethod(access = AccessRights.USER.EDITANY,         endpoint = 'user/edit-any',     needjson = True)
    USER_DELETE_ANY   = ApiMethod(access = AccessRights.USER.EDITANY,         endpoint = 'user/delete-any',   needjson = True)
