"""
Mock test for Smart Energy Monitoring RS485 logger.
This test replaces the serial.Serial class with a mock to simulate data input.
"""

import os
import csv
import time
import pytest

# --- Mock Serial Class ---
class MockSerial:
    def __init__(self, *args, **kwargs):
        self.is_open = True
        self._counter = 0

    def flushInput(self):
        pass

    def readline(self):
        self._counter += 1
        if self._counter > 3:  # stop after a few lines
            return b""
        # Simulate RS485 bytes
        return f"Power:{100 + self._counter},HVAC:{50 + self._counter}\n".encode("utf-8")

    def close(self):
        self.is_open = False


# --- Logger Functions (mirrors main script) ---
LOG_DIRECTORY = "rs485_logs"
FILE_NAME_PREFIX = "rs485_data"

def setup_logging():
    os.makedirs(LOG_DIRECTORY, exist_ok=True)
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    return os.path.join(LOG_DIRECTORY, f"{FILE_NAME_PREFIX}_{timestamp}.csv")

def log_data(file_path, data):
    with open(file_path, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([time.time(), data])


def test_mock_serial_logging(tmp_path, monkeypatch):
    """Test logging with mocked serial input."""
    monkeypatch.setattr("serial.Serial", MockSerial)  # patch serial.Serial

    log_file = setup_logging()

    ser = MockSerial()
    ser.flushInput()

    for _ in range(3):
        received_bytes = ser.readline()
        if received_bytes:
            decoded = received_bytes.decode("utf-8").strip()
            log_data(log_file, decoded)

    ser.close()

    # Verify file created
    assert os.path.exists(log_file)
    with open(log_file) as f:
        lines = f.readlines()
    assert len(lines) == 3  # 3 rows expected
