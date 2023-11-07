from pydub import AudioSegment


def get_audio_duration(filepath):
    audio = AudioSegment.from_wav(filepath)
    duration_in_milliseconds = len(audio)
    duration_in_seconds = duration_in_milliseconds // 1000
    hours, remainder = divmod(duration_in_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    if hours > 0:
        return f"{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}"
    else:
        return f"{int(minutes):02d}:{int(seconds):02d}"
