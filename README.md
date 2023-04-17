# SpotifyAddSong
This short project is a script for adding currently playing songs on Spotify to either a specified playlist or the user's Liked Songs. It uses the Spotify Web API and Python keyboard library. After starting the script, songs are automatically added through a hotkey combination.  Users can configure the hotkey and choose between adding the song to the playlist or Liked Songs.

# Setup
Within hotkey.py, configure PYTHON_PATH to the location of your python installation.
For hotkey configuration, modifying the key_binding variables to your choice.  
Current default is ctrl+alt+a for adding to playlist and ctrl+alt+b for adding to Liked Songs

Within addsong.py, fill in CLIENT_SECRET, CLIENT_ID, and PLAYLIST_ID according to your spotify developer account credentials and playlist uri.

# How to run
Make sure that both python files are in the same directory and run "python hotkey.py"
