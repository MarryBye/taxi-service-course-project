from enum import Enum

class CarStatusEnum(str, Enum):
    AVAILABLE = 'Available'
    ON_MAINTENANCE = 'On maintenance'
    BUSY = 'Busy'
    NOT_WORKING = 'Not working'
