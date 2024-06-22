from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

Volume = int(input("Enter the volume level 0 to 1 : "))
def set_volume(level):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    
    # Set the volume level (0.0 to 1.0)
    volume.SetMasterVolumeLevelScalar(level, None)

# Example usage: set volume 0 to 1.0
Volume = set_volume(int(Volume)) 


