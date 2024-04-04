import uuid
from datetime import date, datetime, timedelta
from pydantic import BaseModel, confloat, validator
from enum import Enum
from typing import Literal


# define an Enum of acceptable Department values
class DepartmentEnum(Enum):
    ARTS_AND_HUMANITIES = "Arts and Humanities"
    LIFE_SCIENCES = "Life Sciences"
    SCIENCE_AND_ENGINEERING = "Science and Engineering"


class Module(BaseModel):
    id: int | uuid.UUID
    name: str
    professor: str
    credits: Literal[10, 20]
    registration_code: str


class Student(BaseModel):
    id: uuid.UUID
    name: str
    date_of_birth: date
    GPA: confloat(ge=0, le=4)
    course: str | None
    department: DepartmentEnum
    fees_paid: bool
    modules: list[Module] = []

    @validator("date_of_birth")
    def ensure_16_or_over(cls, value):
        sixteen_years_ago = datetime.now() - timedelta(days=365 * 16)

        # convert datetime object -> date
        sixteen_years_ago = sixteen_years_ago.date()

        # raise error if DOB is more recent than 16 years past.
        if value > sixteen_years_ago:
            raise ValueError("Too young to enrol, sorry!")
        return value
