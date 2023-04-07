from enum import Enum

from .access_rights import AccessRights


class UserRole(Enum):
    
    STUDENT = [
        AccessRights.ADS.GET,
        AccessRights.AVAILABLETIME.GET,
        AccessRights.ENTRY.CREATE,
        AccessRights.ENTRY.GET,
        AccessRights.ENTRY.DELETE,
        AccessRights.USER.GET,
        AccessRights.USER.EDIT,
        AccessRights.USER.DELETE
    ]

    ADMIN = [
        *AccessRights.get_all_rights()
    ]
