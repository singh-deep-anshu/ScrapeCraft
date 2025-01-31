from bs4 import BeautifulSoup
from scrapingbee import ScrapingBeeClient

YOUR_UNIQUE_API_KEY = "3d93af34c819470699020e8caa4909da"

def scrape_web(website):
    client = ScrapingBeeClient(api_key='2J1HBYTJ5BHAIAJMQSMLO6Q7SS17EKJGSGKN8P9YM4ZJ9AB8MBLACG9NKC8CTDCX7VXFGXRQLB0L665J')
    response = client.get(website,
        params = { 
            'block_ads': 'True',
            'block_resources': 'True',
        }
    )
    print('Response HTTP Status Code: ', response.status_code)
    print('Response HTTP Response Body: ', response.content)
    return response.content

def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""

def clean_body_content(body_content):
    soup = BeautifulSoup(body_content,"html.parser")

    for scr_or_style in soup(["script","style"]):
        scr_or_style.extract()

    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip()
    )

    return cleaned_content

def split_dom_content(dom_content, max_length=6000):
    return [
        dom_content[i:i+max_length] for i in range(0,len(dom_content),max_length)
    ]