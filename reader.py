# Program to read RFID Tags
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
    print("Waiting for card scan...")
    id = reader.read()[0]
    # Printed out RFID Tag value to later assign with Spotify song/album/playlist in main
    print("Card ID: ", id)
    
finally:
    GPIO.cleanup()