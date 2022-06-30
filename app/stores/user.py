from typing import Dict, Union

from app.models.user import UserDB


class BaseUserStore:
    def __init__(self) -> None:
        pass

    def add_user(self, user: UserDB) -> None:
        pass

    def get_user_by_id(self, id: str) -> Union[UserDB, None]:
        pass


class MemoryUserStore(BaseUserStore):
    def __init__(self) -> None:
        self.db_dict: Dict[str, Dict[str, str]] = {}

    def add_user(self, user: UserDB) -> None:
        self.db_dict[user.id] = user.dict()

    def get_user_by_id(self, id: str) -> Union[UserDB, None]:
        user_data = self.db_dict.get(id)
        if not user_data:
            return None

        return UserDB.parse_obj(user_data)


class TestUserStore(MemoryUserStore):
    def reset_store(self) -> None:
        self.db_dict = {}
