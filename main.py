import machine
import utime

# Initialize ADC on GP28 (ADC2)
sensor = machine.ADC(28)

# Baseline threshold (values above this trigger an alert)
LEAK_THRESHOLD = 1000

while True:
    # Read raw 16-bit unsigned analog integer (0 - 65535)
    value = sensor.read_u16()
    
    if value > LEAK_THRESHOLD:
        print(f"🚨 LEAK DETECTED! Reading: {value}")
    else:
        print(f"✅ Normal / Dry. Reading: {value}")
        
    utime.sleep(0.2)  # Delay to avoid flooding the console
