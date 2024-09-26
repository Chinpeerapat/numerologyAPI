from pydantic import BaseModel
from typing import List

class ScrapedResponse(BaseModel):
    phone_number: str
    scraped_paragraphs: List[str]
    paragraph_count: int