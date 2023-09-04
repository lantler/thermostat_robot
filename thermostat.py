# /*
#   HS300x - Read Sensors

#   This example reads data from the on-board HS300x sensor of the
#   Nano 33 BLE Sense Rev2 and prints the temperature and humidity sensor
#   values to the Serial Monitor once a second.

#   The circuit:
#   - Arduino Nano 33 BLE Sense Rev2

#   This example code is in the public domain.
# */

include <Servo.h>
include <Arduino_HS300x.h>
Servo myservo;

float old_temp = 0;
float old_hum = 0;

void setup() {

  Serial.begin(9600);
  myservo.attach(9);  // attaches the servo on pin 9 to the servo object
  while (!Serial);

  if (!HS300x.begin()) {
    Serial.println("Failed to initialize humidity temperature sensor!");
    while (1);
  }
}

void loop() {
  // read all the sensor values
  float temperature = HS300x.readTemperature();
  float humidity    = HS300x.readHumidity();
if (abs(old_temp - temperature) >= 0.5 || abs(old_hum - humidity) >= 1 )
  {
  // print each of the sensor values
  Serial.print("Temperature = ");
  Serial.print(temperature);
  Serial.println(" °C");

  Serial.print("Humidity    = ");
  Serial.print(humidity);
  Serial.println(" %");

  // print an empty line
  Serial.println();

  if ((temperature <= 30) && (myservo.read() !=43)) {
    myservo.write(45);
    Serial.print("off");
    Serial.print(myservo.read());
  }

  if ((temperature >= 30) && (myservo.read() !=133)) {
    myservo.write(135);
    Serial.print("on");
    Serial.print(myservo.read());
   }

  // wait 1 second to print again
  delay(60000);

  }
}