from typing import Any, Dict, Optional
from sqlalchemy import Column, String, Integer, Boolean, Text

from . import Base


class User(Base):

    __tablename__ = 'users'

    id            = Column(Integer, primary_key=True, autoincrement=True)
    student_card  = Column(Integer, nullable=False, unique=True)
    firstname     = Column(String(30), nullable=False)
    secondname    = Column(String(30), nullable=False)
    surname       = Column(String(30), nullable=False, default='')
    group         = Column(String(20), nullable=False)
    hid           = Column(Text, nullable=False)
    role          = Column(String(15), nullable=False, index=True)
    deleted       = Column(Boolean, default=False)


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
            'role'        : self.role,
        }
        
        if get_id: _dict['id'] = self.id
        if get_deleted: _dict['deleted'] = self.deleted

        return _dict
