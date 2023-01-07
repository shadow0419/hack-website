from typing import Optional

from pydantic import BaseModel, EmailStr, Field, HttpUrl

from .utils import form_body


@form_body
class RawApplicationData(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    gender: str
    pronouns: str
    ethnicity: str
    is_18_older: bool
    university: str
    education_level: str
    major: str
    is_first_hackathon: bool
    portfolio_link: Optional[HttpUrl]
    linkedin_link: Optional[HttpUrl]
    stress_relief_question: str = Field(max_length=4096)
    company_specialize_question: str = Field(max_length=4096)

    class Config:
        anystr_strip_whitespace = True
        max_anystr_length = 254


class ProcessedApplicationData(RawApplicationData):
    resume_url: HttpUrl
