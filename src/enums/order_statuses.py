from enum import Enum

class OrderStatuses(str, Enum):
    SEARCHING_FOR_DRIVER = "searching_for_driver"
    WAITING_FOR_DRIVER = "waiting_for_driver"
    WAITING_FOR_CLIENT = "waiting_for_client"
    IN_PROGRESS = "in_progress"
    CANCELED = "canceled"
    COMPLETED = "completed"