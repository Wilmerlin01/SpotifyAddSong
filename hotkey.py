import keyboard
import subprocess

PYTHON_PATH= "C:/Python311/python.exe"
KEY_BINDING_PLAYLIST = "ctrl+alt+a"
KEY_BINDING_LIKED_SONGS = "ctrl+alt+b"

def add_to_playlist():
    subprocess.run([PYTHON_PATH, "addsong.py", "playlist"])

def add_to_liked_songs():
    subprocess.run([PYTHON_PATH, "addsong.py", "liked"])

keyboard.add_hotkey(KEY_BINDING_PLAYLIST, add_to_playlist)
keyboard.add_hotkey(KEY_BINDING_LIKED_SONGS, add_to_liked_songs)
keyboard.wait()
