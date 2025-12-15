from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from src.enums.db import MaintenanceStatus
from src.schemas.common import AddressSchema
from src.schemas.mixins.hashable_password import WithHashablePassword
from src.schemas.users import *