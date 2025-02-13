# for data validation

from pydantic import BaseModel, PositiveFloat, PositiveInt
from typing import Optional, Dict, List
from datetime import datetime
import logfire 


# logfire.configure()
# logfire.instrument_pydantic()

class Delivery(BaseModel):
    driver_id: int
    timestamp: datetime
    dimensions: dict[str, int]
    
   
# this will record details of a successful validation to logfire
m = Delivery(driver_id=201, timestamp='2020-01-02T03:04:05Z', dimensions={'Bag of rice': 20})
print(m.model_dump())