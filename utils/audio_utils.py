from pydub import AudioSegment
from pydub.exceptions import CouldntDecodeError

def get_audio_duration(filepath):
    try:
        # Try to read the file
        audio = AudioSegment.from_wav(filepath)
        duration_in_milliseconds = len(audio)
        duration_in_seconds = duration_in_milliseconds // 1000
        hours, remainder = divmod(duration_in_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        # Format the duration based on the length
        if hours > 0:
            return f"{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}"
        else:
            return f"{int(minutes):02d}:{int(seconds):02d}"
    except CouldntDecodeError:
        # If the file isn't a valid wav file, return "not WAV"
        return "This file is a WAV file but not WAV format"
    except Exception:
        return None
