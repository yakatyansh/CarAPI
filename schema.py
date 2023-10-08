from pydantic import BaseModel

class Car(BaseModel):
    name: str
    engine: str
    Bhp: int
    Torque: int
    top_speed: int
    fuel_tank: int
    fuel_type: str
    transmission: str
    country: str
    number_of_cylinders: int

    class Config:
        orm_mode = True