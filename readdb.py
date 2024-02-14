import sqlite3

# Connect to the database
conn = sqlite3.connect('db/moviesWatchlist.db')
cursor = conn.cursor()

# Execute a query to select all rows from a table
cursor.execute('SELECT * FROM Movies')

# Fetch the column names from the cursor description
columns = [description[0] for description in cursor.description]

# Fetch all rows from the cursor
rows = cursor.fetchall()

# Calculate column widths
column_widths = [len(column) for column in columns]
for row in rows:
    for i, value in enumerate(row):
        column_widths[i] = max(column_widths[i], len(str(value)))

# Print the table header
print("+" + "+".join("-" * (width + 2) for width in column_widths) + "+")
print("|" + "|".join(f" {column.ljust(column_widths[i])} " for i, column in enumerate(columns)) + "|")
print("+" + "+".join("-" * (width + 2) for width in column_widths) + "+")

# Print the rows
for row in rows:
    print("|" + "|".join(f" {str(value).ljust(column_widths[i])} " for i, value in enumerate(row)) + "|")

# Print the table footer
print("+" + "+".join("-" * (width + 2) for width in column_widths) + "+")

def countNumberOfMovies():
    # Count number of movies in the list
    count = cursor.execute('SELECT COUNT(*) FROM Movies').fetchone()
    return count[0]

print("There are {} movies on your watchlist.".format(countNumberOfMovies()))

# Close the connection
conn.close()


