import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import os

BASE_URL = "http://books.toscrape.com/catalogue/page-{}.html"
OUTPUT_DIR = "data"

today = datetime.now().strftime("%Y-%m-%d")
output_file = os.path.join(OUTPUT_DIR, f"books_{today}.csv")

def extract_books_from_page(page_number):
    url = BASE_URL.format(page_number)
    response = requests.get(url)

    if response.status_code != 200:
        return []

    soup = BeautifulSoup(response.content, "html.parser")
    books = []

    articles = soup.select("article.product_pod")

    for article in articles:
        title = article.h3.a["title"]
        price = article.select_one(".price_color").text.replace("£", "").strip()
        availability = article.select_one(".availability").text.strip()
        rating = article.p["class"][1]

        books.append({
            "title": title,
            "price_gbp": price,
            "availability": availability,
            "rating": rating
        })

    return books

def save_books_to_csv(books):
    with open(output_file, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=books[0].keys())
        writer.writeheader()
        writer.writerows(books)

def main():
    all_books = []

    for page in range(1, 51):  
        print(f"Scraping page {page}...")
        books = extract_books_from_page(page)
        if not books:
            print(f"Aucune donnée trouvée à la page {page}. Arrêt du scraping.")
            break
        all_books.extend(books)

    save_books_to_csv(all_books)
    print(f"{len(all_books)} livres enregistrés dans {output_file}")


if __name__ == "__main__":
    main()