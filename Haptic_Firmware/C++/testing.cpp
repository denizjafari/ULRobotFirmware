#include <BLEDevice.h>
#include <BLEUtils.h>
#include <BLEServer.h>

BLEServer *pServer = nullptr;
BLECharacteristic *pCharacteristic;
bool deviceConnected = false;

// UUIDs
#define SERVICE_UUID "12345678-1234-1234-1234-123456789abc"
#define CHARACTERISTIC_UUID "abcd1234-5678-9876-5432-abcd1234efgh"

class MyServerCallbacks: public BLEServerCallbacks {
    void onConnect(BLEServer* pServer) {
        deviceConnected = true;
        Serial.println("Client connected");
    }

    void onDisconnect(BLEServer* pServer) {
        deviceConnected = false;
        Serial.println("Client disconnected");
    }
};

void setup() {
    Serial.begin(115200);
    BLEDevice::init("ESP32-C3"); // Name of the device

    pServer = BLEDevice::createServer();
    pServer->setCallbacks(new MyServerCallbacks());

    BLEService *pService = pServer->createService(SERVICE_UUID);
    pCharacteristic = pService->createCharacteristic(
        CHARACTERISTIC_UUID,
        BLECharacteristic::PROPERTY_READ | BLECharacteristic::PROPERTY_WRITE
    );

    pService->start();
    BLEAdvertising *pAdvertising = BLEDevice::getAdvertising();
    pAdvertising->addServiceUUID(SERVICE_UUID);
    pAdvertising->start();

    Serial.println("Waiting for a client connection...");
}

void loop() {
    if (deviceConnected) {
        // Check if a characteristic was written to
        if (pCharacteristic->getValue() != "") {
            String receivedValue = pCharacteristic->getValue();  // Use Arduino String
            Serial.print("Received: ");
            Serial.println(receivedValue);  // Use Arduino String methods

            // Optionally respond back
            pCharacteristic->setValue("Acknowledged");  // Respond to the central device
            pCharacteristic->notify();  // Notify the central device (if notifications are enabled)
        }
    }
    delay(1000);
}

