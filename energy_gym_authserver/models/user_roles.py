from enum import Enum

from .access_rights import AccessRights


class UserRole(Enum):
    
    STUDENT = [
        AccessRights.ADS.GET,
        AccessRights.AVAILABLETIME.GET,
        AccessRights.ENTRY.CREATE,
        AccessRights.ENTRY.GET,
        AccessRights.ENTRY.DELETE,
        AccessRights.USER.EDIT,
        AccessRights.USER.DELETE
    ]

    COACH = [
        AccessRights.ADS.GET,
        AccessRights.ADS.EDIT,
        AccessRights.ADS.CREATE,
        AccessRights.ADS.DELETE,
        AccessRights.AVAILABLETIME.GET,
        AccessRights.AVAILABLETIME.GETANY,
        AccessRights.ENTRY.GET,
        AccessRights.ENTRY.GETANY,
        AccessRights.USER.GET,
        AccessRights.USER.EDIT,
        AccessRights.USER.DELETE,
        AccessRights.VISIT.GET,
        AccessRights.VISIT.EDIT,
    ]

    ADMIN = [
        *AccessRights.get_all_rights()
    ]
