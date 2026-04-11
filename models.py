from pydantic import BaseModel
from typing import List, Optional

class Observation(BaseModel):
    email_id: int
    subject: str
    body: str
    sender: str

class Action(BaseModel):
    category: str
    priority: str
    response: str
    action: str = "respond"

class Reward(BaseModel):
    score: float
    feedback: str
