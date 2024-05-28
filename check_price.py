# %%
import requests
import bs4
import os

URL = "https://www.kay.com/memories-moments-magic-diamond-engagement-ring-13-ct-tw-roundcut-10k-white-gold/p/V-991145905"

response = requests.get(URL)
soup = bs4.BeautifulSoup(response.content, "html.parser")
soup = soup.find(name="span", attrs={"class": "product-price__price"})
price = soup.get_text(strip=True).replace("Price", "")
status = requests.post(f"https://push.techulus.com/api/v1/notify/{os.environ['PUSH_API_KEY']}", json={
    "title": "💍 Ring Price Notification 💍",
    "body": price,
    "link": URL,
}).status_code
assert status == 200, f"Status {status}"

# %%
