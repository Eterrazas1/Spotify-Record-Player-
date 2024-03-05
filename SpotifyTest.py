# Program to test Spotify access tokens and data
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from time import sleep

# DeviceID needed to connect to Spotify
deviceId = "(Insert Personal DeviceID)"

# ClientID and Secret used to access personal Spotify account/data
clientId = "(Insert Personal Spotify ClientID)"
clientSecret = "(Insert Personal Spotify Client Secret)"

# Assigning information sp
sp = spotipy.Spotify(auth_manager = SpotifyOAuth(client_id = clientId,
                                                     client_secret = clientSecret,
                                                     redirect_uri = "http://localhost:8080",
                                                     scope = "user-read-playback-state,user-modify-playback-state"))

# Connecting Spotify to host device 
sp.transfer_playback(device_id = deviceId, force_play = False)

# Test track to see if all information is correct
# If song begins to play, all information is correct. Else, recheck deviceID, clientID, or clientSecret
sp.start_playback(device_id = deviceId, uris = ['spotify:track:4qYHnP5AmKzXbJhciPV8si'])