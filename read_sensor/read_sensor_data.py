import serial

# Configure the serial port
ser = serial.Serial('/dev/ttyS0', baudrate=9600, timeout=1)  # Use the appropriate port and baud rate for your setup

try:
    while True:
        # Read data from the serial port
        data = ser.readline().decode().strip()

        # Process the data (assuming it's a simple text format)
        if data.startswith("Temperature: ") and data.endswith("°C"):
            temperature = float(data.split("Temperature: ")[1].split("°C")[0])
            print(f"Temperature: {temperature:.2f}°C")
        elif data.startswith("Humidity: ") and data.endswith("%"):
            humidity = float(data.split("Humidity: ")[1].split("%")[0])
            print(f"Humidity: {humidity:.2f}%")

except KeyboardInterrupt:
    print("Exiting the program.")
finally:
    ser.close()  # Close the serial port when the script is interrupted or finished
