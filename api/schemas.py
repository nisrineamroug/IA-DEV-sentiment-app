"""Request and response contracts for the API."""
from pydantic import BaseModel, ConfigDict, Field, field_validator


class PredictRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")
    text: str = Field(min_length=1, max_length=2000)

    @field_validator("text")
    @classmethod
    def reject_whitespace(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("text must contain non-whitespace characters")
        return value


class PredictResponse(BaseModel):
    label: str
    score: float = Field(ge=0, le=1)
    text: str
    abstained: bool
