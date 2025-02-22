const int pumpPin = 8;  // Digital pin connected to water pump relay
const int moistureSensorPin = A0;  // Analog pin connected to moisture sensor
bool autoModeEnabled = false;

void setup() {
  Serial.begin(9600);
  pinMode(pumpPin, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();

    if (command == '1') {
      // Turn on the pump
      digitalWrite(pumpPin, HIGH);
      autoModeEnabled = false;
    } else if (command == '0') {
      // Turn off the pump
      digitalWrite(pumpPin, LOW);
      autoModeEnabled = false;
    } else if (command == '2') {
      // Enable auto mode
      autoModeEnabled = true;
    }
  }
if (autoModeEnabled) {
    int moistureLevel = readMoisture();

    if (moistureLevel < 500) {
      digitalWrite(pumpPin, HIGH);
    } else {
      digitalWrite(pumpPin, LOW);
    }
    delay(1000); // Check moisture level every 1 second
  }
}

int readMoisture() {
  int moistureLevel = analogRead(moistureSensorPin);
  return moistureLevel;
}

