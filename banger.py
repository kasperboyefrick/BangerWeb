from flask import Flask, render_template, request
import spotipy
import json
from spotipy.oauth2 import SpotifyClientCredentials

app = Flask(__name__)

with open("config.json", "r") as f:
    config = json.load(f)
with open("connection.json", "r" as f:
    connection = json.load(f)

# Set up Spotify API credentials
client_credentials_manager = SpotifyClientCredentials(client_id=connection["client_id"], client_secret=connection["client_secret"])
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Define the route for the playlist page
@app.route('/')
def playlist():
    # Get the playlist from the Spotify API
    playlist = sp.playlist(connection["playlist_id_bangers"])

    # Extract the track information from the playlist
    tracks = []
    for item in playlist['tracks']['items']:
        track = item['track']
        tracks.append({
            'name': track['name'],
            'artist': track['artists'][0]['name'],
            'album': track['album']['name']
        })

    # Render the template with the track information
    return render_template("playlist.html", tracks=tracks)

if __name__ == '__main__':
    app.run(debug=True)
