from pydantic import BaseModel, Field
from typing import Optional
class RentalMetadata(BaseModel):
    agreement_value: Optional[str] = Field(default=None)
    agreement_start_date: Optional[str] = Field(default=None)
    agreement_end_date: Optional[str] = Field(default=None)
    renewal_notice_days: Optional[str] = Field(default=None)
    party_one: Optional[str] = Field(default=None)
    party_two: Optional[str] = Field(default=None)