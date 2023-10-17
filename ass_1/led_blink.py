import paho.mqtt.publish as publish
import time

ADDR = "3.25.58.119"
TOPIC = "bengy"


def blink(count):
    print(f"Sending {count} blinks to Teensy")
    for i in range(count):
        time.sleep(0.5)
        print("Sending LED_ON to AWS MQTT")
        publish.single(TOPIC, "LED_ON", hostname=ADDR)
        time.sleep(1)
        print("Sending LED_OFF to AWS MQTT")
        publish.single(TOPIC, "LED_OFF", hostname=ADDR)
        time.sleep(0.5)
    print("Done")


def blink_infinite():
    while True:
        time.sleep(0.5)
        print("sending LED_ON to AWS MQTT")
        publish.single(TOPIC, "LED_ON", hostname=ADDR)
        time.sleep(1)
        print("Sending LED_OFF to AWS MQTT")
        publish.single(TOPIC, "LED_OFF", hostname=ADDR)
        time.sleep(0.5)
    
        
# blink(5)
blink_infinite()
