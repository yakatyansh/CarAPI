from pydantic import BaseModel
from typing import Optional
from uuid import UUID, uuid4
from enum import Enum

class trans(str,Enum):
    manual = "manual"
    automatic = "automatic"
    cvt = "cvt"
    amt = "amt"



class Car(BaseModel):   
    name: str
    engine: str
    Bhp: int
    Torque: int
    top_speed: int
    fuel_tank: int
    fuel_type: str
    transmission: trans
    country: str
    number_of_cylinders: int
    