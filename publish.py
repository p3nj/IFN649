import paho.mqtt.publish as publish

 

publish.single("bengy","LED_OFF",hostname="3.25.58.119") #Your IP Address
print("Done, LED is OFF")
