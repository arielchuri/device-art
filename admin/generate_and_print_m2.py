#!/usr/bin/env python3
"""
Generate and print Milestone 2 physical folder dossiers.
- Only new Milestone 2 information
- Clean, compact typography (9.5pt body, 13pt h1, 11pt h2)
- Clearly labeled headers (Course, Student, Project, Date, Milestone)
- Two-sided duplex printing via lp
"""

import subprocess
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
FINAL_DIR = BASE_DIR / "meta" / "terms" / "fall2026" / "final"
WEASYPRINT_BIN = "/Users/arielchuri/.local/bin/weasyprint"

CSS = """
@page {
    size: letter portrait;
    margin: 0.45in 0.5in 0.45in 0.5in;
    @bottom-center {
        content: "Page " counter(page) " of " counter(pages);
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        font-size: 8pt;
        color: #777777;
    }
}

body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    font-size: 9.5pt;
    line-height: 1.35;
    color: #111111;
    margin: 0;
    padding: 0;
}

.header-banner {
    border-bottom: 2px solid #000000;
    padding-bottom: 6px;
    margin-bottom: 12px;
}

.course-tag {
    font-size: 8pt;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    color: #555555;
    font-weight: 600;
    margin-bottom: 2px;
}

.title {
    font-size: 14pt;
    font-weight: 700;
    margin: 0 0 4px 0;
    line-height: 1.15;
}

.meta-grid {
    display: table;
    width: 100%;
    margin-top: 4px;
    font-size: 8.5pt;
}

.meta-row {
    display: table-row;
}

.meta-cell-label {
    display: table-cell;
    width: 16%;
    font-weight: 600;
    color: #444444;
    padding: 1px 0;
}

.meta-cell-value {
    display: table-cell;
    padding: 1px 0;
}

h2 {
    font-size: 10.5pt;
    font-weight: 700;
    border-bottom: 1px solid #cccccc;
    padding-bottom: 2px;
    margin: 10px 0 6px 0;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    color: #222222;
}

h3 {
    font-size: 9.5pt;
    font-weight: 600;
    margin: 8px 0 4px 0;
    color: #333333;
}

p, ul {
    margin: 0 0 6px 0;
}

ul {
    padding-left: 18px;
}

li {
    margin-bottom: 2px;
}

pre, code {
    font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, Courier, monospace;
    font-size: 8pt;
}

pre {
    background-color: #f6f8fa;
    border: 1px solid #d0d7de;
    border-radius: 3px;
    padding: 6px 8px;
    margin: 6px 0;
    white-space: pre-wrap;
    line-height: 1.25;
}

.img-container {
    margin: 6px 0;
    text-align: center;
}

img {
    max-width: 100%;
    max-height: 2.7in;
    object-fit: contain;
    border: 1px solid #e1e4e8;
    border-radius: 2px;
}

.caption {
    font-size: 7.5pt;
    color: #555555;
    margin-top: 2px;
}

.notice-box {
    background-color: #fef8e7;
    border-left: 3px solid #f1a94e;
    padding: 6px 8px;
    margin: 6px 0;
    font-size: 8.5pt;
}

.badge {
    display: inline-block;
    padding: 1px 5px;
    border-radius: 2px;
    font-size: 7.5pt;
    font-weight: 600;
}
.badge-green { background-color: #e6ffed; color: #1a7f37; border: 1px solid #a8e5b6; }
.badge-yellow { background-color: #fff8c5; color: #9a6700; border: 1px solid #ffe885; }
"""

def generate_tahisha_html(folder):
    return f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>{CSS}</style>
</head>
<body>
<div class="header-banner">
    <div class="course-tag">Device Art (Fall 2026) &bull; Parsons / The New School</div>
    <div class="title">Tahisha Jain &mdash; Milestone 2 Dossier</div>
    <div class="meta-grid">
        <div class="meta-row">
            <div class="meta-cell-label">Project:</div>
            <div class="meta-cell-value"><strong>S.P.I.R.A.L.</strong> (Speculative Possibility &amp; Interpretive Reasoning Assistance Loop)</div>
        </div>
        <div class="meta-row">
            <div class="meta-cell-label">Milestone:</div>
            <div class="meta-cell-value">Milestone 2: Functional Diagram, Pseudo-Code &amp; Benchtop Circuit <span class="badge badge-green">Graded: 50 / 50</span></div>
        </div>
        <div class="meta-row">
            <div class="meta-cell-label">Submitted:</div>
            <div class="meta-cell-value">November 3, 2026 &bull; Source: portfolio.newschool.edu/jaint233</div>
        </div>
    </div>
</div>

<h2>1. Functional System State Architecture</h2>
<div class="img-container">
    <img src="file://{folder}/m2_functional_diagram.jpg" style="max-height: 2.2in;">
    <div class="caption">Figure 1: S.P.I.R.A.L. Functional State Diagram (READY &rarr; LISTENING &rarr; THINKING &rarr; OVERTHINKING &rarr; RESPONSE &rarr; READY)</div>
</div>

<h2>2. Firmware Pseudo-Code (Non-Blocking Loop)</h2>
<pre>INITIALIZE SYSTEM:
  Set up Raspberry Pi Pico W
  Initialize SSD1306 OLED via I2C (GP0 SDA, GP1 SCL)
  Configure pushbuttons: START (GP16), YES (GP18), NO (GP19) with internal pull-up / debouncing
  Configure Piezo Buzzer (GP17) &amp; Status LEDs (GP14, GP15)
  state = READY; Display initial greeting on OLED

MAIN LOOP:
  current_time = time.monotonic()
  Poll and debounce START, YES, NO buttons
  IF START pressed:
      IF state == READY: state = LISTENING; record state_start_time; play beep; update OLED
      ELSE: state = READY
  IF (YES or NO pressed):
      Record user response; state = THINKING; record state_start_time; update OLED
  IF state == THINKING:
      Render thinking animation; IF elapsed &gt;= thinking_duration: state = OVERTHINKING
  IF state == OVERTHINKING:
      Escalate feedback urgency (buzzers, flashing); IF elapsed &gt;= overthink_duration: state = RESPONSE
  IF state == RESPONSE:
      Display LLM generated response; play tone; IF elapsed &gt;= response_duration: state = READY
  Update buzzer &amp; LEDs non-blocking; Repeat loop</pre>

<h2>3. Benchtop Circuit &amp; Hardware Prototype</h2>
<table style="width: 100%;">
<tr>
    <td style="width: 50%; vertical-align: top; padding-right: 4px;">
        <div class="img-container">
            <img src="file://{folder}/m2_circuit_wiring.jpg" style="max-height: 2.0in;">
            <div class="caption">Figure 2: Breadboard wiring schematic</div>
        </div>
    </td>
    <td style="width: 50%; vertical-align: top; padding-left: 4px;">
        <div class="img-container">
            <img src="file://{folder}/m2_breadboard_circuit.png" style="max-height: 2.0in;">
            <div class="caption">Figure 3: Live benchtop Pico circuit</div>
        </div>
    </td>
</tr>
<tr>
    <td style="width: 50%; vertical-align: top; padding-right: 4px;">
        <div class="img-container">
            <img src="file://{folder}/m2_oled_display_test.png" style="max-height: 1.8in;">
            <div class="caption">Figure 4: SSD1306 OLED interface test</div>
        </div>
    </td>
    <td style="width: 50%; vertical-align: top; padding-left: 4px;">
        <div class="img-container">
            <img src="file://{folder}/m2_serial_monitor.png" style="max-height: 1.8in;">
            <div class="caption">Figure 5: Non-blocking serial debug trace</div>
        </div>
    </td>
</tr>
</table>

<h2>4. Prototyping Progression Log</h2>
<ul>
    <li><strong>Display Pivot</strong>: Tested two separate 16&times;2 character LCDs; encountered severe contrast and corrupt character errors. Pivoted to an SSD1306 I2C OLED display on GP0/GP1, achieving immediate stable text rendering.</li>
    <li><strong>Non-Blocking Control</strong>: Replaced standard blocking delays with <code>time.monotonic()</code> elapsed timestamps, enabling continuous button polling and smooth animation frames.</li>
    <li><strong>Input Validation</strong>: Successfully integrated START, YES, and NO inputs with button debouncing and validated state transitions.</li>
</ul>
</body>
</html>
"""

def generate_karina_html(folder):
    return f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>{CSS}</style>
</head>
<body>
<div class="header-banner">
    <div class="course-tag">Device Art (Fall 2026) &bull; Parsons / The New School</div>
    <div class="title">Karina Umekubo &mdash; Milestone 2 Dossier</div>
    <div class="meta-grid">
        <div class="meta-row">
            <div class="meta-cell-label">Project:</div>
            <div class="meta-cell-value"><strong>Digital Plant Living Tamagotchi</strong></div>
        </div>
        <div class="meta-row">
            <div class="meta-cell-label">Milestone:</div>
            <div class="meta-cell-value">Milestone 2: Functional Diagram, Pseudo-Code &amp; Benchtop Circuit <span class="badge badge-green">Complete</span></div>
        </div>
        <div class="meta-row">
            <div class="meta-cell-label">Submitted:</div>
            <div class="meta-cell-value">November 5, 2026 &bull; Source: portfolio.newschool.edu/umekk050</div>
        </div>
    </div>
</div>

<h2>1. Functional System State Machine</h2>
<div class="img-container">
    <img src="file://{folder}/m2_state_machine_diagram.png" style="max-height: 2.3in;">
    <div class="caption">Figure 1: Digital Plant System State Machine (Seed &rarr; Sprout &rarr; Mature Plant / Death States)</div>
</div>

<h2>2. Firmware Pseudo-Code &amp; Hardware Pinouts</h2>
<pre># Hardware Pinout &amp; I2C Configuration:
# - Raspberry Pi Pico 3.3V to Breadboard Power Rail; GND to Ground Rail
# - OLED SSD1306: GND -> GND (Pin 18), VDD -> 3V3, SCK -> GP9 (I2C0 SCL), SDA -> GP8 (I2C0 SDA)

# Potentiometer 1 (Water / Care Level) -> Blue Indicator LED:
#   Read ADC continuous voltage from Potentiometer 1
#   IF voltage is LOW: Blue LED PWM dims down (insufficient water)
#   IF voltage is HIGH: Blue LED PWM increases brightness (high moisture)

# Potentiometer 2 (Sunlight / Energy Level) -> Yellow Indicator LED:
#   Read ADC continuous voltage from Potentiometer 2
#   IF voltage is LOW: Yellow LED PWM dims down (darkness)
#   IF voltage is HIGH: Yellow LED PWM increases brightness (full sunlight)

# Dual-Potentiometer State Synthesis -> OLED Graphics:
#   Combine Pot 1 and Pot 2 readings into plant health index:
#   IF (Pot1 &amp; Pot2 are LOW / under threshold):
#       Display Seed bitmap on OLED (dormant state)
#   IF (Pot1 &amp; Pot2 are BALANCED / within healthy range):
#       Display Sprout / Flourishing Plant bitmap on OLED
#   IF (Pot1 or Pot2 are EXCESSIVE / over-watered / scorched):
#       Display Dead Plant / Wilted bitmap on OLED

# Asset Handling:
#   Import 1-bit monochrome bitmaps for seed, sprout, and dead plant from byte arrays.</pre>

<h2>3. Circuit Wiring Schematic &amp; Benchtop Prototype</h2>
<table style="width: 100%;">
<tr>
    <td style="width: 50%; vertical-align: top; padding-right: 4px;">
        <div class="img-container">
            <img src="file://{folder}/m2_circuit_schematic.png" style="max-height: 2.2in;">
            <div class="caption">Figure 2: Circuit wiring diagram (Pico, dual pots, LEDs, OLED)</div>
        </div>
    </td>
    <td style="width: 50%; vertical-align: top; padding-left: 4px;">
        <div class="img-container">
            <img src="file://{folder}/m2_benchtop_circuit.jpg" style="max-height: 2.2in;">
            <div class="caption">Figure 3: Benchtop circuit verified on solderless breadboard</div>
        </div>
    </td>
</tr>
</table>

<h2>4. Implementation Notes</h2>
<ul>
    <li>Dual analog potentiometers mapped via ADC channels to dynamic PWM duty cycles controlling LED brightness.</li>
    <li>SSD1306 OLED successfully initialized and driven via software state evaluations comparing dual analog inputs against plant vitality thresholds.</li>
    <li>Benchtop circuit verified on solderless breadboard before enclosure cutting and mechanical prototyping.</li>
</ul>
</body>
</html>
"""

def generate_ana_html(folder):
    return f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>{CSS}</style>
</head>
<body>
<div class="header-banner">
    <div class="course-tag">Device Art (Fall 2026) &bull; Parsons / The New School</div>
    <div class="title">Ana Cherkezishvili &mdash; Milestone 2 Dossier</div>
    <div class="meta-grid">
        <div class="meta-row">
            <div class="meta-cell-label">Project:</div>
            <div class="meta-cell-value"><strong>GlitchCam Camera</strong> (Pivot from Emotional Projection Pod)</div>
        </div>
        <div class="meta-row">
            <div class="meta-cell-label">Milestone:</div>
            <div class="meta-cell-value">Milestone 2: Concept Pivot &amp; Hardware Sourcing <span class="badge badge-yellow">Graded: 20 / 50</span></div>
        </div>
        <div class="meta-row">
            <div class="meta-cell-label">Submitted:</div>
            <div class="meta-cell-value">November 4, 2026 &bull; Source: Notion Page</div>
        </div>
    </div>
</div>

<div class="notice-box">
    <strong>Instructor Canvas Review Note:</strong> <em>"Need the milestone 2 items as soon as you can and I will regrade."</em><br>
    The submission documents a major creative pivot to a standalone glitch camera, along with a newly sourced component bill of materials. The functional diagram, firmware pseudo-code, and breadboard benchtop circuit remain pending.
</div>

<h2>1. Creative Pivot Narrative</h2>
<p><strong>New Idea &mdash; GlitchCam Camera:</strong> A handheld tangible digital camera engineered to capture real-time optical frames and deliberately subject the image buffer to computational glitching, pixel shifts, and color-channel displacements before saving and displaying the photograph as interactive glitch art.</p>

<h2>2. Sourced Component BOM</h2>
<table style="width: 100%; border-collapse: collapse; font-size: 8.5pt; margin: 6px 0;">
<tr style="background-color: #f1f3f5; font-weight: 600; border-bottom: 1px solid #ced4da;">
    <th style="text-align: left; padding: 4px 6px;">Component</th>
    <th style="text-align: left; padding: 4px 6px;">Model / Specification</th>
    <th style="text-align: left; padding: 4px 6px;">Function in Camera</th>
</tr>
<tr style="border-bottom: 1px solid #e9ecef;">
    <td style="padding: 4px 6px;"><strong>Compute Core</strong></td>
    <td style="padding: 4px 6px;">Adafruit ESP32 Feather V2 (8MB Flash + 2MB PSRAM, STEMMA QT)</td>
    <td style="padding: 4px 6px;">High-speed frame capture, image buffer manipulation &amp; SPI display drive</td>
</tr>
<tr style="border-bottom: 1px solid #e9ecef;">
    <td style="padding: 4px 6px;"><strong>Optical Sensor</strong></td>
    <td style="padding: 4px 6px;">Adafruit OV5640 Camera Breakout (72&deg; Lens, Autofocus)</td>
    <td style="padding: 4px 6px;">Digital image sensor capturing RGB frames</td>
</tr>
<tr style="border-bottom: 1px solid #e9ecef;">
    <td style="padding: 4px 6px;"><strong>Display &amp; Storage</strong></td>
    <td style="padding: 4px 6px;">Adafruit 1.54" 240&times;240 Wide Angle TFT LCD (ST7789) + MicroSD</td>
    <td style="padding: 4px 6px;">Real-time viewfinder screen and SD card image archive</td>
</tr>
<tr style="border-bottom: 1px solid #e9ecef;">
    <td style="padding: 4px 6px;"><strong>Memory Card</strong></td>
    <td style="padding: 4px 6px;">Centon 32GB SDHC Memory Card (UHS-I U1 V10 A1)</td>
    <td style="padding: 4px 6px;">Non-volatile file storage for captured glitch images</td>
</tr>
<tr style="border-bottom: 1px solid #e9ecef;">
    <td style="padding: 4px 6px;"><strong>Power System</strong></td>
    <td style="padding: 4px 6px;">Lithium Ion Polymer Battery (3.7V, 1200mAh)</td>
    <td style="padding: 4px 6px;">Portable standalone camera power via Feather JST port</td>
</tr>
</table>

<h2>3. Sourced Hardware Documentation</h2>
<table style="width: 100%;">
<tr>
    <td style="width: 33%; text-align: center; padding: 2px;">
        <img src="file://{folder}/m2_hardware_part_1.png" style="max-height: 1.6in;">
        <div class="caption">ESP32 Feather V2</div>
    </td>
    <td style="width: 33%; text-align: center; padding: 2px;">
        <img src="file://{folder}/m2_hardware_part_2.png" style="max-height: 1.6in;">
        <div class="caption">ST7789 1.54" TFT LCD</div>
    </td>
    <td style="width: 33%; text-align: center; padding: 2px;">
        <img src="file://{folder}/m2_hardware_part_5.png" style="max-height: 1.6in;">
        <div class="caption">OV5640 Camera Breakout</div>
    </td>
</tr>
</table>

<h2>4. Outstanding Milestone 2 Requirements for Regrading</h2>
<ul>
    <li><strong>State Machine Diagram</strong>: Visual flow (Idle Viewfinder &rarr; Shutter Button Press &rarr; Sensor Capture &rarr; Glitch Transformation &rarr; TFT / SD Write).</li>
    <li><strong>Firmware Pseudo-Code</strong>: Pseudocode showing camera initialization, SPI LCD frame buffer transfer, and button triggering.</li>
    <li><strong>Benchtop Breadboard Circuit</strong>: Photo of wired components on solderless breadboard confirming hardware communications.</li>
</ul>
</body>
</html>
"""

def generate_john_html(folder):
    return f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>{CSS}</style>
</head>
<body>
<div class="header-banner">
    <div class="course-tag">Device Art (Fall 2026) &bull; Parsons / The New School</div>
    <div class="title">John O'Donovan &mdash; Milestone 2 Dossier</div>
    <div class="meta-grid">
        <div class="meta-row">
            <div class="meta-cell-label">Project:</div>
            <div class="meta-cell-value"><strong>Sound-Reactive / Kinetic Articulation Instrument</strong></div>
        </div>
        <div class="meta-row">
            <div class="meta-cell-label">Milestone:</div>
            <div class="meta-cell-value">Milestone 2: Functional Diagram &amp; State Architecture <span class="badge badge-yellow">Graded: 35 / 50</span></div>
        </div>
        <div class="meta-row">
            <div class="meta-cell-label">Submitted:</div>
            <div class="meta-cell-value">November 4, 2026 &bull; Source: portfolio.newschool.edu/odonj792</div>
        </div>
    </div>
</div>

<div class="notice-box">
    <strong>Instructor Canvas Review Note:</strong> <em>"Seems to need current state of circuit photo and pseudo-code."</em><br>
    The student submitted system architecture and acoustic trigger response diagrams. The benchtop breadboard circuit photo and pseudo-code logic are outstanding for full regrading.
</div>

<h2>1. Functional System State Architecture Diagram</h2>
<div class="img-container">
    <img src="file://{folder}/m2_fsm_state_diagram.png" style="max-height: 2.5in;">
    <div class="caption">Figure 1: Functional State Machine Diagram (Sound capture, threshold analysis, motor articulation, and LED strobe outputs)</div>
</div>

<h2>2. Audio Trigger Response Graph</h2>
<div class="img-container">
    <img src="file://{folder}/m2_audio_trigger_graph.png" style="max-height: 2.2in;">
    <div class="caption">Figure 2: Audio trigger threshold curve modeling impulse response versus ambient acoustic baseline</div>
</div>

<h2>3. System Functional Architecture Breakdown</h2>
<ul>
    <li><strong>Audio Acquisition</strong>: Analog microphone module monitored continuously via microcontroller ADC input.</li>
    <li><strong>Threshold Logic</strong>: Software evaluates peak amplitude against dynamic trigger floor to isolate intentional sound events from room background noise.</li>
    <li><strong>Dual Kinetic/Visual Actuation</strong>: High-amplitude acoustic trigger fires coordinated physical actuation (servo/motor movement) paired with visual indicator responses.</li>
    <li><strong>Cooldown State</strong>: System enters dead-band cooldown after firing to avoid recursive acoustic feedback triggering.</li>
</ul>

<h2>4. Outstanding Milestone 2 Requirements for Regrading</h2>
<ul>
    <li><strong>Firmware Pseudo-Code</strong>: Written logic outlining ADC polling, threshold evaluation, servo PWM positioning, and cooldown timers.</li>
    <li><strong>Benchtop Breadboard Circuit Photo</strong>: Photographic documentation of the wired prototype showing microcontroller, microphone sensor, and actuator connections.</li>
</ul>
</body>
</html>
"""

def build_pdf(html_str, pdf_path):
    temp_html = pdf_path.with_suffix(".html")
    with open(temp_html, "w") as f:
        f.write(html_str)
    
    cmd = [WEASYPRINT_BIN, str(temp_html), str(pdf_path)]
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if res.returncode != 0:
        print(f"WeasyPrint error for {pdf_path.name}: {res.stderr}")
        return False
    print(f"Compiled PDF: {pdf_path.name} ({pdf_path.stat().st_size} bytes)")
    return True

def print_pdf(pdf_path):
    printer = "EPSON_ET_4550_S"
    # Duplex long edge option
    cmd = ["lp", "-d", printer, "-o", "sides=two-sided-long-edge", str(pdf_path)]
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    print(f"Print job result for {pdf_path.name}: {res.stdout.strip()} {res.stderr.strip()}")

def main():
    students = [
        ("tahisha-jain", generate_tahisha_html),
        ("karina-umekubo", generate_karina_html),
        ("ana-cherkezishvili", generate_ana_html),
        ("john-o-donovan", generate_john_html)
    ]
    
    for slug, gen_fn in students:
        folder = FINAL_DIR / slug
        pdf_path = folder / "milestone_02_dossier.pdf"
        html_content = gen_fn(folder)
        success = build_pdf(html_content, pdf_path)
        if success:
            print_pdf(pdf_path)

if __name__ == "__main__":
    main()
