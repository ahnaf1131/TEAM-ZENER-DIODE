import RPi.GPIO as GPIO
import time

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)

# Define GPIO pins for front, right, and left sensors
sensors = {
    "front": {"trigger": 5, "echo": 6},
    "right": {"trigger": 27, "echo": 17},
    "left": {"trigger": 23, "echo": 24}
}

# Set up GPIO pins for each sensor
for sensor in sensors.values():
    GPIO.setup(sensor["trigger"], GPIO.OUT)
    GPIO.setup(sensor["echo"], GPIO.IN)


def measure_distance(trigger, echo, timeout=0.05):
    # Ensure trigger is low
    GPIO.output(trigger, False)
    time.sleep(0.00005)  # Reduced sleep time for quicker trigger reset

    # Send a 10µs pulse to trigger
    GPIO.output(trigger, True)
    time.sleep(0.00001)  # 10µs pulse
    GPIO.output(trigger, False)

    # Wait for echo to go high (start time)
    pulse_start = time.time()
    timeout_start = pulse_start
    while GPIO.input(echo) == 0:
        pulse_start = time.time()
        if pulse_start - timeout_start > timeout:
            return -1  # Timeout, no echo received

    # Wait for echo to go low (end time)
    pulse_end = time.time()
    while GPIO.input(echo) == 1:
        pulse_end = time.time()
        if pulse_end - pulse_start > timeout:
            return -1  # Timeout, echo signal too long

    # Calculate pulse duration
    pulse_duration = pulse_end - pulse_start

    # Calculate distance in cm (speed of sound is 34300 cm/s)
    distance = pulse_duration * 17150
    return round(distance, 2)


def measure_all_sensors():
    distances = {}
    # Trigger and measure distances for each sensor
    for key, sensor in sensors.items():
        distances[key] = measure_distance(sensor["trigger"], sensor["echo"])

    return distances


try:
    while True:
        # Measure all sensor distances
        distances = measure_all_sensors()

        # Print distances (handle timeout case)
        for sensor, distance in distances.items():
            if distance == -1:
                print(f"{sensor.capitalize()} sensor: Timeout")
            else:
                print(f"{sensor.capitalize()} distance: {distance} cm")

        # Reduce waiting time for next measurement
        time.sleep(0.1)  # Faster measurement cycle

except KeyboardInterrupt:
    print("Measurement stopped by user")
    GPIO.cleanup()
