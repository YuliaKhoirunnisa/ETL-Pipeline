import requests
from bs4 import BeautifulSoup
from datetime import datetime, timezone
import time

BASE_URL = "https://fashion-studio.dicoding.dev"

def scrape_page(page_num):
    if page_num == 1:
        url = BASE_URL
    else:
        url = f"{BASE_URL}/page{page_num}"
        
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error scraping page {page_num}: {e}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    products = []

    product_cards = soup.select("div.collection-card")
    print(f"Ditemukan {len(product_cards)} produk di halaman {page_num}")

    for card in product_cards:
        try:
            details = card.select_one("div.product-details").text.strip()
            lines = details.split('\n')
            if len(lines) >= 6:
                title = lines[0].strip()
                price = lines[1].strip()
                rating = lines[2].strip()
                colors = lines[3].strip()
                size = lines[4].strip()
                gender = lines[5].strip()
            else:
                title = details
                price = rating = colors = size = gender = "N/A"

            products.append({
                "Title": title,
                "Price": price,
                "Rating": rating,
                "Colors": colors,
                "Size": size,
                "Gender": gender,
                "timestamp": datetime.now(timezone.utc).isoformat()
            })
        except Exception:
            continue

    return products

def extract_all_pages(total_pages=50):
    all_products = []
    for page in range(1, total_pages + 1):
        print(f"\n🔄 Scraping halaman {page}")
        products = scrape_page(page)
        all_products.extend(products)
        time.sleep(1)  # delay antar halaman
    return all_products