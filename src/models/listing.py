from dataclasses import dataclass
from typing import Optional

@dataclass
class Listing:
    price: float
    area_m2: Optional[float]
    neighbourhood: str
    url: str
    
