# Technical Guide: Networked I/O on Raspberry Pi Pico W

This document outlines the generalized technical architecture for using the onboard 2.4GHz Wi-Fi radio (Infineon CYW43439) on the Raspberry Pi Pico W for networked data exchange and external API communication.

---

## 1. Generalized Architecture (Physical Transduction <-> Remote Endpoint)

```
┌─────────────────────────┐         Wi-Fi (HTTPS/REST)          ┌─────────────────────────┐
│   PHYSICAL MICROCONTROLLER│ ──────────────────────────────────> │     REMOTE API / LLM    │
│   (Raspberry Pi Pico W) │       Serialized Sensor Payloads    │        ENDPOINT         │
│                         │                                     │                         │
│ • Analog / Digital Input│ <────────────────────────────────── │ • External computation  │
│ • I2C / SPI Peripherals │         JSON Data / Strings         │ • Web APIs / Databases  │
│ • Actuators & Displays  │                                     │ • Local Ollama Server   │
└─────────────────────────┘                                     └─────────────────────────┘
```

---

## 2. Technical Capabilities (Generalized Engineering Terms)

1. **Sensor Telemetry Upstream**:
   - Polling local physical sensors (temperature, distance, analog voltage, capacitive touch).
   - Serializing sensor readings into JSON payloads.
   - Sending HTTP `POST` requests over local Wi-Fi to a remote service or local model proxy.

2. **Downstream Actuation & Display**:
   - Receiving response strings or structured JSON from the network.
   - Parsing text data and rendering it to local hardware (e.g. SSD1306 OLED display, char-by-char).
   - Mapping received numerical values to PWM duty cycles, servo angles, or NeoPixel color arrays.

---

## 3. Reference Implementation in CircuitPython

```python
import ssl
import wifi
import socketpool
import adafruit_requests

# 1. Initialize Wi-Fi radio
wifi.radio.connect("NETWORK_SSID", "NETWORK_PASSWORD")

# 2. Configure HTTP session
pool = socketpool.SocketPool(wifi.radio)
requests = adafruit_requests.Session(pool, ssl.create_default_context())

# 3. Transmit payload to REST endpoint
headers = {"Content-Type": "application/json"}
payload = {"sensor_value": 42.5}
response = requests.post(
    "https://api.example.com/v1/endpoint",
    json=payload,
    headers=headers
)

# 4. Transduce response data
data = response.json()
print("Received:", data)
```
