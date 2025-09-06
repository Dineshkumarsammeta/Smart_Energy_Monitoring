import serial
import time
import os
import csv

# Mock serial.Serial for CI
class MockSerial:
    def __init__(self, *args, **kwargs):
        self.is_open = True
    def flushInput(self): pass
    def readline(self):
        time.sleep(0.1)
        return b''
    def close(self): self.is_open = False

serial.Serial = MockSerial

SERIAL_PORT = '/dev/ttyUSB0'
BAUDRATE = 9600
TIMEOUT = 1
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
    ser = serial.Serial(SERIAL_PORT, baudrate=BAUDRATE, timeout=TIMEOUT)
    ser.flushInput()
    print(f"Mocked RS485 port connected. Logging to {log_file_path}")
    # Only run one loop in CI
    for _ in range(1):
        received_bytes = ser.readline()
        if received_bytes:
            decoded_data = received_bytes.decode('utf-8').strip()
            log_data(log_file_path, decoded_data)
    ser.close()
    print("Serial port closed.")

if __name__ == "__main__":
    main()
