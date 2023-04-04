import cloudscraper
from bs4 import BeautifulSoup

pages = [1,2]
artist_hrefs = []

for page in pages:
    exhibition_url = f"https://www.moma.org/artists/?exhibition_id=5224&page={page}"
    scraper = cloudscraper.create_scraper()
    page = scraper.get(exhibition_url)
    soup = BeautifulSoup(page.text, "html.parser")
    artist_container = soup.find('section', {'data-grid' : 'artists'})
    artist_links = artist_container.find_all("a", {'data-gtm' : "clicks on artist"})
    for link in artist_links:  
        artist_hrefs.append(link['href'])

artist_info = {}

# counter = 1
for href in artist_hrefs:
    # print(counter)
    artist_url = f"https://www.moma.org/{href}"
    scraper = cloudscraper.create_scraper()
    page = scraper.get(artist_url)
    soup = BeautifulSoup(page.text, "html.parser")
    artist_name = soup.find('h1').text.strip()
    artist_bio = soup.find('h2').get_text(strip=True)
    artist_works = soup.find('p', {'class' : '$color/alpha:54% $typography/size:medium typography layout/margin:top:page:2'})
    if artist_works is None: 
        artist_works = ""
    else: 
        artist_works = artist_works.get_text(strip=True)
    artist_info[artist_name] = {
        "bio" : artist_bio,
        "works" : artist_works
    }

print(artist_info)



