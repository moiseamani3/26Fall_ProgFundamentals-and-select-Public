# sensor_app_template.py
# This program runs ON THE PC using regular Python 3.
#
# It requests sensor readings from the board only after the user
# selects T, H, or 0. Each reading is displayed and saved in SQLite.
#
# Setup: python -m pip install pyserial
# IMPORTANT: Close Thonny before running this program.

import sqlite3
import time
import serial


# Use the same port that worked in your successful PING test.
PORT = "/dev/cu.usbmodem14101"
BAUD = 115200


def ask_board(ser, command):
    """Send a one-letter command and return the board's numeric reply."""

    # Discard old data before sending a new request.
    ser.reset_input_buffer()

    # Send the command followed by a newline.
    ser.write((command + "\n").encode())

    # Wait for a DATA response, ignoring unrelated messages.
    while True:
        line = ser.readline().decode(errors="ignore").strip()

        # An empty response means the serial read timed out.
        if line == "":
            raise TimeoutError("No reply from board")

        # Examples: DATA,TEMP,21.50 or DATA,HUM,61.50
        # The numeric reading is the third comma-separated field.
        if line.startswith("DATA,"):
            return float(line.split(",")[2])


class DatabaseManager:
    """Manage database creation, saving readings, and viewing history."""

    def __init__(self, db_name="sensor_data.db", reset_database=False):
        # Connect to the database, creating it if necessary.
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()

        # Delete old tables only when a reset is explicitly requested.
        # WARNING: Resetting permanently deletes their saved readings.
        if reset_database:
            self.cur.execute("DROP TABLE IF EXISTS SensorData")
            self.cur.execute("DROP TABLE IF EXISTS Sensor_data")

        # Create the assignment table if it does not already exist.
        self.create_table()

    def create_table(self):
        """Create the sensor table without deleting existing history."""

        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS Sensor_data (
                ID INTEGER PRIMARY KEY,
                timestamp TEXT NOT NULL,
                sensor_type TEXT NOT NULL,
                sensor_reading_value REAL NOT NULL
            )
        """)

        # Save the table creation or an explicitly requested reset.
        self.conn.commit()

    def insert_new_sensor_reading(self, sensor_type, reading_value):
        """Save one sensor reading with the PC's local date and time."""

        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

        # Use placeholders to pass values into the SQL statement.
        # SQLite automatically assigns the new record's ID.
        self.cur.execute("""
            INSERT INTO Sensor_data (
                timestamp,
                sensor_type,
                sensor_reading_value
            )
            VALUES (?, ?, ?)
        """, (timestamp, sensor_type, reading_value))

        # Save the new reading to the database.
        self.conn.commit()

    def display_historical_records(self):
        """Retrieve and display every saved reading, oldest first."""

        records = self.cur.execute("""
            SELECT ID, timestamp, sensor_type, sensor_reading_value
            FROM Sensor_data
            ORDER BY ID
        """).fetchall()

        # Provide a message if no readings have been saved.
        if not records:
            print("No sensor history logged.")
            return

        # Print headings followed by each saved record.
        print("\nID | Timestamp | Sensor Type | Reading")
        print("-" * 65)

        for record_id, timestamp, sensor_type, reading in records:
            # Display the appropriate unit for each sensor.
            if sensor_type == "Temperature":
                unit = "C"
            elif sensor_type == "Humidity":
                unit = "%"
            else:
                unit = ""

            print(
                f"{record_id} | {timestamp} | "
                f"{sensor_type} | {reading:.1f} {unit}"
            )

    def close(self):
        """Close the database connection."""
        self.conn.close()


def log_temperature(ser, db):
    """Request, display, and save the temperature."""

    # Request temperature inside this function only when called.
    temperature = ask_board(ser, "T")

    # Display and save the returned reading.
    print(f"Temperature: {temperature:.1f} C")
    db.insert_new_sensor_reading("Temperature", temperature)


def log_humidity(ser, db):
    """Request, display, and save the humidity."""

    # Request humidity inside this function only when called.
    humidity = ask_board(ser, "H")

    # Display and save the returned reading.
    print(f"Humidity: {humidity:.1f} %")
    db.insert_new_sensor_reading("Humidity", humidity)


def main():
    # Display the required menu before requesting any sensor readings.
    print("Please choose from the following options:")
    print("  T - Temperature")
    print("  H - Humidity")
    print("  0 - Both")
    print("  V - View Log History")

    # Preserve saved history by leaving reset_database as False.
    db = DatabaseManager()

    # Allow cleanup even if the serial connection cannot be opened.
    ser = None

    try:
        # Open the serial port and allow the board time to restart.
        # Opening the connection does not request a sensor reading.
        ser = serial.Serial(PORT, BAUD, timeout=3)
        time.sleep(2)
        ser.reset_input_buffer()

        # Keep asking until one valid selection completes successfully.
        while True:
            choice = input("\nEnter your choice: ").strip().upper()

            # Invalid input must not trigger a sensor request.
            if choice not in ("T", "H", "0", "V"):
                print("Invalid selection. Please choose T, H, 0, or V.")
                continue

            try:
                if choice == "T":
                    log_temperature(ser, db)

                elif choice == "H":
                    log_humidity(ser, db)

                elif choice == "0":
                    # Each function requests and saves its own reading.
                    log_temperature(ser, db)
                    log_humidity(ser, db)

                elif choice == "V":
                    # Viewing history does not request sensor data.
                    db.display_historical_records()

                # End after one successful selection.
                # No additional menu option is required.
                break

            except (TimeoutError, ValueError, IndexError) as error:
                # Allow another attempt if a reply is missing or malformed.
                print(f"Could not read sensor: {error}")

    finally:
        # Close connections after the loop ends or an error propagates.
        # Keep ser.close() outside the input loop.
        if ser is not None:
            ser.close()

        db.close()


# Start the program only when this script is executed directly.
if __name__ == "__main__":
    main()