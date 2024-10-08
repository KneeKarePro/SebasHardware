# SebasHardware
This respository will serve as the holder of all of the files Sebastian has worked on for the Hardware Testing, as well as the casing 

This Repository is broken op into two sections, for testing the hardware and software design of my design for the brace. 

This Arduino sketch is written for the ESP32 microcontroller and reads values from a potentiometer connected to the ADC1 channel 0 (GPIO 36). The potentiometer's readings are converted into an angle (0-290 degrees) representing the current position of the knee in our device. The readADC() function returns the calculated angle by scaling the ADC value from a 12-bit resolution (0 to 4095) to the 0-3.3V range. The result is then printed to the serial monitor for real-time tracking.

The system has been integrated with physical components designed in Onshape, where three different models were uploaded to form part of the knee brace contraption. These models contribute to the device's ergonomic and functional design, ensuring precise measurements for rehabilitation purposes.
