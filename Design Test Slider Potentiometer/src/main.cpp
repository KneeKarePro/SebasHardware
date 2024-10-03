#include <Arduino.h>

// ESP32 ADC1 channel 0 is GPIO 36 for Potentiometer
const int adc_pin = 36;

// Function to read the ADC value from the potentiometer
uint16_t readADC() {
  uint16_t adc_value = analogRead(adc_pin);
  float degree = (adc_value / 4095.0) * 290.0;
  return degree;
}

void setup() {
  
  Serial.begin(115200);  // Initialize serial communication
  analogReadResolution(12);       // 12 bits of resolution for ADC readings
  analogSetAttenuation(ADC_11db); // 0-3.3V range for ADC readings
}

void loop() {
  uint16_t sensor_value = readADC();  // Read potentiometer value
  Serial.print("Current Angle of Knee: ");
  Serial.println(sensor_value);       // Print the value to the terminal
  
  delay(50);  // Wait for half a second before the next reading
}
