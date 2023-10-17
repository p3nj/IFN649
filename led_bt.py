import serial
import time

def toggle_led(state):
    try:
        with serial.Serial('/dev/rfcomm0', 9600, timeout=1) as ser:
            print("Serial port opened")  # Debugging output
            time.sleep(2)  # Adding a delay
            command = "LED_ON" if state else "LED_OFF"
            ser.write(command.encode('utf-8'))
            print(f"Sent command: {command}")  # Debugging output
            response = ser.readline().decode('utf-8').strip()
            print(f"Received response: {response}")  # Debugging output
    except Exception as e:
        print(f"An error occurred: {e}")

# Turn LED on
toggle_led(True)
time.sleep(2)  # Wait for 2 seconds
# Turn LED off
toggle_led(False)

