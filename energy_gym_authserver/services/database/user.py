from typing import Optional
from sqlalchemy import and_

from .abc import BaseService
from ...orm import User
from ...models import UserRole

class UserDBService(BaseService[User]):
    
    def get_by_student_card(self, stud_card: int, role: UserRole = UserRole.STUDENT, get_deleted: Optional[bool] = False) -> Optional[User]:
        return self.get_filtered_first(
            and_(
                User.student_card == stud_card,
                User.role == role.name
            ),
            get_deleted
        )
