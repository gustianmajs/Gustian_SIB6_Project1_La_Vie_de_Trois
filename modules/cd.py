from modules.library_item import LibraryItem


class CD(LibraryItem):
    def __init__(self, title, upc, subject, artist):
        super().__init__(title, upc, subject)
        self.artist = artist
