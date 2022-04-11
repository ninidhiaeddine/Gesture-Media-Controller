# import libraries:
import serial
import win32api

# define codes:
VK_CODES = {
    "VK_VOLUME_DOWN": 0xAE,
    "VK_VOLUME_UP": 0xAF,
    "VK_MEDIA_NEXT_TRACK": 0xB0,
    "VK_MEDIA_PREV_TRACK": 0xB1,
    "VK_MEDIA_PLAY_PAUSE": 0xB3,
}
PORT_NAME = "COM6"
BAUD = 9600

# initialization:
bluetoothSerial = serial.Serial(PORT_NAME, BAUD)


def listenToRequests():
    """
    Returns to requests emitted by arduino
    """
    print("Awaiting request from", PORT_NAME, "...")
    req = bluetoothSerial.readline()

    # treat request:
    req = str(req)
    req = req[2: -5]

    print("Request received:", req)
    return req


def executeRequest(req):
    if "PLAY_PAUSE" in req:
        playPauseMedia()
    if "NEXT" in req:
        nextTrack()
    if "PREVIOUS" in req:
        previousTrack()
    if "VOLUME_UP" in req:
        volumeUp()
    if "VOLUME_DOWN" in req:
        volumeDown()


def playPauseMedia():
    win32api.keybd_event(VK_CODES["VK_MEDIA_PLAY_PAUSE"], 0)


def nextTrack():
    win32api.keybd_event(VK_CODES["VK_MEDIA_NEXT_TRACK"], 0)


def previousTrack():
    win32api.keybd_event(VK_CODES["VK_MEDIA_PREV_TRACK"], 0)


def volumeUp():
    win32api.keybd_event(VK_CODES["VK_VOLUME_UP"], 0)


def volumeDown():
    win32api.keybd_event(VK_CODES["VK_VOLUME_DOWN"], 0)


# main loop:
while True:
    executeRequest(listenToRequests())