from pydantic import BaseModel

from app.stores.user import BaseUserStore, MemoryUserStore

user_store = MemoryUserStore()


class CommonParameters(BaseModel):
    user_store: BaseUserStore

    class Config:
        arbitrary_types_allowed = True


def common_parameters() -> CommonParameters:
    return CommonParameters(user_store=user_store)
