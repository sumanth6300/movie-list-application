import json

MOVIE_FILE = "movies.json"

def load_movies():
    try:
        with open(MOVIE_FILE, 'r') as file:
            movies = json.load(file)
    except FileNotFoundError:
        movies = []
    return movies

def save_movies(movies):
    with open(MOVIE_FILE, 'w') as file:
        json.dump(movies, file, indent=2)

def show_all_movies(movies):
    print("All Movies:")
    for movie in movies:
        print_movie_info(movie)

def add_new_movie():
    print("Add a New Movie:")
    title = input("Title: ")
    director = input("Director: ")
    release_year = input("Release Year: ")
    language = input("Language: ")
    rating = input("Rating: ")

    # Validate input (e.g., ensure release_year is a number, and rating is a float)
    try:
        release_year = int(release_year)
        rating = float(rating)
    except ValueError:
        print("Invalid input. Release Year should be a number, and Rating should be a float.")
        return

    movie = {
        'Name': title,
        'Director': director,
        'Release Year': release_year,
        'Language': language,
        'Rating': rating
    }

    movies = load_movies()
    movies.append(movie)
    save_movies(movies)
    print("Movie added successfully!")

def print_movie_info(movie):
    title = movie.get('Name', 'Title not available')
    print(f"Title: {title}")
    print(f"Director: {movie.get('Director', 'Director not available')}")
    print(f"Release Year: {movie.get('Release Year', 'Release Year not available')}")
    print(f"Language: {movie.get('Language', 'Language not available')}")
    print(f"Rating: {movie.get('Rating', 'Rating not available')}")
    print("-" * 20)

def filter_movies(criteria, value):
    movies = load_movies()
    filtered_movies = [movie for movie in movies if movie.get(criteria) == value]

    if filtered_movies:
        print(f"Movies filtered by {criteria} ({value}):")
        for movie in filtered_movies:
            print_movie_info(movie)
    else:
        print(f"No movies found for {criteria} ({value}).")

def search_for_movie():
    search_term = input("Enter the title of the movie to search for: ")
    filter_movies('Name', search_term)

def update_movie_details():
    director = input("Enter the director of the movie to update: ")
    movies = load_movies()

    for movie in movies:
        if movie.get('Director') == director:
            print("Current Movie Details:")
            print_movie_info(movie)
            
            movie['Name'] = input("Enter the new title: ")
            movie['Release Year'] = input("Enter the new Release Year: ")
            movie['Language'] = input("Enter the new Language: ")
            movie['Rating'] = input("Enter the new Rating: ")

            save_movies(movies)
            print("Movie details updated successfully!")
            return

    print(f"No movie found with director: {director}.")
    # Placeholder function for updating movie details
    #print("Update movie details function")

def delete_movie():
    director = input("Enter the director of the movie to delete: ")
    movies = load_movies()

    movies = [movie for movie in movies if movie.get('Director') != director]

    if len(movies) < len(load_movies()):
        save_movies(movies)
        print("Movie deleted successfully!")
    else:
        print(f"No movie found with director: {director}.")
    # Placeholder function for deleting a movie
   # print("Delete movie function")

def get_number_of_movies_in_language():
    language = input("Enter the language to get the number of movies: ")
    movies = load_movies()

    filtered_movies = [movie for movie in movies if movie.get('Language') == language]
    print(f"Number of movies in {language}: {len(filtered_movies)}")
    # Placeholder function for getting the number of movies in a specified language
    #print("Get number of movies in language function")

def main():
    while True:
        print("\nConsole-Based Movie List Application")
        print("1. Show all Movies")
        print("2. Add a New Movie")
        print("3. Filter Movies based on criteria")
        print("4. Search for a Movie")
        print("5. Update a Movie's Details")
        print("6. Delete a Movie")
        print("7. Get the number of movies in a specified language")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            show_all_movies(load_movies())
        elif choice == '2':
            add_new_movie()
        elif choice == '3':
            print("\nFilter Movies by Criteria:")
            print("1. Filter by Title")
            print("2. Filter by Director")
            print("3. Filter by Release Year")
            print("4. Filter by Language")
            print("5. Filter by Rating")
            filter_choice = input("Enter your choice (1-5): ")
            filter_criteria = {
                '1': 'Name',
                '2': 'Director',
                '3': 'Release Year',
                '4': 'Language',
                '5': 'Rating'
            }.get(filter_choice, 'Invalid Choice')
            
            if filter_criteria != 'Invalid Choice':
                filter_value = input(f"Enter the {filter_criteria} to filter: ")
                filter_movies(filter_criteria, filter_value)
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
        elif choice == '4':
            search_for_movie()
        elif choice == '5':
            update_movie_details()
        elif choice == '6':
            delete_movie()
        elif choice == '7':
            get_number_of_movies_in_language()
        elif choice == '8':
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

if __name__ == "__main__":
    main()
