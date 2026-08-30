# Blender 3D Cheat Sheet (Primitives & Booleans)

---

## 1. 3D Viewport Navigation

| Action | Mac Shortcut | Windows Shortcut | What It Does |
| :--- | :--- | :--- | :--- |
| <strong>Orbit / Rotate View</strong> | `Middle Mouse Click + Drag` <em>(or 2-finger drag on Trackpad)</em> | `Middle Click + Drag` | Rotates perspective around origin |
| <strong>Pan / Move View</strong> | `Shift + Middle Click + Drag` | `Shift + Middle Click + Drag` | Slides view horizontally/vertically |
| <strong>Zoom In / Out</strong> | `Scroll Wheel` <em>(or pinch trackpad)</em> | `Scroll Wheel` | Zooms focal distance |
| <strong>Focus on Selected</strong> | `Numpad .` <em>(or `View -> Frame Selected`)</em> | `Numpad .` | Centers view directly onto active object |

---

## 2. Object Manipulation (Grab, Rotate, Scale)

<em>Select an object by clicking it (highlighted orange), then press:</em>

- `G` <em>(Grab / Move)</em>: Slides object. Press `X`, `Y`, or `Z` right after to lock movement to a single axis.
- `R` <em>(Rotate)</em>: Rotates object. Press `X`, `Y`, or `Z` to constrain rotation axis.
- `S` <em>(Scale)</em>: Enlarges/shrinks object. Press `X`, `Y`, or `Z` to stretch along one axis.
- `Shift + D` <em>(Duplicate)</em>: Makes an exact copy of the selected object.
- `X` or `Delete`: Deletes active object.

---

## 3. Adding 3D Primitives

Press `Shift + A` → `Mesh`:

- Cube: Enclosures, chassis walls, screen bezels, buttons.
- Cylinder: Dials, knobs, potentiometers, battery compartments, screw holes.
- UV Sphere / Ico Sphere: Ball joints, indicator domes, soft grip pads.
- Torus: O-rings, rotary dials, tactile grip rings.

---

## 4. Constructive Solid Geometry (Boolean Modifier)

<em>Booleans let you build complex physical forms by combining, cutting, or intersecting solid primitives.</em>

1. Select your primary object (e.g. your device main body).
2. Go to the <strong>Modifier Properties</strong> tab on the right sidebar (blue wrench icon 🔧).
3. Click <strong>Add Modifier</strong> → <strong>Generate</strong> → <strong>Boolean</strong>.
4. In the modifier panel, select the operation:
   - Difference (Cutout): Carves the cutter shape out of the main body (e.g. cutting out a screen recess, battery cavity, or USB port hole).
   - Union (Combine): Melds two shapes into one seamless solid shell.
   - Intersect: Keeps only the volume where both objects overlap.
5. In the <strong>Object</strong> field (eyedropper icon), click the cutter object.
6. Hide the cutter object (`H`) in the viewport to inspect your clean cutout!

---

## 5. Exporting for 3D Printing (`.stl` / `.3mf`)

1. Select all components of your final device.
2. Go to <strong>File → Export → Stl (.stl)</strong> (or <strong>3D Manufacturing Format (.3mf)</strong>).
3. Check the box: <strong>Selection Only</strong> in the export panel.
4. Scale: Set to millimeters (<strong>1.0</strong>) and click <strong>Export STL</strong>.
