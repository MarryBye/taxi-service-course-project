from enum import Enum


class CarStatus(str, Enum):
    available = "available"
    on_maintenance = "on_maintenance"
    busy = "busy"
    not_working = "not_working"


class CarClass(str, Enum):
    standard = "standard"
    comfort = "comfort"
    business = "business"


class MaintenanceStatus(str, Enum):
    diagnosis = "diagnosis"
    in_progress = "in_progress"
    completed = "completed"


class OrderStatus(str, Enum):
    searching_for_driver = "searching_for_driver"
    waiting_for_driver = "waiting_for_driver"
    waiting_for_client = "waiting_for_client"
    in_progress = "in_progress"
    waiting_for_marks = "waiting_for_marks"
    canceled = "canceled"
    completed = "completed"


class TransactionType(str, Enum):
    debit = "debit"
    credit = "credit"
    refund = "refund"
    penalty = "penalty"


class PaymentMethod(str, Enum):
    credit_card = "credit_card"
    cash = "cash"


class BalanceType(str, Enum):
    payment = "payment"
    earning = "earning"


class UserRole(str, Enum):
    admin = "admin"
    driver = "driver"
    client = "client"


class CityName(str, Enum):
    Kyiv = "Kyiv"
    Lviv = "Lviv"
    Odessa = "Odessa"
    Dnipro = "Dnipro"
    Kharkiv = "Kharkiv"


class CountryName(str, Enum):
    Ukraine = "Ukraine"


class ClientTag(str, Enum):
    accurate = "accurate"
    friendly = "friendly"
    respectful = "respectful"
    communicative = "communicative"
    polite = "polite"


class DriverTag(str, Enum):
    accurate = "accurate"
    fast = "fast"
    friendly = "friendly"
    clean = "clean"
    modern_car = "modern_car"
    polite = "polite"
    communicative = "communicative"
    helpful = "helpful"


class DriverCancelTag(str, Enum):
    reason_1 = "reason 1"
    reason_2 = "reason 2"
    reason_3 = "reason 3"


class ClientCancelTag(str, Enum):
    reason_1 = "reason 1"
    reason_2 = "reason 2"
    reason_3 = "reason 3"
