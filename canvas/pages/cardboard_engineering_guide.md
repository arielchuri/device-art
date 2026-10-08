# Cardboard Engineering & Rapid Enclosure Prototyping

---

## 1. Overview & Philosophy

Building physical housings for electronics bridges the gap between a fragile breadboard circuit and a cohesive, tangible artwork. Rapid prototyping with paper, chipboard, and corrugated cardboard allows quick iteration of form, scale, ergonomics, and component placement before committing to final fabrication methods.

### Design Philosophy
- **Form follows function and interaction**: Let user grip, sensor visibility, and cable routing dictate structural volumes.
- **Fail fast and iterate**: Build low-stakes mockups in paper and scrap board to discover tolerance errors early.
- **Measure with calipers**: Account for component heights, connector clearances, and wall thicknesses.

---

## 2. Materials & Properties

| Material | Thickness / Density | Primary Use Case | Joining Techniques |
| :--- | :--- | :--- | :--- |
| **Corrugated Cardboard (E/B Flute)** | 1.5mm - 3.0mm (Fluted) | Structural chassis, outer load-bearing shells | Hot glue, tab-and-slot, PVA |
| **Chipboard / Greyboard** | 1.0mm - 2.0mm (Solid) | Flat bezel panels, faceplates, clean geometric planes | PVA glue, double-sided tape, corner tape |
| **Mat Board / Museum Board** | 1.2mm - 1.5mm (Rigid) | High-finish facades, tight score-and-fold enclosures | Bookbinding glue, craft adhesive |
| **Foam Core** | 3.0mm - 5.0mm (Sandwich) | Lightweight internal partitioning and spacers | Low-temp hot glue, craft pins |

### Structural Principles
- **Flute / Grain Direction**: Corrugated board bends easily parallel to flutes and resists bending perpendicular to flutes. Orient flutes vertically for load-bearing walls.
- **Scoring vs. Cutting**:
  - *Full Cut*: Passes through all layers to separate pieces.
  - *Score*: Slices only the top paper liner, allowing a crisp 90-degree or curved fold without splitting.
- **Layering (Lamination)**: Glue multiple sheets with opposing grain directions to create rigid, warp-resistant panels.

---

## 3. Planning & Drafting (2D to 3D)

### Net Patterns (Unfolded 3D Boxes)
Before cutting, draft the unfolded geometry (the "net") flat on cardboard:
1. **Base Plate**: Matches the footprint of your breadboard/Pico with 5-10mm perimeter margin.
2. **Side Walls**: Height must exceed the tallest component (Pico + headers + display + jumper wire loops).
3. **Folding Tabs**: Add 10-15mm glue tabs along corner edges to secure joints.
4. **Material Thickness Allowance**: When folding 2mm cardboard, add $2 \times \text{thickness}$ (4mm) to outer panels so corners meet cleanly.

### Component Cutouts & Tolerances
- **OLED Displays (SSD1306)**: Measure screen viewing window ($128 \times 64$ is approx. $25 \times 14\text{ mm}$). Cut window slightly undersized so bezel conceals PCB edges.
- **Pushbuttons & Rotary Potentiometers**: Drill/punch circular apertures. Use washer and hex nut to panel-mount directly through chipboard.
- **USB-C / Micro-USB Port**: Cut an oval or rectangular relief slot ($12 \times 7\text{ mm}$) centered on the Pico connector to allow cable plugging without straining the board.
- **Ultrasonic Sensors (HC-SR04)**: Twin 16mm circular cutouts spaced 26mm center-to-center for transducer barrels.

---

## 4. Tools & Craft Techniques

### Essential Tooling
- **Cutting**: Utility knife / X-Acto (#11 blade for detail, heavy-duty utility knife for corrugated board). Always cut against a steel safety ruler on a self-healing mat.
- **Multiple Light Passes**: Make 2 to 3 light scoring cuts rather than forcing a heavy cut in one pass. This prevents edge crushing and blade wander.
- **Adhesives**:
  - *Hot Glue*: Fast setting, excellent gap-filling for interior bracing.
  - *PVA / Wood Glue*: Creates permanent, high-strength bonds on porous paper fibers (clamp or tape while curing).
  - *Removable Mounting*: Velcro dots or adhesive standoffs for electronics that must be removed for reprogramming.

---

## 5. Prototyping Stages

```
[ Stage 1: Paper Sketch Model ]
  └── Quick 1:1 paper cutout to test ergonomics and physical hand feel.

[ Stage 2: Rough Cardboard Mockup ]
  └── Sized to actual electronics. Verify component fit, wire clearances, and button access.

[ Stage 3: Refined Functional Enclosure ]
  └── Precise cutouts, panel joinery, battery access hatch, and clean edge finishing.

[ Stage 4: Digital CAD / Final Material (Optional) ]
  └── Vectorize for laser-cut acrylic / wood or model in Blender/Fusion 360 for 3D printing.
```

---

## 6. Electronics Integration & Wire Management

1. **Strain Relief**: Fasten cables with tape or zip-tie anchors near ports to prevent solder joints and breadboard wires from pulling loose during handling.
2. **Removable Access Panels**: Incorporate a friction-fit lid, magnetic clasp, or sliding bottom tray so you can access the Pico REPL and wiring without destroying the enclosure.
3. **Insulation**: Cardboard is non-conductive, but ensure exposed solder joints cannot touch metal fasteners or conductive foil linings.
