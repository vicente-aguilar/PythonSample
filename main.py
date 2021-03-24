""""
Best Picture Nominees
- Minari
- Sound of Metal
- Mank
- Promising Young Woman
- The Father
- Judas and the Black Messiah
- The Trial of the Chigago 7
- Nomadland
For each movie, obtain:
- Year
- Rating
- Director(s)
- Plot
- Cast (top 5)
- Genre
 Create a dictionary  and store the output in a file called output.txt
Post the source code and the output file in your github.
Share the link with sarifern@cisco.com
"""

from imdb import IMDb

# create an instance of the IMDb class
ia = IMDb()

list_of_movie_id = ['0133093','0133095']

for movie in list_of_movie_id:

  movie = ia.get_movie(movie)
  name_of_movie = movie.values()[0]
  year = movie['year']
  rating = movie['rating']

  directors = []
  for director in movie['directors']:
      directors.append(director['name'])
  
  plot = movie['plot']
  actors = []

  for actor in movie['cast']:
      actors.append(actor['name'])
  genre = movie['genre']

  #Saving the dictionary 
  movies_dictionary = {
    "name": name_of_movie,
    "year": year,
    "director": directors,
    "plot": plot,
    "cast":actors[0:5],
    "gendre": genre 
  };

  with open('archivo_nuevo.txt','w') as f:
    f.write("Movie: " + str(name_of_movie)+"\r\n")
    f.write("Year: " + str(year)+"\r\n")
    f.write("Rating: " + str(rating)+"\r\n")
    f.write("Director: " + str(directors)+"\r\n")
    f.write("Plot: " + str(plot)+"\r\n")
    f.write("Cast: " + str(actors[0:5])+"\r\n")
    f.write("Gendre: " + str(genre)+"\r\n")
    


# Print the values
print(name_of_movie)
print(year)
print(rating)
print(directors)
print(plot)
print(actors[0:5])
print(genre)

#escribir en un archivo