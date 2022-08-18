from typing import Optional

from sqlmodel import SQLModel, Field

class Accommodation(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    keyword: str = Field(index=True)
    link: str
    
class Finance(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    keyword: str = Field(index=True)
    link: str
    
class Careers(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    keyword: str = Field(index=True)
    link: str
    
class ExamsAndAssessment(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    keyword: str = Field(index=True)
    link: str

class CourseInfo(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    keyword: str = Field(index=True)
    link: str
    
class Chaplaincy(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    keyword: str = Field(index=True)
    link: str
    
class Societies(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    keyword: str = Field(index=True)
    link: str

class Crime(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    keyword: str = Field(index=True)
    link: str
    
class Health(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    keyword: str = Field(index=True)
    link: str
    
class Library(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    keyword: str = Field(index=True)
    link: str
    
class MentalHealth(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    keyword: str = Field(index=True)
    link: str
    
class Success(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    keyword: str = Field(index=True)
    link: str
    
class Travel(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    keyword: str = Field(index=True)
    link: str
    
class StudentStatus(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    keyword: str = Field(index=True)
    link: str
    
class Discount(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    keyword: str = Field(index=True)
    link: str



