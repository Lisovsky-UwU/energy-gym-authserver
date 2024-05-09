from enum import Enum
from dataclasses import dataclass

from .access_rights import AccessRights


@dataclass
class ApiMethod:
    access   : str
    endpoint : str
    needjson : bool


class MainServerApiMethods(Enum):

    GYM_NEWS_CREATE    = ApiMethod(access = AccessRights.ADS.CREATE,           endpoint = 'gym-news/create',    needjson = True)
    GYM_NEWS_GET       = ApiMethod(access = AccessRights.ADS.GET,              endpoint = 'gym-news/get',       needjson = False)
    GYM_NEWS_GET_ANY   = ApiMethod(access = AccessRights.ADS.GETANY,           endpoint = 'gym-news/get-any',   needjson = False)
    GYM_NEWS_EDIT      = ApiMethod(access = AccessRights.ADS.EDIT,             endpoint = 'gym-news/edit',      needjson = True)
    GYM_NEWS_DELETE    = ApiMethod(access = AccessRights.ADS.DELETE,           endpoint = 'gym-news/delete',    needjson = True)

    AVTIME_CREATE      = ApiMethod(access = AccessRights.AVAILABLETIME.CREATE, endpoint = 'avtime/create',      needjson = True)
    AVTIME_GET         = ApiMethod(access = AccessRights.AVAILABLETIME.GET,    endpoint = 'avtime/get',         needjson = False)
    AVTIME_GET_ANY     = ApiMethod(access = AccessRights.AVAILABLETIME.GETANY, endpoint = 'avtime/get-any',     needjson = False)
    AVTIME_EDIT        = ApiMethod(access = AccessRights.AVAILABLETIME.EDIT,   endpoint = 'avtime/edit',        needjson = True)
    AVTIME_DELETE      = ApiMethod(access = AccessRights.AVAILABLETIME.DELETE, endpoint = 'avtime/delete',      needjson = True)

    ENTRY_CREATE       = ApiMethod(access = AccessRights.ENTRY.CREATE,         endpoint = 'entry/create',       needjson = True)
    ENTRY_CREATE_ANY   = ApiMethod(access = AccessRights.ENTRY.EDITANY,        endpoint = 'entry/create-any',   needjson = True)
    ENTRY_CHECK_OPEN   = ApiMethod(access = AccessRights.ENTRY.CREATE,         endpoint = 'entry/check-open',   needjson = False)
    ENTRY_CHANGE_OPEN  = ApiMethod(access = AccessRights.ENTRY.EDITANY,        endpoint = 'entry/change-open',  needjson = True)
    ENTRY_GET          = ApiMethod(access = AccessRights.ENTRY.GET,            endpoint = 'entry/get',          needjson = False)
    ENTRY_GET_ANY      = ApiMethod(access = AccessRights.ENTRY.GETANY,         endpoint = 'entry/get-any',      needjson = False)
    ENTRY_DELETE       = ApiMethod(access = AccessRights.ENTRY.DELETE,         endpoint = 'entry/delete',       needjson = True)
    ENTRY_DELETE_ANY   = ApiMethod(access = AccessRights.ENTRY.EDITANY,        endpoint = 'entry/delete-any',   needjson = True)

    USER_CREATE        = ApiMethod(access = AccessRights.USER.CREATE,          endpoint = 'user/create',        needjson = True)
    USER_GET           = ApiMethod(access = AccessRights.USER.GET,             endpoint = 'user/get',           needjson = False)
    USER_EDIT          = ApiMethod(access = AccessRights.USER.EDIT,            endpoint = 'user/edit',          needjson = True)
    USER_EDIT_PASSWORD = ApiMethod(access = AccessRights.USER.EDIT,            endpoint = 'user/edit-password', needjson = True)
    USER_EDIT_ANY      = ApiMethod(access = AccessRights.USER.EDITANY,         endpoint = 'user/edit-any',      needjson = True)
    USER_DELETE_ANY    = ApiMethod(access = AccessRights.USER.EDITANY,         endpoint = 'user/delete-any',    needjson = True)

    VISIT_GET          = ApiMethod(access = AccessRights.VISIT.GET,            endpoint = 'visit/get',          needjson = False)
    VISIT_EDIT         = ApiMethod(access = AccessRights.VISIT.EDIT,           endpoint = 'visit/edit',         needjson = True)

    REPORT_VISITS      = ApiMethod(access = AccessRights.REPORTS,              endpoint = 'report/visits',      needjson = True)
