import serial
import time
import csv
import os

# Configuration of port
SERIAL_PORT = '/dev/ttyUSB0'  # Replace with your RS485 adapter's port
BAUDRATE = 9600
TIMEOUT = 1  # Seconds to wait for data

LOG_DIRECTORY = 'rs485_logs'  # Folder to store log files
FILE_NAME_PREFIX = 'rs485_data'

# Script
def setup_logging():
    """Creates the log directory if it doesn't exist and returns the log file path."""
    os.makedirs(LOG_DIRECTORY, exist_ok=True)  #
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    file_path = os.path.join(LOG_DIRECTORY, f"{FILE_NAME_PREFIX}_{timestamp}.csv")
    return file_path

def log_data(file_path, data):
    """Appends data to the specified CSV log file."""
    with open(file_path, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([time.time(), data]) #

def main():
    log_file_path = setup_logging()

    try:
        ser = serial.Serial(
            port=SERIAL_PORT,
            baudrate=BAUDRATE,
            timeout=TIMEOUT
        )
        ser.flushInput()  # Clear any buffered data
        print(f"Connected to RS485 port {SERIAL_PORT} at {BAUDRATE} baudrate.")
        print(f"Logging data to: {log_file_path}")

        while True:
            try:
                # Read data from the serial port
                received_bytes = ser.readline()
                if received_bytes:
                    decoded_data = received_bytes.decode('utf-8').strip() #
                    print(f"Received: {decoded_data}")
                    log_data(log_file_path, decoded_data)

            except serial.SerialException as e:
                print(f"Serial communication error: {e}")
                break # Exit loop on error

            except Exception as e:
                print(f"Error processing received data: {e}")

    except serial.SerialException as e:
        print(f"Could not open serial port {SERIAL_PORT}: {e}")

    finally:
        if 'ser' in locals() and ser.is_open:
            ser.close()
            print("Serial port closed.")

if __name__ == "__main__":
    main()
