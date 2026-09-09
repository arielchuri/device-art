# Miro Circuit Playground: The Secret Flow of Electricity

**Course:** Device Art (Fall 2026)  
**Location:** Miro Canvas First (No Real Parts Until the Grand Finale!)  
**Canvas Status:** Unpublished Draft  

---

## Welcome to the Miro Sandbox

Before we touch any real wires or fragile chips, we are going to play inside **Miro**. 

Think of Miro as our digital sandbox. In Miro, you can make mistakes, plug things in backward, cross wires, and experiment freely—nothing will smoke, get hot, or break!

In this workshop, you will learn the secret language of electricity by dragging, dropping, and connecting vector parts on your Miro board. At the very end of class, once our digital blueprints make complete sense, we will bring them to life with real hardware.

---

## The Big Three: What Actually Is Electricity?

Imagine a giant water park slide:

1. **Voltage (V) — The Push (Water Tower Height)**  
   Voltage is measured in **Volts**. Think of it like the height of a water tower. The higher the tower, the harder the water presses to burst out of the pipe. Voltage is the invisible push that urges electricity forward. Our Raspberry Pi Pico provides a gentle push of **3.3 Volts**.

2. **Current (I) — The Flow (Amount of Water Passing By)**  
   Current is measured in **Amps** (or tiny fractions called **milliamps**, written as **mA**). 1 Amp is like a raging firehose; 1 milliamp (1/1000th of an Amp) is like a tiny trickle through a straw. Current is the actual stream of tiny electric charges rushing through the wire.

3. **Resistance (R) — The Narrow Pipe (The Squeeze)**  
   Resistance is measured in **Ohms** (using the Greek letter **Omega** or **R**). Imagine pinching a water hose with your fingers. The harder you pinch, the harder it is for water to flow through. Resistors are gentle pinch-points that keep current safe and slow so components do not pop.

---

## The Golden Rule: Ohm's Law

All three work together in a simple tug-of-war:

```text
The Push (Volts) = The Flow (Current) x The Squeeze (Resistance)
```

In short:
- If you push harder (**more Volts**), you get **more Flow**.
- If you squeeze harder (**more Resistance / Ohms**), you get **less Flow**.

To find out how much flow you get:

```text
Current (Flow) = Volts (Push) / Resistance (Squeeze)
```

Let us see how this works on our Miro board!

---

## Mission 1: The One-Way Light Bridge (LED & Polarity)

### What is an LED?
**LED** stands for **Light Emitting Diode**.  
Think of an LED like a one-way turnstile at a subway station:
- If you walk through the turnstile the right way (**Forward**), you walk right through and light up!
- If you push against it backward (**Reverse**), the gate slams shut. Zero water/electricity gets through!

An LED has two legs:
- **The Long Leg (Anode, +)**: Friendly to the positive push (+3.3V).
- **The Short Leg (Cathode, -)**: Connects toward ground (GND / 0V).

### The Miro Blueprint
1. Open your Miro board.
2. Drag `solderless_breadboard.svg` onto your workspace.
3. Notice how the breadboard works: inside, metal clips run across the numbered rows (Row 1, Row 2, Row 3...). Any two wires in the same row are holding hands!
4. Drag a **220 Ohm Resistor** onto your board. Place one leg on **Row 5** and the other on **Row 9**.
5. Drag an **LED** onto your board. Put the **Long Leg (+)** on **Row 9** (holding hands with the resistor) and the **Short Leg (-)** on **Row 10**.
6. Connect a **Red wire** from `3V3` to **Row 5**.
7. Connect a **Black wire** from `GND` to **Row 10**.

### Miro Brain Teaser 1: The Flipped Turnstile
- In Miro, flip the LED upside down so the short leg faces Row 9 and the long leg faces Row 10.
- **Question:** Does the turnstile open or stay locked?
- **Answer:** It stays locked! Current drops to 0 mA, and the LED stays dark.

---

## Mission 2: The Energy Toll Booth (LED Colors & Math)

Every LED is also a picky toll booth. Before an LED allows electricity to pass through and create light, it collects an **energy toll** called the **Forward Voltage Drop** ($V_f$).

Different color LEDs have different chemical crystals inside them, so their toll amounts differ:
- **Red LED Toll:** Takes **2.0 Volts**. Easy to pass!
- **Blue LED Toll:** Takes **3.1 Volts**. Very expensive!
- **White LED Toll:** Takes **3.2 Volts**. Almost the entire battery!

### Let Us Do the Math Step-by-Step

Our power source gives us **3.3 Volts** of total push.  
Whatever voltage the LED does not eat gets handed directly to our **220 Ohm resistor**:

```text
Voltage left for Resistor = Total Push (3.3V) - LED Toll
```

Then we find the current using Ohm's Law:

```text
Current (in Amps) = Voltage left / 220 Ohms
Current (in mA)   = Current in Amps x 1000
```

#### 1. The Red LED:
- Toll = 2.0 Volts.
- Leftover push for the resistor:
  $$3.3\text{V} - 2.0\text{V} = 1.3\text{V}$$
- Current flowing through the circuit:
  $$I = \frac{1.3\text{V}}{220\,\Omega} = 0.00591\text{ Amps}$$
- Turn into milliamps (multiply by 1000):
  $$0.00591 \times 1000 = 5.91\text{ mA}$$
- **Result:** Healthy, bright glow!

#### 2. The Blue LED:
- Toll = 3.1 Volts.
- Leftover push for the resistor:
  $$3.3\text{V} - 3.1\text{V} = 0.2\text{V}$$
- Current flowing through the circuit:
  $$I = \frac{0.2\text{V}}{220\,\Omega} = 0.00091\text{ Amps}$$
- In milliamps:
  $$0.00091 \times 1000 = 0.91\text{ mA}$$
- **Result:** Very gentle, dim glow because there was almost no push left for the resistor!

#### 3. The White LED:
- Toll = 3.2 Volts.
- Leftover push for the resistor:
  $$3.3\text{V} - 3.2\text{V} = 0.1\text{V}$$
- Current flowing through the circuit:
  $$I = \frac{0.1\text{V}}{220\,\Omega} = 0.00045\text{ Amps} = 0.45\text{ mA}$$
- **Result:** Whispering dim!

---

## Mission 3: Series vs. Parallel (Conga Line vs. Fork in the Road)

### Part A: The Conga Line (Series)
In a **Series circuit**, components line up single file, like dancers in a conga line. Every single drop of electricity must march through Component 1, then Component 2, then home to Ground.

In Miro, place **Two Red LEDs** in a single line, one after another:
```text
[ 3.3V Push ] ---> [ Resistor ] ---> [ LED 1 ] ---> [ LED 2 ] ---> [ GND ]
```

#### The Math Mystery: Why will they not turn on?
- LED 1 demands a toll of **2.0 Volts**.
- LED 2 also demands a toll of **2.0 Volts**.
- Total toll required:
  $$2.0\text{V} + 2.0\text{V} = 4.0\text{ Volts}$$
- But how much push does our Pico give us? **Only 3.3 Volts!**
- **The Verdict:** 3.3V is smaller than 4.0V. We do not have enough tickets to pay both toll booths! The circuit cannot turn on.

---

### Part B: The Fork in the Road (Parallel)
In a **Parallel circuit**, the wire splits into two separate paths, like a fork in a river.

```text
                   +---> [ Branch A: 220Ω Resistor + Red LED ] ---+
[ 3.3V Push ] ----|                                               |---> [ GND ]
                   +---> [ Branch B: 220Ω Resistor + Red LED ] ---+
```

Each branch gets the full **3.3 Volts** push!
- Branch A draws: **5.91 mA**
- Branch B draws: **5.91 mA**
- Total current leaving the battery:
  $$\text{Total Current} = 5.91\text{ mA} + 5.91\text{ mA} = 11.82\text{ mA}$$

In Miro, connect both branches. Both LEDs light up at full brightness!

---

## Mission 4: The Voltage Divider (The Electric Seesaw)

A **Voltage Divider** is one of the most useful tricks in physical computing. It turns a fixed push (like 3.3V) into any smaller voltage you want, like a seesaw.

### 1. The Volume Knob (Potentiometer)
A potentiometer is a 10,000 Ohm (10k) resistor strip with a sliding metal finger (called a **Wiper**) in the middle.

```text
[ 3.3V Push ] ---> Left Pin
                   Middle Pin (Wiper Output) ---> Multimeter / Sensor pin
[ GND (0V)  ] ---> Right Pin
```

- When the knob is all the way to the left (0%): The wiper touches Ground = **0 Volts**.
- When the knob is dead center (50%): The wiper sits halfway between 3.3V and 0V = **1.65 Volts**.
- When the knob is all the way to the right (100%): The wiper touches full power = **3.3 Volts**.

---

### 2. The Sun Catcher (LDR Photocell Divider)
An **LDR** (Light Dependent Resistor) is a magical light sensor made of special crystal squiggles.
- In bright light, electricity slides through easily (**low resistance, e.g., 1,000 Ohms / 1k**).
- In pitch black darkness, it clogs up tight (**huge resistance, e.g., 50,000 Ohms / 50k**).

We pair the LDR with a **10,000 Ohm (10k) fixed resistor** to make an electric seesaw:

```text
[ 3.3V Push ] ---> [ LDR Sensor ] ---> [ Measurement Point ] ---> [ 10k Fixed Resistor ] ---> [ GND ]
```

The formula for the voltage at the Measurement Point is:

$$\text{Output Voltage} = 3.3\text{V} \times \frac{10,000}{\text{LDR Resistance} + 10,000}$$

#### Math Test 1: In the Bright Sunshine (LDR = 1,000 Ohms / 1k)
$$\text{Total Squeeze} = 1,000 + 10,000 = 11,000\,\Omega$$
$$\text{Output Voltage} = 3.3\text{V} \times \frac{10,000}{11,000} = 3.3 \times 0.909 = 3.00\text{ Volts}$$
**Result:** The voltage jumps up high near 3 Volts!

#### Math Test 2: In Pitch Black Darkness (LDR = 40,000 Ohms / 40k)
$$\text{Total Squeeze} = 40,000 + 10,000 = 50,000\,\Omega$$
$$\text{Output Voltage} = 3.3\text{V} \times \frac{10,000}{50,000} = 3.3 \times 0.20 = 0.66\text{ Volts}$$
**Result:** The voltage drops down low to 0.66 Volts!

By watching this voltage go up and down, a computer (like our Raspberry Pi Pico) can 'see' if the lights in the room are turned on or off.

---


---

## Mission 5: The Magic Doctor's Stethoscope (The Multimeter)

Before you touch real components, how do engineers peek inside wires when electricity is invisible? They use a **Multimeter**!

Think of a multimeter like a doctor's stethoscope. It lets you listen to the heartbeat, blood pressure, and flow of your circuit without guessing.

On the front of your multimeter, you have two probe wires:
- **Black Probe**: Plugs into `COM` (Ground / Home base). It **never moves**!
- **Red Probe**: Plugs into the `V Ω mA` hole.

Here are the 4 superpowers of the multimeter, explained simply:

### Superpower 1: The Magic Beep (Checking Continuity)
- **What it tests**: *"Are these two pieces of metal actually touching?"*
- **Child's Analogy**: Think of it like a metal detector that sings when it finds an open bridge. If the bridge is broken, it stays silent!
- **How to use it in Miro & on the bench**:
  1. Turn the central dial to the **Beep / Diode symbol** (`-|>|-` or speaker waves).
  2. Touch the two probe tips together. **BEEEEEP!** (The bridge is solid!).
  3. Touch Hole 5a and Hole 5e on the same breadboard row. **BEEP!** (Proves all 5 holes in a row hold hands internally).
  4. Touch two completely different rows (Row 5 and Row 6). **Silence!** (Proves breadboard rows are separated like lanes on a highway).

### Superpower 2: Measuring The Push (Volts DC)
- **What it tests**: *"How tall is our water tower? How hard is electricity being pushed?"*
- **Child's Analogy**: Holding a ruler next to the water pipe while the water is running.
- **Rule**: Circuit must be **TURNED ON**.
- **How to use it**:
  1. Turn dial to **DC Volts** (`V=` or `20V`).
  2. Touch probes **across** a component (Black probe on Ground/`-`, Red probe on Power/`+`).
  3. Pico check: Red probe on `3V3` pin, Black probe on `GND` pin $\rightarrow$ Reads **3.30V**!
  4. Red LED check: Across the LED $\rightarrow$ Reads **2.00V** (shows the LED eating its 2 Volt toll!).

### Superpower 3: Measuring The Squeeze (Ohms / Resistance)
- **What it tests**: *"How narrow is this straw? How hard is it to squeeze through?"*
- **Child's Analogy**: Checking the size of a door before anybody tries to walk through.
- **Rule**: **POWER MUST BE COMPLETELY UNPLUGGED!** (Never measure Ohms while power is on, or the meter gets confused and angry!).
- **How to use it**:
  1. Unplug the Pico from your computer.
  2. Turn dial to **Ohms** ($\Omega$ or `2000` / `20k`).
  3. Touch one probe to each leg of your 220 Ohm resistor $\rightarrow$ Reads **~220 $\Omega$**.
  4. Touch one probe to each leg of the LDR sensor, then cover it with your hand $\rightarrow$ Watch the number jump from **1,000 $\Omega$** up to **40,000 $\Omega$**!

### Superpower 4: Measuring The Traffic Flow (Current / Amps / Milliamps)
- **What it tests**: *"How many tiny electric ants are marching through the wire per second?"*
- **Child's Analogy**: A turnstile counter at an amusement park gate. To count the people, every single person has to walk **THROUGH** the turnstile!
- **Rule**: The circuit must be **BROKEN OPEN** and the meter inserted into the line!
- **How to use it**:
  1. Turn dial to **200mA DC**.
  2. Disconnect the wire going into the LED.
  3. Connect Red probe to the power wire, and Black probe to the LED leg.
  4. All electric ants now march straight through the meter before reaching the LED $\rightarrow$ Reads **5.91 mA**!


## Mission 6: The Grand Finale — From Miro to Real Life

Only once every puzzle above has been arranged and solved on your Miro board:

1. **Check Your Miro Map**: Review your breadboard rows and wire colors.
2. **Collect Your Hardware Box**: Pick up your breadboard, Pico, resistors, and LEDs.
3. **Copy the Blueprint**: Place the real components in the exact rows you drew in Miro.
4. **Plug in Power**: Watch your ideas light up in physical reality!
