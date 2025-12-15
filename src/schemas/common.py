from pydantic import BaseModel, Field
from src.enums.db import CountryName, CityName


class AddressSchema(BaseModel):
    country_name: CountryName = Field(..., alias="country_name", description="Country name", max_length=32)
    city_name: CityName = Field(..., alias="city_name", description="City name", max_length=32)
    street_name: str = Field(..., alias="street_name", description="Street name", max_length=32)
    house_number: str = Field(..., alias="house_number", description="House number", max_length=9)
    latitude: float = Field(..., alias="latitude", description="Latitude coordinate")
    longitude: float = Field(..., alias="longitude", description="Longitude coordinate")
