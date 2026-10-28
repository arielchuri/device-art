---
title: "Fabrication & Enclosure Resources"
published: false
---

# Fabrication & Enclosure Resources

Central reference hub for physical prototyping, laser cutting, 3D modeling, enclosure joinery, campus fabrication labs, and material suppliers for **Device Art (PSAM 2230)**.

---

## 1. Laser Cutting & 2D Vector Fabrication

- **Laser Cutter Setup & Vector Preparation**:
  - [Illustrator Universal Laser Cutter Guide (PDF)](../files/cheatsheets/Illustrator-Universal-Laser-Guide-2025.pdf) — Preparing vector cut, vector engrave, and raster etch files for Universal Laser Systems (ULS) machines.
- **Reference Enclosure Vector Files**:
  - [MoodLight Laser Cut Pattern (`moodlight_laserpattern.svg`)](../assignments/moodlight/moodlight_laserpattern.svg) — Sample laser-cut acrylic panel layout with standoff mounting holes and sensor apertures.
  - [MoodLight Mechanical Drawing (`moodlight_drawing.svg`)](../assignments/moodlight/moodlight_drawing.svg) — Dimensioned orthographic assembly reference.
  - [MoodLight Project Brief](../assignments/moodlight/moodlight.md) — Hardware assembly notes using M3 machine screws, M3x6mm standoffs, copper tape, and *Scigrip 4* acrylic cement.
- **Campus Laser Lab Store**:
  - [Parsons E4 Laser Lab Store](https://epay.newschool.edu/C21120_ustores/web/store_main.jsp?STOREID=56) — On-campus acrylic and sheet stock purchase portal.

---

## 2. Rapid Prototyping & Cardboard Engineering

- [Cardboard Engineering & Rapid Enclosure Prototyping Guide](cardboard_engineering_guide.md) — Complete guide covering:
  - Material properties (corrugated E/B flute, chipboard, mat board, foam core).
  - Drafting 2D unfolded net patterns, folding tabs, and material thickness allowances.
  - Standard component cutout tolerances for OLED displays (SSD1306), panel-mount pushbuttons/potentiometers, USB-C relief slots, and ultrasonic sensors (HC-SR04).
  - Strain relief, removable service access panels, and electrical insulation.

---

## 3. 3D Modeling & CAD Fabrication

- **Course Guides**:
  - [Blender 3D Modeling Cheatsheet](../files/cheatsheets/blender_cheatsheet.md) — Viewport navigation, transformations, modifiers, and boolean operations for enclosure design.
  - [Assignment 04: 3D Modeling Speculative Device in Blender](../assignments/assignment_04_blender_device_modeling.md)
  - [Final Project Milestone 3: Mechanical Drawing & Enclosure Mockup](../assignments/final_project_milestone_03_enclosure.md) — Requirements for dimensioned mechanical drawings (SVG/DXF/STEP/STL) and physical tolerance test-fits.
- **CAD & Modeling Software**:
  - [Blender 3D](https://www.blender.org/) — Open-source 3D modeling, rendering, and mesh preparation.
  - [Autodesk Fusion 360 (Education Access)](https://www.autodesk.com/products/fusion-360/education-overview) — Parametric CAD for 3D printing, sheet-metal/acrylic folding, and precision mechanical enclosures.
  - [Inkscape](https://inkscape.org/) — Open-source 2D vector editor for SVG laser-cutting templates.

---

## 4. Soldering & Permanent Circuit Assembly

Transitioning from a benchtop breadboard to a finished physical enclosure requires durable, permanent electrical connections. Jumper wires on solderless breadboards easily dislodge, vibrate loose, or short against enclosure walls during handling.

### Moving from Breadboard to Permanent Board
- **Perma-Proto & Perfboards**: Transfer verified breadboard circuits to plated through-hole protoboards (such as Adafruit Perma-Proto boards, which replicate the standard 5-hole breadboard bus layout) or stripboards for compact mounting.
- **Soldered Header Pins & Sockets**: Solder male or female header pins to microcontrollers (Raspberry Pi Pico) and breakout modules (SSD1306 OLED, DS3231 RTC) rather than friction-fitting or wrapping bare wire.
- **Wire Selection**:
  - **Solid-Core Wire (22 AWG)**: Ideal for stationary point-to-point connections routed flat against a protoboard.
  - **Stranded Wire (24–28 AWG)**: Required for connections running between the circuit board and panel-mounted components (pushbuttons, potentiometers, switches, NeoPixel rings). Stranded wire is flexible and resists metal fatigue when opening and closing enclosures.

### Soldering Best Practices
- **Temperature & Iron Setup**: Use a temperature-controlled iron set to **350°C–370°C (660°F–700°F)** for lead-free solder. Keep the tip clean using a brass wire sponge.
- **Heat the Joint, Not the Solder**: Touch the iron tip simultaneously to the copper pad and component lead for 1–2 seconds to heat both elements, then feed solder into the joint (not directly onto the iron tip). Solder will naturally flow toward the heated metal.
- **Volcano Fillet**: A proper solder joint forms a concave cone ("volcano shape") that completely covers the circular copper pad and adheres smoothly to the lead. Avoid cold solder joints (rough, dull, rounded balls caused by insufficient heat) and solder bridges (unwanted connections spanning adjacent pins).
- **Insulation with Heat-Shrink Tubing**: Always slide a piece of heat-shrink tubing over wire leads *before* making the connection. Slide the sleeve over the completed joint and shrink with a heat gun to insulate bare conductors and prevent short circuits.
- **Mechanical Strain Relief**: Solder joints are electrical bonds, not structural fasteners. Never allow wires to dangle unsupported. Anchor wire harnesses inside the chassis using zip ties, cable clamps, or adhesive anchor pads to protect solder points from tension and pulling.

### Campus Electronics Labs & Safety
- **Parsons Making Center AMT E-Lab** (63 Fifth Ave & 2 W 13th St): Fully equipped workbenches featuring Hakko and Weller temperature-controlled soldering stations, bench fume extractors, PanaVise PCB holders, flush cutters, wire strippers, and desoldering pumps.
- **Fume Extraction & Safety**: Always activate local benchtop fume extractors while soldering. Wear safety glasses to protect against flying wire clippings and solder splatters. Wash hands after handling solder and electronics hardware.
- Reference: [Sparkle Labs Electronics Manual (PDF)](../files/readings/manual_wm_s.pdf) — Circuit wiring fundamentals and moving from breadboards to permanent projects.

---

## 5. Parsons Making Center & Campus Facilities

- **Making Center Hubs (63 Fifth Ave & 2 W 13th St)**:
  - [Parsons Making Center Portal](https://makingcenter.parsons.edu/) — Facility hours, laser cutter and 3D printer reservations, and safety orientation schedules.
  - [Making Center Tool & Equipment Catalog](https://drive.google.com/file/d/1dF-RaKN6y5C2Pp43RNqfa-ncEDPiNYUA/view?usp=sharing) — Inventory of available laser cutters, 3D printers, woodworking tools, soldering stations, and hand tools.
  - [AMT E-Lab & Physical Computing Studios](https://makingcenter.parsons.edu/facilities/) — Electronics workbenches, oscilloscopes, bench power supplies, and hand fabrication tools.

---

## 6. Materials, Plastics & Mechanical Hardware Suppliers

- **Local NYC & Online Material Vendors**:
  - [Canal Plastics Center](https://www.canalplastic.com/) *(345 Canal St, NYC)* — Cast and extruded acrylic sheet in specialty colors/finishes, *Scigrip 4* acrylic cement, and solvent applicators.
  - [McMaster-Carr](https://www.mcmaster.com/) — Next-day delivery for M2.5/M3 machine screws, hex standoffs, heat-set threaded inserts, raw acrylic/Delrin sheet, and mechanical hardware.
  - [Adafruit Industries](https://www.adafruit.com/) *(NYC-based)* — Panel-mount buttons, switches, bezels, enclosures, and standoffs.
  - [SparkFun Electronics](https://www.sparkfun.com/) — Enclosures, mechanical mounts, and prototyping hardware.
  - [DigiKey](https://www.digikey.com/) & [Mouser Electronics](https://www.mouser.com/) — Industrial enclosures, panel-mount connectors, and switches.
- **Course Hardware Reference**:
  - [Course Materials & Hardware Kit List (BOM)](../files/materials_list.md)
  - [Parts & Hardware Master Reference](../files/parts/parts.md)

---

## 7. Prototyping & Hardware Production Readings

- [Sparkle Labs: Bringing Hardware to Market (PDF)](../files/readings/prototyping/BRINGINGHWTOMARKET.pdf) — End-to-end overview of enclosure tooling, injection molding, and small-batch hardware production.
- [Stephanie Houde & Charles Hill: What Do Prototypes Prototype? (PDF)](../files/readings/prototyping/houde-prototypes.pdf) — Distinguishing Role, Look & Feel, and Implementation prototypes.
- [Mike Kuniavsky: Smart Things Prototyping (Ch 14 PDF)](../files/readings/prototyping/kuniavsky-smartthings-ch14.pdf) — Physical computing form factors and iterative hardware testing.
- [This Is Service Design Doing: Prototyping Methods (Ch 07 PDF)](../files/readings/prototyping/prototyping_tisdd_method_ch07.pdf) & [TISDD Methods Overview (PDF)](../files/readings/prototyping/TISDD_methods.pdf) — Physical mockups and iterative testing.
- [Universal Methods of Design: Simulations (PDF)](../files/readings/prototyping/Universal_Methods_of_Design_Expanded_and_Revised_----_(98._Simulations).pdf)
