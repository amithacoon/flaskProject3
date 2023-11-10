from multiprocessing import Manager, current_process
from concurrent.futures import ProcessPoolExecutor
from processing.consumer import process_audio
from utils.queue_utils import audio_queue, result_queue

number_of_workers = 4
manager = Manager()
audio_queue = manager.Queue()  # Queue for audio files waiting to be processed
result_queue = manager.Queue()  # Queue for storing processed results

def start_worker_processes(number_of_workers):
    # Let's get some workers ready to handle the audio files
    with ProcessPoolExecutor(max_workers=number_of_workers) as executor:
        for _ in range(number_of_workers):
            # Send them off to the worker_process function
            executor.submit(worker_process, audio_queue, result_queue)

def worker_process(audio_queue, result_queue):
    # The grunt work happens here: keep pulling files and processing them
    while True:
        filepath = audio_queue.get()  # Grab the next file
        process_audio(filepath, result_queue)  # And process it

def fetch_results():
    # Grab all the processed data from the queue
    results = []
    while not result_queue.empty():
        results.append(result_queue.get())  # Keep pulling until it's empty
    return results  # And hand them back

def init_process_manager(app):
    global audio_queue
    global result_queue
    # Time to get the process manager up and running
    number_of_workers = app.config.get('NUMBER_OF_WORKERS', 4)  # We'll start with 4 workers by default

    app.logger.info(f"Starting {number_of_workers} worker processes")  # Log how many workers we're firing up
    start_worker_processes(number_of_workers)  # And get them started

# Assuming you've got a global or class-level spot for your executor
executor = None

def init_process_manager(app):
    global executor
    # Set up your queues and app configs here...
    executor = ProcessPoolExecutor(max_workers=number_of_workers)  # This is where we'll manage our workers

def shutdown_process_manager():
    global executor
    if executor:
        app.logger.info("Shutting down worker processes")  # Let's log that we're closing up shop
        executor.shutdown(wait=True)  # And wait for any stragglers to finish up
