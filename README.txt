
## Description
The Audio File Processor is a multi-process Flask web application that allows users to upload WAV audio files and view their durations. The application is designed to demonstrate efficient multiprocessing and inter-process communication using queues.

## How It Works

### Web Interface
- Users are presented with a simple and intuitive interface to upload WAV audio files.
- Upon uploading a file, it is added to a processing queue for duration calculation.

### Producer Process
- Once a file is uploaded, the producer process reads the file and places it into a shared queue for processing.

### Consumer Process
- The consumer process retrieves audio files from the shared queue.
- It performs a basic operation: calculating the audio duration.
- The duration is then placed into a separate results queue.

### Display Results
- The web interface dynamically updates to display the results.
- A table below the upload form shows the filenames and their corresponding durations.

## Functionality Overview
- Upload WAV audio files through the web interface.
- View the duration of each audio file in a table below the upload form.
- The application utilizes multiprocessing for efficient handling of multiple files.
