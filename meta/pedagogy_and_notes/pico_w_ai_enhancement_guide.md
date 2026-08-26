# Enhancing Device Art Objects with AI & The Raspberry Pi Pico W

## 1. The Core Architecture (Physical Transduction <-> Cloud/Local AI)

Because the **Raspberry Pi Pico W** includes a 2.4GHz Wi-Fi/Bluetooth radio (Infineon CYW43439), it can connect directly to local networks or the internet. 

While the Pico's microcontroller (RP2040) cannot run a massive neural network internally, its radio allows it to act as an **embodied physical conduit for AI models** (Gemini, Claude, local Ollama endpoints).

```
┌─────────────────────────┐         Wi-Fi (HTTPS/Sockets)       ┌─────────────────────────┐
│   PHYSICAL DEVICE       │ ─────────────────────────────────>  │     AI ENDPOINT         │
│   (Raspberry Pi Pico W) │                                     │ (Gemini / Claude /      │
│                         │ <─────────────────────────────────  │  Local Ollama Server)   │
│ • Physical Knobs/Dials  │          JSON Response              │                         │
│ • Photocell / Ultrasonic│     (State machine behaviors,       │ • Generative text/audio │
│ • OLED Display / Voice  │      absurd responses, dynamic      │ • Semantic perception   │
│ • NeoPixels & Motors    │      mechanics)                     │ • System subversion     │
└─────────────────────────┘                                     └─────────────────────────┘
```

---

## 2. Compelling Device Art & Political Concepts using Pico W + AI

### A. The "Disobedient Oracle" (Anti-Virtual Device)
- **Concept**: A small physical object with a single rotary knob and an old receipt printer or OLED screen.
- **Interaction**: The user turns the dial to select a topic or presses a tactile button. The Pico W queries Gemini with a custom system prompt that generates sarcastic, subversive, or poetic commentary on algorithmic society.

### B. The "Absurd Environmental Translator" (Chindōgu + AI)
- **Concept**: The Pico W reads analog physical values (room temperature, light intensity, ultrasonic proximity) and sends the numerical values to an LLM.
- **LLM Prompt**: *"You are an anxious Victorian spirit trapped inside an electronic thermometer. Interpret these sensor values: Temperature 72F, Light 45%."*
- **Output**: The Pico prints or displays the Victorian ghost's dramatic reaction on an OLED display or buzzer.

### C. The "Adversarial Noise Generator" (Anti-Surveillance Object)
- **Concept**: A physical "smart home decoy" sitting on a desk.
- **Interaction**: The Pico W periodically connects via Wi-Fi and streams synthetic, AI-generated nonsensical browsing traffic or queries to poison local advertising profile trackers.

---

## 3. Technical Implementation in CircuitPython (Zero Friction for Students)

```python
import ssl
import wifi
import socketpool
import adafruit_requests

# 1. Connect to Wi-Fi
wifi.radio.connect("PARSONS_WIFI", "password")

# 2. Setup HTTPS session
pool = socketpool.SocketPool(wifi.radio)
requests = adafruit_requests.Session(pool, ssl.create_default_context())

# 3. Query AI Endpoint (e.g. Gemini or local proxy)
headers = {"Content-Type": "application/json"}
payload = {
    "contents": [{"parts": [{"text": "Generate a 1-sentence poetic fortune about a toaster."}]}]
}
response = requests.post(
    "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=API_KEY",
    json=payload,
    headers=headers
)

# 4. Parse & Transduce to Hardware
text = response.json()["candidates"][0]["content"]["parts"][0]["text"]
oled.text(text, 0, 0, 1)
oled.show()
```

---

## 4. Where This Fits into the Curriculum
- **Week 07/08**: Introduced during *Complex Systems & Networked Interactions*.
- Gives students the option to use AI as an **unpredictable, conversational, or adversarial material** inside their physical enclosures.
