# Blender 3D Cheat Sheet (Primitives & Booleans)

---

## 1. 3D Viewport Navigation

| Action | Mac Shortcut | Windows Shortcut | What It Does |
| :--- | :--- | :--- | :--- |
| **Orbit / Rotate View** | `Middle Mouse Click + Drag` *(or 2-finger drag on Trackpad)* | `Middle Click + Drag` | Rotates perspective around origin |
| **Pan / Move View** | `Shift + Middle Click + Drag` | `Shift + Middle Click + Drag` | Slides view horizontally/vertically |
| **Zoom In / Out** | `Scroll Wheel` *(or pinch trackpad)* | `Scroll Wheel` | Zooms focal distance |
| **Focus on Selected** | `Numpad .` *(or `View -> Frame Selected`)* | `Numpad .` | Centers view directly onto active object |

---

## 2. Object Manipulation (Grab, Rotate, Scale)

*Select an object by clicking it (highlighted orange), then press:*

- **`G`** (*Grab / Move*): Slides object. Press **`X`**, **`Y`**, or **`Z`** right after to lock movement to a single axis.
- **`R`** (*Rotate*): Rotates object. Press **`X`**, **`Y`**, or **`Z`** to constrain rotation axis.
- **`S`** (*Scale*): Enlarges/shrinks object. Press **`X`**, **`Y`**, or **`Z`** to stretch along one axis.
- **`Shift + D`** (*Duplicate*): Makes an exact copy of the selected object.
- **`X`** or **`Delete`**: Deletes active object.

---

## 3. Adding 3D Primitives

Press **`Shift + A`** $\to$ **`Mesh`**:

- **Cube**: Enclosures, chassis walls, screen bezels, buttons.
- **Cylinder**: Dials, knobs, potentiometers, battery compartments, screw holes.
- **UV Sphere / Ico Sphere**: Ball joints, indicator domes, soft grip pads.
- **Torus**: O-rings, rotary dials, tactile grip rings.

---

## 4. Constructive Solid Geometry (Boolean Modifier)

*Booleans let you build complex physical forms by combining, cutting, or intersecting solid primitives.*

1. Select your primary object (e.g. your device main body).
2. Go to the **Modifier Properties** tab on the right sidebar (blue wrench icon 🔧).
3. Click **Add Modifier** $\to$ **Generate** $\to$ **Boolean**.
4. In the modifier panel, select the operation:
   - **Difference (Cutout)**: Carves the cutter shape out of the main body (e.g. cutting out a screen recess, battery cavity, or USB port hole).
   - **Union (Combine)**: Melds two shapes into one seamless solid shell.
   - **Intersect**: Keeps only the volume where both objects overlap.
5. In the **Object** field (eyedropper icon), click the cutter object.
6. Hide the cutter object (`H`) in the viewport to inspect your clean cutout!

---

## 5. Exporting for 3D Printing (`.stl` / `.3mf`)

1. Select all components of your final device.
2. Go to **File $\to$ Export $\to$ Stl (.stl)** (or **3D Manufacturing Format (.3mf)**).
3. Check the box: **Selection Only** in the export panel.
4. Scale: Set to millimeters (**1.0**) and click **Export STL**.
