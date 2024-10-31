#include <Arduino.h>

// ESP32 ADC1 channel 0 is GPIO 36 for Potentiometer
const int adc_pin = 36;

uint16_t baseline = 0;  // Variable to store the initial calibration value

// Function to read the ADC value from the potentiometer
uint16_t readADC() {
  uint16_t adc_value = analogRead(adc_pin);
  float degree = ((adc_value - baseline) / 4095.0) * 290.0 / 11.0 * 9.0;  // Adjust with baseline
  if (degree < 0) degree = 0;  // Ensure we don't get negative values
  return degree;
}

void setup() {
  Serial.begin(115200);  // Initialize serial communication
  analogReadResolution(12);       // 12 bits of resolution for ADC readings
  analogSetAttenuation(ADC_11db); // 0-3.3V range for ADC readings

  // Calibration: Read the initial potentiometer value
  baseline = analogRead(adc_pin);  // Set the baseline to the current position
  Serial.print("Baseline set to: ");
  Serial.println(baseline);
}

void loop() {
  uint16_t sensor_value = readADC();  // Read potentiometer value
  Serial.print("Current Angle of Knee: ");
  Serial.println(sensor_value);       // Print the value to the terminal
  
  delay(50);  // Wait for half a second before the next reading
}
