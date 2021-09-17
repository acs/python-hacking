from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel, ValidationError


class User(BaseModel):
    id: int
    name = "Lisa Perez"
    signup_ts: Optional[datetime] = None
    friends: List[int] = []

    class Config:
        extra = 'forbid'


external_data = {
    "id1": 1,
    "id": 1,
    "signup_ts": "2021-01-10 10:00",
    "friends": []
}

if __name__ == '__main__':
    try:
        user = User(**external_data)
        print(user.dict())
    except ValidationError as e:
        print(e.json())


