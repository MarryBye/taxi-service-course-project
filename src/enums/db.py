from enum import Enum

class CarStatuses(str, Enum):
    AVAILABLE = "available"
    ON_MAINTENANCE = "on_maintenance"
    BUSY = "busy"
    NOT_WORKING = "not_working"

class CarClasses(str, Enum):
    STANDARD = "standard"
    COMFORT = "comfort"
    BUSINESS = "business"

class MaintenanceStatuses(str, Enum):
    DIAGNOSIS = "diagnosis"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"

class OrderStatuses(str, Enum):
    SEARCHING_FOR_DRIVER = "searching_for_driver"
    WAITING_FOR_DRIVER = "waiting_for_driver"
    WAITING_FOR_CLIENT = "waiting_for_client"
    IN_PROGRESS = "in_progress"
    WAITING_FOR_MARKS = "waiting_for_marks"
    CANCELED = "canceled"
    COMPLETED = "completed"

class TransactionType(str, Enum):
    DEBIT = "debit"
    CREDIT = "credit"
    REFUND = "refund"
    PENALTY = "penalty"

class PaymentMethods(str, Enum):
    CREDIT_CARD = "credit_card"
    CASH = "cash"

class BalanceTypes(str, Enum):
    PAYMENT = "payment"
    EARNING = "earning"

class UserRoles(str, Enum):
    ADMIN = "admin"
    DRIVER = "driver"
    CLIENT = "client"
    GUEST = "guest"

class ClientTags(str, Enum):
    accurate = "accurate"
    friendly = "friendly"
    respectful = "respectful"
    communicative = "communicative"
    polite = "polite"
    on_time = "on_time"
    clear_instructions = "clear_instructions"
    calm = "calm"
    helpful = "helpful"
    other = "other"

class DriverTags(str, Enum):
    accurate = "accurate"
    fast = "fast"
    friendly = "friendly"
    clean = "clean"
    modern_car = "modern_car"
    polite = "polite"
    communicative = "communicative"
    helpful = "helpful"
    smooth_driving = "smooth_driving"
    safe_driving = "safe_driving"
    good_navigation = "good_navigation"
    other = "other"

class DriverCancelTags(str, Enum):
    client_not_responding = "client_not_responding"
    client_not_at_pickup_point = "client_not_at_pickup_point"
    vehicle_breakdown = "vehicle_breakdown"
    traffic_accident = "traffic_accident"
    unsafe_pickup_location = "unsafe_pickup_location"
    route_unreachable = "route_unreachable"
    emergency = "emergency"
    other = "other"

class ClientCancelTags(str, Enum):
    driver_too_far = "driver_too_far"
    long_wait_time = "long_wait_time"
    changed_plans = "changed_plans"
    wrong_pickup_location = "wrong_pickup_location"
    found_another_transport = "found_another_transport"
    driver_not_responding = "driver_not_responding"
    price_too_high = "price_too_high"
    emergency = "emergency"
    other = "other"

class Colors(str, Enum):
    RED = "red"
    BLUE = "blue"
    GREEN = "green"
    BLACK = "black"
    WHITE = "white"
    YELLOW = "yellow"
    ORANGE = "orange"
    PURPLE = "purple"
    BROWN = "brown"
    PINK = "pink"
    GRAY = "gray"
    SILVER = "silver"
    GOLD = "gold"