class Movie:
    def __init__(self, title, year, genres):
        self.title = title
        self.year = year
        self.genres = genres


def sort_by_year_descending(movies):
    return sorted(movies, key=lambda movie: (-movie.year, movie.title))

def sort_by_title_ignoring_articles(movies):
    ignored_articles = ["A", "An", "The"]

    def remove_leading_articles(title):
        words = title.split(" ")
        if words[0] in ignored_articles:
            return " ".join(words[1:])
        return title

    return sorted(movies, key=lambda movie: remove_leading_articles(movie.title.lower()))

