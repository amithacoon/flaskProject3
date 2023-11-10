from app import app
from process_manager import init_process_manager, shutdown_process_manager

if __name__ == '__main__':
    init_process_manager(app)
    try:
        app.run(host="0.0.0.0", port=80)
    finally:
        shutdown_process_manager()
