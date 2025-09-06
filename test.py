# test_rs485.py
import time
import os
import csv

LOG_DIRECTORY = 'rs485_logs'
FILE_NAME_PREFIX = 'rs485_data'

def setup_logging():
    os.makedirs(LOG_DIRECTORY, exist_ok=True)
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    return os.path.join(LOG_DIRECTORY, f"{FILE_NAME_PREFIX}_{timestamp}.csv")

def log_data(file_path, data):
    with open(file_path, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([time.time(), data])

def main():
    log_file_path = setup_logging()
    print(f"Logging to {log_file_path}")

    # Simulate receiving 5 data points
    for i in range(5):
        data = f"mock_data_{i}"
        print(f"Received: {data}")
        log_data(log_file_path, data)
        time.sleep(0.1)

    print("Finished logging.")

if __name__ == "__main__":
    main()
