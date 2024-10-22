# ULRobotFirmware

Haptic Firmware
- Flashing ESP32C3 with MicroPython
  1. Open CMD.
  2. Make sure Python is installed.
  3. Enter command "python -m pip install esptool".
  4. Check if installed with "python -m esptool".
  5. Download latest micropython firmware from https://micropython.org/download/esp32c3-usb/. It should be a bin file, and save it to where you plan on working.
  6. Enter this command "python -m esptool --chip esp32c3 --port COM13 erase_flash". Change COM13 to the port that the esp32c3 is connected to on your PC.
  7. Enter this command "python -m esptool --chip esp32c3 --port COM13 --baud 115200 write_flash -z 0x0 esp32c3-usb-20230426-v1.20.0.bin". Again, change COM13 to the port that the esp32c3 is connected to on your PC. Also, change the bin file name to the one you downloaded.
  8. Program esp32c3 through your IDE.

- Installing aioble library for ble communication
  1. git clone https://github.com/micropython/micropython-lib.git
  2. Drag and drop aioble into pymakr workspace, or just clone it directly in ws.
  3. FYI: I found issues with this method, so I instead just downloaded the aioble package in thonny and programmed there.
