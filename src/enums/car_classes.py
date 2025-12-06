from enum import Enum

class CarClass(str, Enum):
    STANDARD = "standard"
    COMFORT = "comfort"
    BUSINESS = "business"