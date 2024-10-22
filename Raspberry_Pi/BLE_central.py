from bluepy.btle import Peripheral, UUID
import binascii

# ESP32-C3 BLE device address (replace with your actual address)
esp32_address = "ec:da:3b:bf:26:2e"  # Find this using a BLE scanning tool

# UUIDs for the BLE service and characteristic
SERVICE_UUID = "12345678-1234-5678-1234-56789abcdef0"
CHAR_UUID = "12345678-1234-5678-1234-56789abcdef1"

def send_hex_data(hex_string):
    # Convert the hex string to bytes
    data_to_send = bytes.fromhex(hex_string)
    
    # Connect to the ESP32-C3 device
    esp32 = Peripheral(esp32_address)
    
    # Get the service and characteristic
    service = esp32.getServiceByUUID(UUID(SERVICE_UUID))
    char = service.getCharacteristics(UUID(CHAR_UUID))[0]
    
    # Write the data to the characteristic
    print(f"Sending hex data: {hex_string}")
    char.write(data_to_send)
    
    # Disconnect after sending data
    esp32.disconnect()

# Example: Sending hex data '01' to trigger an action on the ESP32-C3
send_hex_data('01')  # This will trigger the `run_alert()` function on ESP32-C3

# Example: Sending hex data '02' to stop the action
send_hex_data('02')  # This will trigger the `stop_alert()` function on ESP32-C3
