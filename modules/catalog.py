from modules.book import Book
from modules.magazine import Magazine
from modules.cd import CD
from modules.dvd import DVD


class Catalog():
    def __init__(self, catalog):
        self.catalog = catalog

    def search(self, input_search):
        list_result = []
        for catalog_item in self.catalog:
            for item in catalog_item:
                if input_search.lower() in item.title.lower():
                    if type(item) is Magazine:
                        list_result.append(
                            f'Title: {item.title}, '
                            f'Volume: {item.volume}, '
                            f'Type Catalog: Magazine'
                        )
                    elif type(item) is Book:
                        list_result.append(
                            f'Title: {item.title}, '
                            f'Authors: {item.authors}, '
                            f'Type Catalog: Book'
                        )
                    elif type(item) is CD:
                        list_result.append(
                            f'Title: {item.title}, '
                            f'Artist: {item.artist}, '
                            f'Type Catalog: CD'
                        )
                    elif type(item) is DVD:
                        list_result.append(
                            f'Title: {item.title}, '
                            f'subject: {item.subject}, '
                            f'upc: {item.upc}, '
                            f'Actors: {item.actors}, '
                            f'Directors: {item.directors}, '
                            f'Genre: {item.genre}, '
                            f'Type Catalog: DVD'
                        )
        return list_result
