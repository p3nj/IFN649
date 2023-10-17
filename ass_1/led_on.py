import paho.mqtt.publish as publish

publish.single("bengy", "LED_ON", hostname="3.25.58.119")
print("Done")
