from multiprocessing import Process
from processing.consumer import process_audio
from utils.queue_utils import audio_queue

# Keep track of processes
processes = []

def enqueue_audio(filepath):
    global audio_queue
    global processes
    audio_queue.put(filepath)
    # Start a new process for each audio file
    process = Process(target=process_audio, args=(audio_queue,))
    process.start()
    # Instead of joining the process, add it to the list of processes
    processes.append(process)
    # Optionally, you can clean up finished processes here
    processes = [p for p in processes if p.is_alive()]
