import spotipy
from array import array
import RPi.GPIO as GPIO
from spotipy.oauth2 import SpotifyOAuth
from time import sleep
from mfrc522 import SimpleMFRC522
sleep(18)

# Function to play selected song/playlist/album user scans
def songSelection(cardId):
    playSelectedPlaylist = cardToPlaylist.get(cardId)
    if (playSelectedPlaylist):
        sp.start_playback(device_id = deviceId, context_uri = playSelectedPlaylist)
        sp.shuffle(True, device_id = deviceId)
      
# Main
deviceId = "(Insert personal device ID)"
clientId = "(Insert personal client ID)"
clientSecret = "(Insert personal client Secret"

# Array holding any number RFID Tag values
# Values are put into an array incase users want to input more tags (more songs/playlists)
cardValueList = [123456789123] # Sample of RFID Tag value 

# Dictionary to assign specific Tag values to specific songs/albums/playlists from Spotify
cardToPlaylist = {
    123456789123: 'spotify:playlist:rand0mT3xt10IncludeY0ur0wn', # Sample of Spotify Playlist
}

# Program continuously runs for users to switch between different assigned songs/playlists/albums
while True:
    try:
        reader = SimpleMFRC522()
        sp = spotipy.Spotify(auth_manager = SpotifyOAuth(client_id = clientId,
                                                         client_secret = clientSecret,
                                                         redirect_uri = "http://localhost:8080",
                                                         scope = "user-read-playback-state,user-modify-playback-state",
                                                         ))
        # RFID Scanner continuously runs for users to switch between songs/playlists/albums                                         
        while True:
            print("Waiting for card to read...")
            id = reader.read()[0]
            print("Card vaue is: ", id)
            sp.transfer_playback(device_id = deviceId, force_play = False)
            sleep(0.1)
        
            # Searches for match between scanned RFID tag and stored tag value
            for i in cardValueList:
                # If data matches, call songSelection functions with scanned RFID tag value
                if (id == i):
                    songSelection(id)
            
	       # RFID Tag assigned with pausing current track
            if (id == 386457999370):
                sp.pause_playback(device_id = deviceId)

	       # RFID Tag assigned with playing current track
            elif (id == 451004536967):
                sp.start_playback(device_id = deviceId)

	       # RFID Tag assigned with skipping current track
            elif (id == 792949101126):
                sp.next_track(device_id = deviceId)
                    
    except Exception as e:
        print(e)
        pass
            
    finally:
        GPIO.cleanup()
        print("Cleaning up...")