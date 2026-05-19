from pydantic import (
    BaseModel,
    EmailStr,
    Field
)

from typing import Optional


class LeadModel(BaseModel):

    name: str = Field(
        ...,
        min_length=2,
        max_length=100
    )

    email: EmailStr

    company: str = Field(
        ...,
        min_length=2,
        max_length=100
    )

    phone: str = Field(
        ...,
        min_length=7,
        max_length=15
    )

    source: Optional[str] = "Inbound"