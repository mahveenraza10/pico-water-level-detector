# pico-water-level-detector
# Raspberry Pi Pico Water Level & Leak Detection System

A MicroPython-based embedded system that reads analog signals from a resistive water level sensor using the Raspberry Pi Pico. The system measures water depth in real time and detects liquid leaks based on dynamic baseline thresholding.

## 📌 Overview & Applications
The sensor utilizes a series of exposed, parallel copper traces. As water bridges the conductive traces, the resistance decreases, generating a higher analog voltage output corresponding to submersion depth.

- **Rainfall Detection:** Measure precipitative accumulation.
- **Water Level Monitoring:** Track tank/reservoir fluid levels.
- **Leakage Detection:** Trigger immediate alerts when dry baselines are breached.

---

## 🛠 Hardware & Wiring

| Component | Connection Pin | Functional Role |
| :--- | :--- | :--- |
| **Raspberry Pi Pico** | GP28 (ADC Pin) | Analog Signal Input |
| **Water Sensor Signal (S)** | GP28 | Reads 16-bit voltage levels |
| **Water Sensor Positive (+)**| 3.3V Rail | Powers the sensor traces |
| **Water Sensor Ground (-)**  | GND | Completes circuit / 0V reference |


## 💻 Firmware Implementation

### Base ADC Reader (`firmware/main.py`)
Reads raw 16-bit unsigned integers (`0` to `65535`) from channel ADC28 at 200ms intervals.

```python
import machine
import utime

# Initialize ADC on GP28
sensor = machine.ADC(28)

while True:
    # Read the 16-bit analog value
    value = sensor.read_u16()
    print("Water level reading:", value)
    utime.sleep(0.2)  # Delay to prevent console flooding
