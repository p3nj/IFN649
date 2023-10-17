#define LED_PIN 11
#define BUZZER_PIN 9
#define FSR_PIN 20

void setup() {
  // Setup serial for monitor and Setup Serial1 for Bluetooth
  Serial.begin(9600);
  Serial1.begin(9600);
  
  pinMode(LED_PIN, OUTPUT);
  pinMode(BUZZER_PIN, OUTPUT);
}

void loop() {
  sendFSRReading();
  handleBluetoothCommands();
}

void sendFSRReading() {
  int fsrReading = analogRead(FSR_PIN);
  Serial1.print("FSR Reading: "); 
  Serial1.println(fsrReading);
  Serial.print("FSR Reading: "); 
  Serial.println(fsrReading);
  delay(1000);
}

void handleBluetoothCommands() {
  if (Serial1.available() > 0) {
    String command = Serial1.readString();

    if (command == "LED_ON\n") {
      digitalWrite(LED_PIN, HIGH);
      Serial1.println("LED ON");
      Serial1.println("FINISHED");
    } 
    else if (command == "LED_OFF\n") {
      digitalWrite(LED_PIN, LOW);
      Serial1.println("LED OFF");
      Serial1.println("FINISHED");
    } 
    else if (command.startsWith("BUZZ_NOTIFY\n")) {
      buzzNotify();
      Serial1.println("FINISHED");
    } 
    else if (command.startsWith("BUZZ_ON")) {
      buzzOn(command);
      Serial1.println("FINISHED");
    } 
    else if (command == "BUZZ_OFF\n") {
      noTone(BUZZER_PIN);
      Serial1.println("FINISHED");
    }
    else {
      Serial1.println("COMMAND_NOT_FOUND");
    }
  }
}


void buzzNotify() {
  for (int i = 0; i < 3; i++) {
    tone(BUZZER_PIN, 2000, 200);  // Example frequency and duration
    delay(200);  // Wait 1 second between buzzes
  }
}

void buzzOn(String command) {
  int commaIndex = command.indexOf(',');
  if (commaIndex != -1) {
    int freq = command.substring(7, commaIndex).toInt();
    int duration = command.substring(commaIndex + 1).toInt();
    tone(BUZZER_PIN, freq, duration);
  }
}

