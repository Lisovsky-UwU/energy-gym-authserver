from typing import Optional, List
from sqlalchemy import and_

from .abc import BaseService
from ...orm import User
from ...models import UserRole

class UserDBService(BaseService[User]):
    
    def get_by_student_card(self, stud_card: int, roles: List[UserRole] = [ UserRole.STUDENT, UserRole.BLOCKED ], get_deleted: Optional[bool] = False) -> Optional[User]:
        return self.get_filtered_first(
            and_(
                User.student_card == stud_card,
                User.role.in_(roles)
            ),
            get_deleted
        )
