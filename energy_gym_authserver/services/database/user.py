from typing import Optional

from .abc import BaseService
from ...orm import User


class UserDBService(BaseService[User]):
    
    def get_by_student_card(self, stud_card: int, get_deleted: Optional[bool] = False) -> Optional[User]:
        return self.get_filtered_first(User.student_card == stud_card, get_deleted)
