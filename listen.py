import paho.mqtt.client as mqtt
import serial

 
#Code from last week's bt.py
#relay the command from Pi to Teensy
#Connect Pi with Teensy over BT first
print("Setting up bluetooth serial conncetion on /dev/rfcomm0 on port 9600")
ser = serial.Serial("/dev/rfcomm0", 59600)

def on_connect(client, userdata, flags, rc): # func for makinf connection
    print(f"Connected to MQTT Server {ADD} at port {PORT}")
    print(f"Connection returned result: " + str(rc) )
    topic = "bengy"
    client.subscribe(topic)
    print(f"Subscribe to topic: {topic}")


 

def on_message(client, userdata, msg): #Func for Sending msg
    #print("recieved message!")
#    print(msg.topic+" "+str(msg.payload))
#    print(str(msg.payload))
    #print("relying to teensy over BT...")

    print(f"Writing payload: {msg.payload} received from AWS Broker")
    ser.write(msg.payload)

ADD = "3.25.58.119"
PORT = 1883

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
 

client.connect(ADD,PORT, 60)


print("Initial setup complete, running the listener forever...")
client.loop_forever()
