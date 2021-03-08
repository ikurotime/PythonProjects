import requests
import spotipy
from bs4 import  BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth

TOP100_ENDPOINT = "https://www.billboard.com/charts/hot-100/"
CLIENT_ID = '613994df86694aae8b095860b2f7c3d6'
CLIENT_SECRET = '5dde162a4a7a43eeb7fc84535c250854'
REDIRECT_URI = "http://example.com"
SCOPE = "playlist-modify-private"
MY_ID = 'z78fjpl9pxovyz24s2ucxr2d5'

date_selection = input("Would you like to search by date or by year?(date/year)" ).lower()
if date_selection == "date":
    selected_year = input("Which year would you like to travel to? (YYYY-MM-DD) ")
    print("Finding songs, please wait...")
    website = TOP100_ENDPOINT + selected_year
    response = requests.get(website)
    website_html = response.text
    soup = BeautifulSoup(website_html,"html.parser")
    elements = soup.find_all(name = "span",class_="chart-element__information__song text--truncate color--primary")
    titles= []
    for title_tag in elements:
        text = title_tag.getText()
        titles.append(text)

    print(f"Found {len(titles)} songs.")
    spotify = spotipy.Spotify(auth_manager = SpotifyOAuth(client_id = CLIENT_ID,
                        client_secret = CLIENT_SECRET,
                        redirect_uri = REDIRECT_URI,
                        scope = SCOPE,
                        cache_path="token.txt"))
    titles_uris = []
    year = selected_year.split("-")[0]
    print("Adding songs to a new playlist...")
    for item in titles:
        search = spotify.search(q=f'track:{item} year:{year}',type = 'track')
        try:
            uri = search['tracks']['items'][0]['uri']
            titles_uris.append(uri)
        except IndexError:
            print(f"{item} doesn't exist in Spotify. Skipped.")
    new_playlist = spotify.user_playlist_create(user = MY_ID, name = f"{selected_year} Billboard 100", public = False, )
    spotify.playlist_add_items(playlist_id = new_playlist['id'] ,items = titles_uris)
    print(f'{len(titles_uris)} songs have been added to the playlist "{selected_year} Billboard 100"')
else:
    print("lol")