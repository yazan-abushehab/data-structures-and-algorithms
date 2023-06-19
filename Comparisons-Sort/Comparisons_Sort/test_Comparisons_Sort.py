import pytest
from Comparisons_Sort.Comparisons_Sort import Movie, sort_by_year_descending, sort_by_title_ignoring_articles

@pytest.fixture

def sample_movies():
    return [
        Movie("The Avengers", 2012, ["Action", "Adventure", "Sci-Fi"]),
        Movie("Anchorman: The Legend of Ron Burgundy", 2004, ["Comedy"]),
        Movie("A Beautiful Mind", 2001, ["Biography", "Drama"]),
        Movie("The Dark Knight", 2008, ["Action", "Crime", "Drama"]),
    ]


def test_sort_by_year_descending(sample_movies):
    sorted_movies = sort_by_year_descending(sample_movies)
    assert len(sorted_movies) == 4
    assert sorted_movies[0].title == "The Avengers"
    assert sorted_movies[1].title == "The Dark Knight"
    assert sorted_movies[2].title == "Anchorman: The Legend of Ron Burgundy"
    assert sorted_movies[3].title == "A Beautiful Mind"


def test_sort_by_title_ignoring_articles(sample_movies):
    sorted_movies = sort_by_title_ignoring_articles(sample_movies)
    assert len(sorted_movies) == 4
    assert sorted_movies[0].title == "A Beautiful Mind"
    assert sorted_movies[1].title == "Anchorman: The Legend of Ron Burgundy"
    assert sorted_movies[2].title == "The Avengers"
    assert sorted_movies[3].title == "The Dark Knight"