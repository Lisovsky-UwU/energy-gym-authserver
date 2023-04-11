from typing import Type
from loguru import logger

from ..orm import User
from ..models import UserRole
from ..exceptions import LoginError
from ..exceptions import RegistrationError
from ..services.database import UserDBService


class UserControleer:

    def __init__(self, user_service_type: Type[UserDBService]):
        self.user_service_type = user_service_type


    def registrate_user(
        self,
        student_card: int,
        name: str,
        group: str,
        password: str
    ) -> User:
        with self.user_service_type() as user_service:
            if user_service.get_by_student_card(student_card):
                raise RegistrationError('Данный номер студенческого уже зарегистрирован')
            
            user = user_service.create(
                User(
                    student_card = student_card,
                    name         = name,
                    group        = group,
                    password     = password,
                    role         = UserRole.STUDENT.name,
                )
            )
            user_service.commit()
            logger.trace(f'Зарегистрирован новый пользователь: {user.to_dict(get_id = True)}')

            return user
        

    def login_user(self, student_card: int, password: str) -> User:
        with self.user_service_type() as user_service:
            user = user_service.get_by_student_card(student_card)
            if user is None or user.password != password:
                raise LoginError('Неверный логин или пароль')
            
            return user
