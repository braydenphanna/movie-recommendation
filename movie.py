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
    
    # Creates a Movie object from the corresponding result in recommendations.json
    @classmethod
    def from_json(cls,result_number):
        with open("recommendations.json", "r") as file:
            data = json.load(file)
        entry = data["results"][result_number]
        return cls(entry["id"],entry["title"],entry["overview"],entry["poster_path"],entry["genre_ids"],entry["popularity"],entry["release_date"],entry["vote_average"],entry["vote_count"])