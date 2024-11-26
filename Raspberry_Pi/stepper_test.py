import RPi.GPIO as GPIO
import time

# Pin definitions
DIR_PIN = 27    # GPIO27, direction pin
STEP_PIN = 17   # GPIO17, step pin
ENABLE_PIN = 22 # GPIO22, enable pin

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR_PIN, GPIO.OUT)
GPIO.setup(STEP_PIN, GPIO.OUT)
GPIO.setup(ENABLE_PIN, GPIO.OUT)

# Enable the motor driver
GPIO.output(ENABLE_PIN, GPIO.LOW)  # LOW enables the motor

# Motor parameters
steps_per_revolution = 200  # Full steps for 360ï¿½ rotation (1.8ï¿½ per step)
step_delay = 0.1           # Delay between steps in seconds (adjust for speed)

# Function to rotate motor
def rotate_motor(steps, direction, delay):
    GPIO.output(DIR_PIN, direction)
    for _ in range(steps):
        GPIO.output(STEP_PIN, GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(STEP_PIN, GPIO.LOW)
        time.sleep(delay)

try:
    print("Rotating motor 360 degrees in clockwise direction.")
    rotate_motor(steps_per_revolution, GPIO.HIGH, step_delay)  # Clockwise
    time.sleep(1)  # Pause for 1 second
    
    print("Rotating motor 360 degrees in counter-clockwise direction.")
    rotate_motor(steps_per_revolution, GPIO.LOW, step_delay)  # Counter-clockwise

except KeyboardInterrupt:
    print("Exiting...")
finally:
    GPIO.cleanup()
