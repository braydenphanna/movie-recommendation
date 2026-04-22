import json

class Movie:
    def __init__(self, id, title, overview, poster_path, genre_ids, popularity,release_date,vote_average,vote_count):
        self.id = id
        self.title = title
        self.overview = overview
        self.poster_path = poster_path
        self.genre_ids = genre_ids
        self.popularity = popularity
        self.release_date=release_date
        self.vote_average=vote_average
        self.vote_count=vote_count

    def __str__(self):
        return str(self.title)
    
    def to_dict(self):
        return self.__dict__
    
    @classmethod
    def from_json(cls, entry):
        if "genre_ids" in entry:
            genres = entry["genre_ids"]
        elif "genres" in entry:
            genres = [g["id"] for g in entry["genres"]]
        else:
            genres = []

        return cls(
            entry["id"],
            entry["title"],
            entry["overview"],
            entry.get("poster_path"),
            genres,
            entry["popularity"],
            entry["release_date"],
            entry["vote_average"],
            entry["vote_count"]
        )