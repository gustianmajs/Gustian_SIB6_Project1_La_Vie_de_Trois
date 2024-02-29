import json
from modules.book import Book
from modules.magazine import Magazine
from modules.cd import CD
from modules.dvd import DVD
from modules.catalog import Catalog

f = open('files/catalog.json')
data_json = json.load(f)

books = []
magazines = []
cds = []
dvds = []

for item in data_json:
    if item['source'] == 'book':
        books.append(
            Book(
                title=item['title'],
                subject=item['subject'],
                upc=item['upc'],
                issbn=item['issbn'],
                authors=item['authors'],
                dds_number=item['dds_number']
            )
        )
    elif item['source'] == 'magazine':
        magazines.append(
            Magazine(
                title=item['title'],
                subject=item['subject'],
                upc=item['upc'],
                volume=item['volume'],
                issue=item['issue']
            )
        )
    elif item['source'] == 'cd':
        cds.append(
            CD(
                title=item['title'],
                upc=item['upc'],
                subject=item['subject'],
                artist=item['artist']
            )
        )
    elif item['source'] == 'dvd':
        dvds.append(
            DVD(
                title=item['title'],
                subject=item['subject'],
                upc=item['upc'],
                actors=item['actors'],
                directors=item['directors'],
                genre=item['genre']
            )
        )

catalog_all = [books, magazines, cds, dvds]
input_search = 'test'
results = Catalog(catalog_all).search(input_search)

for index, result in enumerate(results):
    print(f'Results-{index + 1} | {result}')
