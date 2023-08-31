import paho.mqtt.publish as publish

publish.single("ifn649", "LED_ON", hostname="3.25.58.119")
print("Done")
