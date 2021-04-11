from typing import Optional, List

from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

class LocationPing(BaseModel):
    device_id: str
    location: str
    timestamp:Optional[str] = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")

class PowerStatusPing(BaseModel):
    device_id: str
    status: bool
    timestamp:Optional[str] = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")


location_database : List[LocationPing] = []
power_database : List[PowerStatusPing] = []


@app.get("/location")
def get_location_data():
    print("Timestamp | Device Id | Location")
    for location in location_database[::-1]: 
        print(' | '.join([location.timestamp, location.device_id, location.location]))
    return location_database

@app.get("/power")
def get_power_data():
    print("Timestamp | Device Id | Power Status")
    for power in power_database[::-1]: 
        status = lambda x: "ON" if x else "OFF"
        print(' | '.join([power.timestamp, power.device_id, status(power.status)]))
    return power_database

@app.post("/location")
def save_location(location_ping: LocationPing):
    location_database.append(location_ping)
    return "Saved location successfully for device id: " + location_ping.device_id

@app.post("/power")
def save_power_status(power_ping: PowerStatusPing):
    power_database.append(power_ping)
    return "Saved Power successfully for device id: " + power_ping.device_id


