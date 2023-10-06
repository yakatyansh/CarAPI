from fastapi import FastAPI
from models import Car
from typing import List

app = FastAPI()

db: List[Car] = [
    Car(name= "Fiat Avventura Abarth",number_of_cylinder=4, engine= "1.4L", Bhp= 140, Torque= 220, top_speed= 195, fuel_tank= 45, fuel_type= "Petrol", transmission= "manual", country= "Italy"),
    Car(name= "Ford Mustang", engine= "5.0L",number_of_cylinder=8, Bhp= 460, Torque= 569, top_speed= 250, fuel_tank= 60, fuel_type= "Petrol", transmission= "automatic", country= "USA"),
    Car(name= "Honda City", engine= "1.5L",number_of_cylinder=4, Bhp= 120, Torque= 145, top_speed= 180, fuel_tank= 45, fuel_type= "Petrol", transmission= "cvt", country= "Japan"),
    Car(name= "Hyundai Venue", engine= "1.5L", Bhp= 120, Torque= 145, top_speed= 180, fuel_tank= 45, fuel_type= "Petrol", transmission= "amt", country= "South Korea"),
    Car(name= "Kia Seltos", engine= "1.5L", Bhp= 120,number_of_cylinder=4, Torque= 145, top_speed= 180, fuel_tank= 45, fuel_type= "Petrol", transmission= "cvt", country= "South Korea"),
    Car(name= "Maruti Suzuki Swift", engine= "1.2L",number_of_cylinder=4, Bhp= 83, Torque= 113, top_speed= 180, fuel_tank= 40, fuel_type= "Petrol", transmission= "manual", country= "India"),
    Car(name= "Mercedes-Benz S-Class", engine= "3.0L",number_of_cylinder=6, Bhp= 362, Torque= 500, top_speed= 250, fuel_tank= 80, fuel_type= "Petrol", transmission= "automatic", country= "Germany"),
    Car(name= "MG Hector", engine= "2.0", Bhp= 143,number_of_cylinder=4, Torque= 250, top_speed= 180, fuel_tank= 45, fuel_type= "Diesel", transmission= "cvt", country= "China"),
    Car(name= "Nissan Kicks", engine= "1.5L",number_of_cylinder=4, Bhp= 106, Torque= 142, top_speed= 180, fuel_tank= 45, fuel_type= "Petrol", transmission= "manual", country= "Japan"),
    Car(name= "Renault Duster", engine= "1.3L",number_of_cylinder=4, Bhp= 154, Torque= 254, top_speed= 180, fuel_tank= 50, fuel_type= "Petrol", transmission= "automatic", country= "France")
]

@app.get("/")
async def root():
    return {"message": "welcome to the car api v0.0.1 by @yakatyansh"} 


@app.get("/api/v1/cars")
async def get_cars():
    return db