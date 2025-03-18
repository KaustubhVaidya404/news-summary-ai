from bs4 import BeautifulSoup
import requests


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}


def format_company_name(inp):
    """Function to normalize the user input"""
    return inp.replace(" ", "").lower()

def extract_articles(company_name):
    """Function to extract the articles from times of india website"""

    name = format_company_name(company_name)
    url = f"https://timesofindia.indiatimes.com/topic/{name}/news"

    try:
        result = requests.get(url, headers=headers)

        soup = BeautifulSoup(result.text, 'html.parser')

        data = soup.find_all('div', class_='VXBf7')
        if data:
            articles = []
            for div in data:

                title = div.find('div', class_='fHv_i').get_text(strip=True) if div.find('div', class_='fHv_i') else "No title"
                date = div.find('div', class_='ZxBIG').get_text(strip=True) if div.find('div', class_='ZxBIG') else "No date"
                summary = div.find('p', class_='oxXSK').get_text(strip=True) if div.find('p', class_='oxXSK') else "No summary"

                article = {
                    'title': title,
                    'date': date,
                    'summary': summary
                }
                articles.append(article)
            return articles
        else:
            return "No data found."
    except(e):
        return f"Failed to fetch page. Status code: {result.status_code} {e}"
