from enum import Enum


class MainServerApiMethods(Enum):

    USER_CREATE     = {'method': 'POST', 'endpoint': 'user/create'}
    USER_GET_ALL    = {'method': 'GET',  'endpoint': 'user/get-all'}

    AVTIME_GET_ALL  = {'method': 'GET',  'endpoint': 'avtime/get-all'}

    ENTRY_CREATE    = {'method': 'POST', 'endpoint': 'entry/create'}
    ENTRY_GET_ALL   = {'method': 'GET',  'endpoint': 'entry/get-all'}
    ENTRY_GET       = {'method': 'GET',  'endpoint': 'entry/get'}
