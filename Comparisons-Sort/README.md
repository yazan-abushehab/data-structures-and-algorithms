# Comparisons-Sort
In the first half of this code challenge, you will write functions which sort domain objects. Your functions will receive an array of Movie objects. Each Movie object has a title (string), a year (number), and a list of genres (array of strings). One function will sort the movies by most recent year first. One function will sort the movies, alphabetical by title, but will ignore any leading “A”s, “An”s, or “The”s. Test outputs for these functions, and an array of sample data, have been provided in test and movies.

In the second half of the code challenge, you will write tests for your comparator functions. This may necessitate refactoring the code you wrote in part one. Your tests will need to call the comparator functions directly, and make assertions about the response values given test inputs.

<br>

## visual step through
Not Required

<br>

## Approach & Efficiency
Time: of sort_by_year_descending is also O(n log n), where n is the number of movies in the input list.
      of sort_by_title_ignoring_articles is O(n * k), where n is the number of movies in the input list.
Space: O(n) because the functions create a new sorted list as the output.

<br>

## Solution

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
