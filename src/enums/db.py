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
    ACCURATE = "accurate"
    FRIENDLY = "friendly"
    RESPECTFUL = "respectful"
    COMMUNICATIVE = "communicative"
    POLITE = "polite"
    ON_TIME = "on_time"
    CLEAR_INSTRUCTIONS = "clear_instructions"
    CALM = "calm"
    HELPFUL = "helpful"
    OTHER = "other"

class DriverTags(str, Enum):
    ACCURATE = "accurate"
    FAST = "fast"
    FRIENDLY = "friendly"
    CLEAN = "clean"
    MODERN_CAR = "modern_car"
    POLITE = "polite"
    COMMUNICATIVE = "communicative"
    HELPFUL = "helpful"
    SMOOTH_DRIVING = "smooth_driving"
    SAFE_DRIVING = "safe_driving"
    GOOD_NAVIGATION = "good_navigation"
    OTHER = "other"

class DriverCancelTags(str, Enum):
    CLIENT_NOT_RESPONDING = "client_not_responding"
    CLIENT_NOT_AT_PICKUP_POINT = "client_not_at_pickup_point"
    VEHICLE_BREAKDOWN = "vehicle_breakdown"
    TRAFFIC_ACCIDENT = "traffic_accident"
    UNSAFE_PICKUP_LOCATION = "unsafe_pickup_location"
    ROUTE_UNREACHABLE = "route_unreachable"
    EMERGENCY = "emergency"
    OTHER = "other"

class ClientCancelTags(str, Enum):
    DRIVER_TOO_FAR = "driver_too_far"
    LONG_WAIT_TIME = "long_wait_time"
    CHANGED_PLANS = "changed_plans"
    WRONG_PICKUP_LOCATION = "wrong_pickup_location"
    FOUND_ANOTHER_TRANSPORT = "found_another_transport"
    DRIVER_NOT_RESPONDING = "driver_not_responding"
    PRICE_TOO_HIGH = "price_too_high"
    EMERGENCY = "emergency"
    OTHER = "other"

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