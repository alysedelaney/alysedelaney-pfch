import cloudscraper
from bs4 import BeautifulSoup

artist_list = []

pages = [1,2]

for page in pages:

    base_url = f"https://www.moma.org/artists/?exhibition_id=5224&page={page}"

    scraper = cloudscraper.create_scraper()
    page = scraper.get(base_url)
    soup = BeautifulSoup(page.text, "html.parser")
    artist_container = soup.find('section', {'data-grid' : 'artists'})
    artist_title = artist_container.find_all('h3', {'class':'typography'})

    for artist in artist_title:
        name = artist.find('span').get_text()
        artist_list.append(name)

print(artist_list)
print(len(artist_list))
