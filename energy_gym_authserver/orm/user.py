from typing import Any, Dict, Optional
from sqlalchemy import Enum
from sqlalchemy.orm import Mapped, mapped_column

from . import Base
from ..models import UserRole


class User(Base):

    __tablename__ = 'users'

    id           : Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    student_card : Mapped[int] = mapped_column(unique=True, index=True)
    firstname    : Mapped[str]
    secondname   : Mapped[str]
    surname      : Mapped[str]
    group        : Mapped[str]
    hid          : Mapped[str]
    image        : Mapped[Optional[str]]
    role         : Mapped[UserRole] = mapped_column(Enum(UserRole))
    deleted      : Mapped[bool] = mapped_column(server_default='false')


    def to_dict(
        self, 
        get_id: Optional[bool] = False,
        get_deleted: Optional[bool] = False,
    ) -> Dict[str, Any]:
        _dict = {
            'studentCard' : self.student_card,
            'firstname'   : self.firstname,
            'secondname'  : self.secondname,
            'surname'     : self.surname,
            'group'       : self.group,
            'image'       : self.image,
            'role'        : self.role.name if isinstance(self.role, UserRole) else self.role,
        }
        
        if get_id: _dict['id'] = self.id
        if get_deleted: _dict['deleted'] = self.deleted

        return _dict
