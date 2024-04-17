import jwt
from datetime import datetime

from ..orm import User
from ..exceptions import LoginError
from ..services.database import UserDBService


SECRET_KEY = '9NAqbu8VWFWJjPPL8wIF6H9PwSemkRqDVQQ'


class AuthController: 

    def __init__(self, user_service: UserDBService):
        self.user_service = user_service

    
    def generate_token(self, user_id: int) -> str:
        return jwt.encode(
            {
                'user_id': user_id,
                'create_at': datetime.now().strftime('%m/%d/%Y %H:%M:%S'),
            },
            SECRET_KEY,
            algorithm='HS256'
        )
    

    def get_user(self, token: str) -> User:
        try:
            data = jwt.decode(
                token,
                SECRET_KEY,
                algorithms=['HS256']
            )
        except jwt.exceptions.DecodeError:
            raise LoginError('Неверный токен')

        user = self.user_service.get_by_id(data['user_id'])
        if user is None:
            raise LoginError('Неверный токен')
        
        return user
