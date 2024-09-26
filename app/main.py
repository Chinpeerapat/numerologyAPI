from fastapi import FastAPI
from .scraper import scrape_content
from .models import ScrapedResponse

app = FastAPI()

@app.get("/get/{phone_number}", response_model=ScrapedResponse)
async def scrape_endpoint(phone_number: str):
    return await scrape_content(phone_number)