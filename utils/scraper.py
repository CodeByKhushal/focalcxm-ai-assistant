import requests
# Used to fetch webpage HTML content

from bs4 import BeautifulSoup
# Used to parse and clean HTML


def get_page_text(url):

    try:
        # Browser-like headers to reduce 403 Forbidden errors
        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        # Send GET request to webpage
        response = requests.get(
            url,
            headers=headers,
            timeout=15
        )

        # Raise error if request fails
        response.raise_for_status()

        # Parse HTML content
        soup = BeautifulSoup(response.text, "html.parser")

        # Remove unwanted HTML sections
        for tag in soup(["script", "style", "nav", "footer", "header"]):
            tag.decompose()

        # Extract clean readable text
        text = soup.get_text(separator=" ")

        # Remove unnecessary spaces/newlines
        return " ".join(text.split())

    except Exception as e:
        # Print error if scraping fails
        print(f"Error scraping {url}: {e}")

        return ""