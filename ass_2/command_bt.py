import serial
import time
import threading

# Global variable to indicate if we are waiting for a response
waiting_for_response = False

def read_from_serial(ser):
    global waiting_for_response
    while True:
        if not waiting_for_response:
            # Read a response from the serial port
            response = ser.readline().decode('utf-8').strip()
            if response:
                print(f'Received: {response}')
            time.sleep(0.1)

def manage_serial():
    global waiting_for_response
    try:
        # Open the serial port
        with serial.Serial('/dev/rfcomm0', 9600, timeout=1) as ser:
            # Start a thread to read from serial
            threading.Thread(target=read_from_serial, args=(ser,), daemon=True).start()
           
            while True:
                # Take user input for the command
                custom_command = input("Please enter your custom command: ").strip()
                
                # Set the flag to indicate we are waiting for a response
                waiting_for_response = True
                
                # Append a newline character to the custom command
                custom_command += '\n'
                
                # Convert the custom command to bytes
                custom_command_bytes = bytes(custom_command, 'utf-8')
                
                # Write the custom command to the serial port
                ser.write(custom_command_bytes)
                
                # Wait for a specific response from the Teensy to proceed
                while waiting_for_response:
                    response = ser.readline().decode('utf-8').strip()
                    if response == "FINISHED":  # Replace with the actual response you expect
                        waiting_for_response = False
                        print("Mate has finished the task.")
                    else:
                        waiting_for_response = False
                        print(f'Mate replied: {response}')

    except serial.SerialException as e:
        print(f'Error: {e}')

# Call the function to start the interactive session
manage_serial()
 
