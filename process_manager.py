from multiprocessing import Manager, current_process
from concurrent.futures import ProcessPoolExecutor

from processing.consumer import process_audio
from utils.queue_utils import audio_queue, result_queue
manager = Manager()
audio_queue = manager.Queue()
result_queue = manager.Queue()

def start_worker_processes(number_of_workers):
    # Use a pool of workers to process audio files
    with ProcessPoolExecutor(max_workers=number_of_workers) as executor:
        for _ in range(number_of_workers):
            executor.submit(worker_process, audio_queue, result_queue)


def worker_process(audio_queue, result_queue):
    while True:
        filepath = audio_queue.get()
        process_audio(filepath, result_queue)


def fetch_results():
    # Fetch results and clear the queue
    results = []
    while not result_queue.empty():
        results.append(result_queue.get())
    return results


def init_process_manager(app):
    global audio_queue
    global result_queue
    # Initialize the process manager
    number_of_workers = app.config.get('NUMBER_OF_WORKERS', 4)  # Default to 4 workers

    app.logger.info(f"Starting {number_of_workers} worker processes")
    start_worker_processes(number_of_workers)


# Assuming you have a global or class-level reference to your executor
executor = None

def init_process_manager(app):
    global executor
    # ... initialize your queues and app configuration ...
    executor = ProcessPoolExecutor(max_workers=number_of_workers)

def shutdown_process_manager():
    global executor
    if executor:
        app.logger.info("Shutting down worker processes")
        executor.shutdown(wait=True)  # Wait for all running tasks to complete
