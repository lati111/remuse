from ReMuse.DB import base
from tinydb import Query

class PlaylistDB(base.BaseDB):
    table = "playlist"

    def insert(self, title: str):
        self.db.insert({
            'title': title
        })

    def titleIsUnique(self, title: str):
        return self.db.search(Query().title == title) == []
