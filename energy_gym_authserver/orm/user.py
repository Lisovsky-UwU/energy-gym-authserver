from typing import Any
from typing import Dict
from typing import Optional
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import Boolean
from sqlalchemy.orm import relationship
from flask_login import UserMixin

from . import Base


class User(Base, UserMixin):

    __tablename__ = 'users'

    id            = Column(Integer, primary_key=True, autoincrement=True)
    student_card  = Column(Integer, nullable=False, unique=True)
    firstname     = Column(String(30), nullable=False)
    secondname    = Column(String(30), nullable=False)
    surname       = Column(String(30), nullable=False, default='')
    group         = Column(String(20), nullable=False)
    password      = Column(String(60), nullable=False)
    role          = Column(String(15), nullable=False, index=True)
    deleted       = Column(Boolean, default=False)

    tokens        = relationship('Token', back_populates='users',  uselist=True)


    def to_dict(
        self, 
        get_id: Optional[bool] = False,
        get_password: Optional[bool] = False,
        get_deleted: Optional[bool] = False,
    ) -> Dict[str, Any]:
        _dict = {
            'student_card' : self.student_card,
            'firstname'    : self.firstname,
            'secondname'   : self.secondname,
            'surname'      : self.surname,
            'group'        : self.group,
            'role'         : self.role,
        }
        
        if get_id: _dict['id'] = self.id
        if get_password: _dict['password'] = self.password
        if get_deleted: _dict['deleted'] = self.deleted

        return _dict
