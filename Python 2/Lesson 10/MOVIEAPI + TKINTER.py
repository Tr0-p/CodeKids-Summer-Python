import tkinter as tk
from tkinter import messagebox
import requests

OMDB_API_KEY = "e1239c51"
OMDB_API_URL = "http://www.omdbapi.com/"

def get_movie_info(title):
    params = {
        "apikey": OMDB_API_KEY,
        "t": title
    }
    response = requests.get(OMDB_API_URL, params=params)
    data = response.json()

    if data['Response'] == 'False':
        messagebox.showerror("Error", data['Error'])
        return

    movie_info = f"""
    Title: {data.get('Title')}
    Year: {data.get('Year')}
    Rated: {data.get('Rated')}
    Released: {data.get('Released')}
    Runtime: {data.get('Runtime')}
    Genre: {data.get('Genre')}
    Director: {data.get('Director')}
    Plot: {data.get('Plot')}
    Country: {data.get('Country')}
    Metascore: {data.get('Metascore')}
    """
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, movie_info)

def search_movie(query):
  params = {
    "apikey": OMDB_API_KEY,
    "s": query
  }
  response = requests.get(OMDB_API_URL, params=params)
  data = response.json()

  if data['Response'] == 'False':
      messagebox.showerror("Error", data['Error'])
      return

  search_results = data.get('Search', [])
  results = "\n".join([f"Title: {result.get('Title')}, Year: {result.get('Year')}" for result in search_results])

  result_text.delete(1.0, tk.END)
  result_text.insert(tk.END, results)

def on_get_movie_info():
  title = title_entry.get()
  if not title:
    messagebox.showwarning("Input Error", "Please enter a movie title.")
  else:
    get_movie_info(title)

def on_search_movie():
  query = search_entry.get()
  if not query:
    messagebox.showwarning("Input Error", "Please enter a search query.")
  else:
    search_movie(query)

#GUI
root = tk.Tk()
root.title("Summer's Movie Information App")

#Movie title entry
title_label = tk.Label(root, text="Enter a movie title:")
title_label.pack()
title_entry = tk.Entry(root, width=50)
title_entry.pack()

#Get movie info button
get_movie_buttion = tk.Button(root, text="Get Movie Info", command=on_get_movie_info)
get_movie_buttion.pack()

#Search query entry
search_label = tk.Label(root, text="Enter a search query:")
search_label.pack()
search_entry = tk.Entry(root, width=50)
search_entry.pack()

#Search button
search_button = tk.Button(root, text="Search", command=on_search_movie)
search_button.pack()

#Text widget to display results
result_text = tk.Text(root, height=20, width=80)
result_text.pack()

root.mainloop()
