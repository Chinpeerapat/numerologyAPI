import requests
from bs4 import BeautifulSoup
from fastapi import HTTPException

async def scrape_content(phone_number: str):
    url = f"https://www.somjade.com/ber/?{phone_number}"
    
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all <p> tags
        paragraphs = soup.find_all('p')
        
        # Extract text from each <p> tag
        scraped_data = [p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True)]
        
        return {
            "phone_number": phone_number,
            "scraped_paragraphs": scraped_data,
            "paragraph_count": len(scraped_data)
        }
    
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error fetching the URL: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")