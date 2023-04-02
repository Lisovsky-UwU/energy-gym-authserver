from typing import Optional

from .abc import BaseService
from ...orm import Token
from ...orm import User


class TokenDBService(BaseService[Token]):
    
    def get_by_token(self, token: str, get_deleted: Optional[bool] = False) -> Optional[Token]:
        return self.get_filtered_first(Token.token == token, get_deleted)
        
    
    def create_for_user(self, user: User) -> Token:
        return self.create(Token(user = user.id))
