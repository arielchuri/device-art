# Assignment 04: 3D Modeling Your Speculative Device (Blender Primitives & Booleans)

- **Due Date**: Wednesday, September 9, 2026 at 7:00 PM
- **Points**: 20 Points
- **Submission Type**: Online File Upload (`.blend` file and exported `.stl` / `.3mf` print file) + Image Renders / Screenshots
- **Quick Reference**: 📖 **[Blender 3D Cheat Sheet (Primitives & Booleans)](https://github.com/arielchuri/device-art/blob/main/canvas/files/cheatsheets/blender_cheatsheet.md)**

---

## Assignment Overview

In our previous studio exercise, you generated a speculative device narrative and mapped its interaction architecture in Miro. Now, you will translate that 2D schematic diagram into a tangible **3D physical enclosure** in **Blender**.

To develop strong industrial design modeling habits and prepare for 3D printing, you must build your enclosure using **only 3D Primitives and Boolean Modifiers** (Constructive Solid Geometry).

---

## 🛠 Core Modeling Constraints:

1. **Primitives Only**: Build every component using basic geometric shapes (`Shift + A -> Mesh` $\to$ *Cube, Cylinder, UV Sphere, Torus, Cone*).
2. **Boolean Operations (CSG)**:
   * **Difference (Carving)**: Cut out screen bezels, port sockets (USB-C, audio jack), button recesses, battery bays, and sensor windows.
   * **Union (Combining)**: Fuse structural grips, mounting bosses, and tactile knobs into the main chassis.
3. **Ergonomics & Scale**: Model the object to human handheld scale (approx. 60mm – 150mm dimensions).
4. **Form Follows Prompt**: The physical silhouette, weight distribution, and tactile controls must directly reflect the lived tension and object ritual from your prompt generator vignette.

---

## Step-by-Step Instructions

### Step 1: Download & Install Blender
If you don't already have it installed, download the free, open-source 3D suite:
* **[blender.org/download](https://www.blender.org/download/)** (macOS Apple Silicon/Intel or Windows).

---

### Step 2: Model Your Device Enclosure
1. **Main Body Shell**: Start with a scaled cube or cylinder.
2. **Component Cutouts**: Create cutter objects (cubes for rectangular screens, cylinders for knobs/buttons/ports) and apply **Boolean Modifiers** (`Difference`) to carve out their recesses.
3. **Controls & Actuation**: Add buttons, knobs, dials, sliders, or touch surfaces seated inside their carved sockets.

---

### Step 3: Export for 3D Printing & Capture Screenshots
1. **Save Blender File**: Save your work as `YourName_SpeculativeDevice.blend`.
2. **Export 3D Print File**: Select your model $\to$ **File $\to$ Export $\to$ Stl (.stl)** or **.3mf**.
3. **Capture 3 Viewport Screenshots**:
   * Perspective / Isometric View
   * Front View
   * Top / Detail View (showing buttons and port recesses)

---

## 📝 How to Submit on Canvas:
Submit the following items:
1. Your native **`.blend` file**.
2. Your exported **`.stl` or `.3mf`** 3D print file.
3. **3 Screenshots / Renders** (JPG or PNG) showing different angles of your modeled device.
4. In the text comment box, include the **3-layer prompt** you used to design the device (*The World, The Human Tension, The Object Ritual*).

---

## Rubric Point Breakdown

| Criterion | Description | Points |
| :--- | :--- | :---: |
| **Form Execution via Primitives & Booleans** | Effective use of geometric primitives and clean Boolean cuts/unions without messy geometry | 8 pts |
| **Interaction Details & Control Recesses** | Clear physical accommodations for buttons, dials, screens, sensor windows, and cable ports | 6 pts |
| **Alignment with Speculative Narrative** | Physical form, ergonomics, and affordances clearly embody the generated prompt | 4 pts |
| **File Preparation & 3D Print Export** | Proper `.blend` file, valid `.stl`/`.3mf` export, and 3 clean perspective screenshots | 2 pts |
| **Total** | | **20 pts** |
