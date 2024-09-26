from fastapi import FastAPI, HTTPException
import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI
from .scraper import scrape_content
from .models import ScrapedResponse

app = FastAPI()

@app.get("/scrape/{phone_number}", response_model=ScrapedResponse)
async def scrape_endpoint(phone_number: str):
    return await scrape_content(phone_number)

    url = f"https://www.somjade.com/ber/?{phone_number}"
    
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract the relevant information (modify this part based on the website structure)
        result = {}
        
        # Example: Extract the title
        title = soup.find('title')
        if title:
            result['title'] = title.text.strip()
        
        # Example: Extract all paragraphs
        paragraphs = soup.find_all('p')
        result['paragraphs'] = [p.text.strip() for p in paragraphs]
        
        # Add more extraction logic as needed
        
        return result
    
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error fetching the URL: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)