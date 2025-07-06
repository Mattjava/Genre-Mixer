import requests
from bs4 import BeautifulSoup
# This function removes a specific substring from a string
# This substring is based on the variable part.
# It splits the string into an array, and appends all elements into the string
# This will result in an string that doesn't contain the string in part

# This function is useful because of how everynoise.com works
# Each genre has their own page, and they appear in its url with no whitespaces
# This function enables BeautifulSoup to find the webpage and scrape it.
def remove_part(word, part):
    word_array = word.split(part)
    new_word = ""
    for part in word_array:
        new_word += part
    return new_word

# This function removes any duplicates from an array
# It firsts sorts the array using a built-in python method.
# It then goes through the list. If it detects an element that is equal to the element next to it, it
# deletes it.
# At the end, an array with 0 duplicate elements should appear

# This function is useful to ensure there are no duplicate artists in each generated playlist
# Although removing duplicates makes the playlist smaller, it ensures that there is a diverse amount
# of artists within each generate playlist.
def remove_duplicates(arr):
    arr.sort()
    scope_length = len(arr) - 2
    i = 0
    while i < scope_length:
        if arr[i] == arr[i + 1]:
            arr.remove(arr[i])
            i -= 1
        i += 1
        scope_length = len(arr) - 2

# This class handles Genre
# It has two attributes: name and artists
# Name contains the name of the genre.
# Artist contains every artist that has created a song for that genre
# It finds these artist by webscraping a website called everynoise.com
# It finds the genre's webpage and collects every artist that appears.
# It then saves those artist into array. Any duplicate artist will be removed.
class Genre:
    def __init__(self, genre_name):
        self.name = remove_part(genre_name, " ")
        if "-" in self.name:
            self.name = remove_part(self.name, "-")

        try:
            genre_page = requests.get(f"https://everynoise.com/engenremap-{self.name}.html").text
            genre_soup = BeautifulSoup(genre_page, "html.parser")
        except:
            raise Exception("Genre cannot be found on the website.")
        else:
            self.artists = genre_soup.find_all("div", class_="genre scanme")
            self.artists = [x.get_text() for x in self.artists]
            self.artists = [x[:len(x)-2] for x in self.artists]
            remove_duplicates(self.artists)

    def __str__(self):
        return "" + self.name
