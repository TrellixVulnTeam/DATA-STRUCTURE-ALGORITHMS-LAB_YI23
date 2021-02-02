class Movie:
    def __init__(self):
        self.number = None
        self.description = None
        self.rating = None
        self.availability = None

    def set_info(self, number, description, rating, availability):
        self.number = number
        self.description = description
        self.rating = rating
        self.availability = availability

    def display(self):
        print(
            f"Movie Number: {self.number} Movie Description: {self.description} Movie Rating: {self.rating} Movie Availability {self.availability}")


class Movies:
    def __init__(self):
        self.movies = list()

    def load_movies(self):
        movie_list = Movie()
        list = [(1, "movie1", 0, True), (2, "movie2", 0, True), (3, "movie3", 0, True)]
        for iteration in (list):
            movie_list.set_info(iteration[0], iteration[1], iteration[2], iteration[3])
            self.movies.append(movie_list.number)

    def view_all_movies(self):
        print("All Movies")
        for movie in self.movies:
            print(movie)


    def View_all_available_movies(self):
        pass

    def View_all_unavailable_movies(self):
        pass


if __name__ == "__main__":
    movies = Movies()
    movies.load_movies()
    movies.view_all_movies()

    # user_choice = "1"
    #
    # while user_choice == "1":
    #     menu = Menu()


