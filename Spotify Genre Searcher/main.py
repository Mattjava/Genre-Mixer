import os, requests, random, spotipy
from spotipy import SpotifyOAuth
from bs4 import BeautifulSoup
from genre import Genre

# The scope the Spotipy API will check
scope = "playlist-modify-private,playlist-read-private,user-library-read,user-library-modify"

# Webscrapes an archive of everynoise.com
# I chose this archive in the event everynoise.com shuts down.
# I plan to use other websites or APIs should this link and other links used shut down
genre_scrape = requests.get("https://web.archive.org/web/20231112033936/http://everynoise.com/").text

genre_soup = BeautifulSoup(genre_scrape, "html.parser")

# Gathers a list of all genres and filters out to collect the names
genres = genre_soup.find_all("div", class_="genre scanme")

genres = [x.get_text() for x in genres]
genres = [x[:len(x)-2] for x in genres]

# Gets user input
user_input = input("Pick a specific genre you want to listen to (E.G. dream pop, nu metal, breakcore, etc).\nIf you don't know what to listen to, don't worry. We'll pick for you.\nEnter a genre you want to listen to: ")

# If the user inserts a genre that exist, the program will use it.
# Otherwise, if the user doesn't insert anything or inserts a string not present in the genre database, the
# program will randomly select a genre.
if user_input in genres:
    user_genre_input = user_input
else:
    user_genre_input = random.choice(genres)

# Creates a genre object using the inputted genre. Please view genre.py for more information
chosen_genre = Genre(user_genre_input)

# Connects to the Spotify API
# It relies on multiple environmental variables to pass sensitive information.
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.environ["CLIENT_ID"],client_secret=os.environ["CLIENT_SECRET"], redirect_uri=os.environ["REDIRECT_URI"], cache_path="token.txt", scope=scope, open_browser=True))

# Creates the song database
# Also creates the array where the artists from the genre object will be stored
songs = []
artists_chosen = []

# If the amount of artists in the genre object is greater than 100, it will randomly select 100 of them.
# Otherwise, it will take all of the artists and put them into artists_chosen
if len(chosen_genre.artists) > 100:
    i = 0
    while i < 100:
        artist = random.choice(chosen_genre.artists)
        if artist not in artists_chosen:
            artists_chosen.append(artist)
            i += 1
else:
    artists_chosen = chosen_genre.artists

# This series of commands performs the following
# 1: Searches through Spotify's API for the artist
# 2: Selects the most appropriate artist
# 3: Takes their #1 song
# 4: Appends it into the song database
for artist in artists_chosen:
    artists_found = sp.search(q=f"artist:{artist}", type="artist")
    chosen_artist_uri = None
    for potential_artist in artists_found['artists']['items']:
        if user_genre_input in potential_artist['genres']:
            chosen_artist_uri = potential_artist['uri']
            continue
    if chosen_artist_uri is None:
        continue
    try:
        top_tracks = sp.artist_top_tracks(chosen_artist_uri)['tracks']
        track = top_tracks[0]['uri']
        songs.append(track)
    except Exception as e:
        pass

# Creates the playlist on spotify
# It will then put every song in the song database into the playlist
playlist = sp.user_playlist_create(user=os.environ["SPOTIFY_ID"], name=f"{user_genre_input}", public=False, collaborative=False, description=f"{chosen_genre.name} playlist. Created using Spotipy API.")
sp.playlist_add_items(playlist_id=playlist["id"], items=songs)

# Prints the link to the newly created playlist.
print(f"Finished! {playlist['external_urls']['spotify']}")
