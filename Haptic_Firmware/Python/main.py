from machine import Pin, PWM
import time

# Setup 

# Pin Definitions
buzzer_pin = Pin(3, Pin.OUT)
haptic_pin = Pin(2, Pin.OUT)

# Initialize PWM 
buzzer_pwm = PWM(buzzer_pin, freq=1000)

# Set duty cycle to 40%. This is needed for the buzzer as vrated is 1.5V and 
duty_40_percent = int(0.45*1023)

#Function Definitions

#run_alert: Function that is used to alert user
def run_alert():
    for i in range(5):
        buzzer_pwm.duty(duty_40_percent)
        haptic_pin.on()

        time.sleep(0.4)

        buzzer_pwm.duty(0)
        haptic_pin.off()

        time.sleep(0.4)

#main

run_alert()
