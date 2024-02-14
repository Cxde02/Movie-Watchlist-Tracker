import sqlite3

def insertMovieInfo():
    movieName = ''
    Genre = ''
    Date = ''
    Rating = ''

    movieName = input("Enter movie name: ")
    Genre = input("Enter genre: ")
    Date = input("Enter date (DD-MMM-YYYY): ")
    Rating = int(input("Enter rating (1-10): "))

    while True:
        if (Rating < 1) or (Rating > 10):
            print('Invalid rating. Please enter a number between 1 and 10')
            Rating = int(input("Enter rating again: "))
        else:
            break
    
    # Return the variables as a tuple
    return (movieName, Genre, Date, Rating)

# Call the function and store the returned values
movies = insertMovieInfo()


# Connect to the database (will create it if it doesn't exist)
conn = sqlite3.connect('db/moviesWatchlist.db')
cursor = conn.cursor()

# Create a table called Movies
cursor.execute("CREATE TABLE IF NOT EXISTS Movies (Title TEXT, Genre TEXT, Date DATE, Ratings INTEGER)")

'''
# Insert 4 rows into the Movies table
movies = [
    ('Eternals', 'Action, Adventure, Fantasy', '07 Feb 2024', 3),
    ('65', 'Action, Adventure, Drama', '27 Jan 2024', 7),
    ('How to Train Your Dragon', 'Animation, Action, Adventure', '13 Feb 2024', 10),
    ('The Marvels', 'Action, Adventure, Fantasy', '20 Jan 2024', 7)
]
'''

# Access the variables from the returned tuple
movieName, Genre, Date, Rating = movies

cursor.execute('INSERT INTO Movies (Title, Genre, Date, Ratings) VALUES (?, ?, ?, ?)', movies)


# Commit the changes and close the connection
conn.commit()
conn.close()
print("Data inserted successfully!")

