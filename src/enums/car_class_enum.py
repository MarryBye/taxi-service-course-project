from enum import Enum

class CarClassEnum(str, Enum):
    STANDARD = 'Standard'
    COMFORT = 'Comfort'
    BUSINESS = 'Business'