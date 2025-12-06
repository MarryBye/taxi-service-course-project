from enum import Enum

class CarStatus(str, Enum):
    AVAILABLE = "available"
    ON_MAINTENANCE = "on_maintenance"
    BUSY = "busy"
    NOT_WORKING = "not_working"
    