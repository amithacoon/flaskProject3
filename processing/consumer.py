import wave
import logging
from utils.queue_utils import audio_queue, result_queue

logging.basicConfig(level=logging.INFO)

def process_audio(audio_queue):
    while True:
        filepath = audio_queue.get()
        try:
            with wave.open(filepath, 'rb') as wave_file:
                frames = wave_file.getnframes()
                rate = wave_file.getframerate()
                duration = frames / float(rate)
                result_queue.put((filepath, duration))
                logging.info(f"Processed {filepath}: Duration {duration} seconds")
        except Exception as e:
            logging.error(f"Error processing {filepath}: {e}")
