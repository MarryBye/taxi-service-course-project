from enum import Enum

class UserRole(str, Enum):
    CLIENT = "client"
    DRIVER = "driver"
    MANAGER = "manager"
    ADMIN = "admin"