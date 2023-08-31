import paho.mqtt.client as mqtt
import serial

def on_connect(client, userdata, flags, rc): # func for makinf connection
	print(f"Connected to MQTT Server {ADDR} at port {PORT}")
	print(f"Connection returned result: " + str(rc) )
	topic = "ifn649"
	client.subscribe(topic)
	print(f"Subscribe to topic: {topic}")
	

def on_message(client, userdata, msg): #Func for Sending msg
	print("recieved message!")
	print(msg.topic+" "+str(msg.payload))
	print("relying to teensy over BT...")
	
	#Code from last week's bt.py
	#relay the command from Pi to Teensy
	#Connect Pi with Teensy over BT first
	ser = serial.Serial("/dev/rfcomm0", 9600)
	ser.write(msg.payload)
	

ADDR = "3.25.58.119"
PORT = 1883
	
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(ADDR, PORT, 60) 

client.loop_forever()
