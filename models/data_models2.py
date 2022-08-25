from typing import Optional
from unicodedata import category

from sqlmodel import SQLModel, Field

class NoCatergory(SQLModel):
    id: Optional[int] = Field(primary_key=True)
    keyword: str = Field(index=True)
    link: str
    
class Catergory(SQLModel):
    id: Optional[int] = Field(primary_key=True)
    category: str = Field(index=True)
    keyword: str
    link: str
    
class Careers(NoCatergory, table=True):
    pass

class Crime(NoCatergory, table=True):
    pass

class Dental(NoCatergory, table=True):
    pass

class Doctor(NoCatergory, table=True):
    pass
    
class HallSenior(NoCatergory, table=True):
    pass

class Finances(NoCatergory, table=True):
    pass

class Library(NoCatergory, table=True):
    pass

class GeneralAccommodation(NoCatergory, table=True):
    pass
    
class MentalHealth(NoCatergory, table=True):
    pass

class PrivateHousing(NoCatergory, table=True):
    pass

class SpecificHalls(Catergory, table=True):
    pass

class SummerAccommodation(NoCatergory, table=True):
    pass

class TuitionFees(NoCatergory, table=True):
    pass