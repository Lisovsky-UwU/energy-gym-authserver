from enum import Enum
from dataclasses import dataclass

from .access_rights import AccesRights


@dataclass
class ApiMethod:
    access   : str
    endpoint : str


class MainServerApiMethods(Enum):

    USER_CREATE     = ApiMethod(access = AccesRights.USER.CREATE,       endpoint = 'user/create')
    USER_GET_ALL    = ApiMethod(access = AccesRights.USER.EDITANY,      endpoint = 'user/get-all')

    AVTIME_GET_ALL  = ApiMethod(access = AccesRights.AVAILABLETIME.GET, endpoint = 'avtime/get-all')

    ENTRY_CREATE    = ApiMethod(access = AccesRights.ENTRY.CREATE,      endpoint = 'entry/create')
    ENTRY_GET_ALL   = ApiMethod(access = AccesRights.ENTRY.EDITANY,     endpoint = 'entry/get-all')
    ENTRY_GET       = ApiMethod(access = AccesRights.ENTRY.GET,         endpoint = 'entry/get')
