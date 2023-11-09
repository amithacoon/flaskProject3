from multiprocessing import Process
from processing.consumer import process_audio
from utils.queue_utils import audio_queue

# Let's keep a list of all our running tasks
processes = []

def enqueue_audio(filepath):
    global audio_queue
    global processes
    audio_queue.put(filepath)
    # Kick off a new task for each sound file
    process = Process(target=process_audio, args=(audio_queue,))
    process.start()
    # Instead of waiting for the task to finish, just add it to our list
    processes.append(process)
    # If you want, you can get rid of tasks that are done
    processes = [p for p in processes if p.is_alive()]
