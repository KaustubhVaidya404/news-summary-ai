from bs4 import BeautifulSoup
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

company_name = input("Enter company name: \n")

url = f"https://timesofindia.indiatimes.com/topic/{company_name}/news"

try:
    result = requests.get(url, headers=headers)
    print(result.status_code)

    soup = BeautifulSoup(result.text, 'html.parser')

    data = soup.find_all('div', class_='VXBf7')
    if data:
        for div in data:
            print(div.prettify())
    else:
        print("No data found.")
except:
    print(f"Failed to fetch page. Status code: {result.status_code}")
