from pydantic import BaseModel

class trans(str,Enum):
    manual = "manual"
    automatic = "automatic"
    cvt = "cvt"
    amt = "amt"



class Car(BaseModel):   
    id: optional[UUID] = uuid4
    name: str
    engine: str
    Bhp: int
    Torque: int
    top_speed: int
    fuel_tank: int
    fuel_type: str
    transmission: trans
    country: str
    