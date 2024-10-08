from fastapi import FastAPI, Path, HTTPException
from .scraper import scrape_content
from .models import ScrapedResponse

app = FastAPI()

@app.get("/get/{phone_number}", response_model=ScrapedResponse)
async def scrape_endpoint(
    phone_number: str = Path(
        ..., 
        title="Phone Number",
        description="A 10-digit phone number, e.g., 0866246630",
        regex="^\d{10}$"  # Regex to ensure exactly 10 digits
    )
):
    # If additional validation or processing is needed, you can add it here
    return await scrape_content(phone_number)
