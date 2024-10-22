from micropython import const
import aioble
import bluetooth
import struct
import asyncio
from machine import Pin
import time

# Setup 

# Pin Definitions
buzzer_pin = Pin(3, Pin.OUT)
haptic_pin = Pin(2, Pin.OUT)

# Initialize PWM 
buzzer_pwm = PWM(buzzer_pin, freq=1000)

# Set duty cycle to 40%. This is needed for the buzzer as vrated is 1.5V and 
duty_40_percent = int(0.45*1023)

# UUIDs for BLE service and characteristic
_SERVICE_UUID = bluetooth.UUID("12345678-1234-5678-1234-56789abcdef0")
_CHAR_UUID = bluetooth.UUID("12345678-1234-5678-1234-56789abcdef1")

# Create BLE service and characteristic
service = aioble.Service(_SERVICE_UUID)
char = aioble.Characteristic(service, _CHAR_UUID, write=True, read=True)

# Register the service
aioble.register_services(service)

# handle_data: Function to await client connection and handle incoming data
async def handle_data():
    while True:
        try:
            # Wait for a raspberry pi (client) to connect
            async with await aioble.advertise(250_000, name="ESP32-C3", services=[_SERVICE_UUID]) as connection:
                print("Connected to:", connection.device)

                # Wait for data to be written to the characteristic
                while True:
                    data = await char.written()
                    print("Data received:", data)

                    # Call haptic function if called by client
                    if value == b'\0x01':
                        print("Run Haptics")
                        await run_alert()
                    else:
                        print("Unknown command")

        except asyncio.CancelledError:
            print("Connection closed")
        except Exception as e:
            print("Error:", e)

#run_alert: Function that is used to alert user
async def run_alert():
    for i in range(5):
        buzzer_pwm.duty(duty_40_percent)
        haptic_pin.on()

        time.sleep(0.4)

        buzzer_pwm.duty(0)
        haptic_pin.off()

        time.sleep(0.4)


# Main function to run the BLE task
async def main():
    await handle_data()

# The ble connection is run as a asynchronous run to prevent concurent tasks blocking each other, if
# other asynchronous tasks were added.
asyncio.run(main())

