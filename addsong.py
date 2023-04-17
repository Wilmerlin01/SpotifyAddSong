import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
import sys

REDIRECT_URI = "http://localhost:8000/callback"
CLIENT_SECRET = "YOUR_CLIENT_SECRET"
CLIENT_ID = "YOUR_CLIENT_ID"
#to get playlist id, go to the playlist and navigate to the share
#hover over "copy spotify link"
#if on windows, hold alt and copy spotify uri will pop up
#on mac, hold down the option or control key
PLAYLIST_ID = "YOUR_PLAYLIST_ID"

scope = "user-library-read user-library-modify user-read-playback-state playlist-modify-public playlist-modify-private"
cache_path = os.path.join(os.getcwd(), ".spotifycache")

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI, scope=scope))

def add_to_liked_songs(track_info):
    #Add the track to your Liked Songs
    track_uri = track_info['item']['uri']
    sp.current_user_saved_tracks_add(tracks=[track_uri])

    #Get track name
    track_name = track_info['item']['name']
    print(f"Playlist: Liked Songs | Song: {track_name}")

def add_to_playlist(track_info):
    #Add track to the playlist
    track_uri = track_info['item']['uri']
    sp.playlist_add_items(playlist_id=PLAYLIST_ID, items=[track_uri])

    #Get playlist name
    playlist = sp.playlist(PLAYLIST_ID)
    playlist_name = playlist['name']

    #Get track name
    track_name = track_info['item']['name']
    print(f"Playlist: {playlist_name} | Song: {track_name}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python addsong.py <function>")
        exit()

    track_info = sp.current_user_playing_track()
    if track_info is None:
        print("No track is currently playing.")
        exit()

    function_name = sys.argv[1]
    if function_name == "liked":
        add_to_liked_songs(track_info)
    elif function_name == "playlist":
        add_to_playlist(track_info)
    else:
        print("Invalid function name.")