from pydantic import BaseModel
from typing import List, Optional

class Observation(BaseModel):
    email_id: int
    subject: str
    body: str
    sender: str

class Action(BaseModel):
    category: str   # work / spam / personal
    priority: str   # high / medium / low
    response: Optional[str]

class Reward(BaseModel):
    score: float
    feedback: str
