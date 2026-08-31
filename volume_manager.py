from pycaw.pycaw import AudioUtilities

def get_volume():
    return AudioUtilities.GetSpeakers().EndpointVolume

def volume_up():
    volume = get_volume()
    current = volume.GetMasterVolumeLevelScalar()
    volume.SetMasterVolumeLevelScalar(min(current + 0.1, 1.0), None)
    return "Volume increased."

def volume_down():
    volume = get_volume()
    current = volume.GetMasterVolumeLevelScalar()
    volume.SetMasterVolumeLevelScalar(max(current - 0.1, 0.0), None)
    return "Volume decreased."

def mute_volume():
    volume = get_volume()
    volume.SetMute(1, None)
    return "Volume muted."

def unmute_volume():
    volume = get_volume()
    volume.SetMute(0, None)
    return "Volume unmuted."