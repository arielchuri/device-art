# Lecture: Electricity Fundamentals

**Week:** 3
**Date:** Feb 9
**Duration:** ~45 minutes

## Learning Outcomes

This lecture supports the following learning outcomes:

- **LO 2 - Tools, Materials, Methods:** Write and debug basic Python code and create electronic circuits using microprocessors.

## Overview

This lecture introduces the fundamental principles of electricity needed to design and build safe, functional electronic circuits. Students learn about voltage, current, resistance, and how to read circuit diagrams and calculate component values.

## Key Topics

### Basic Electrical Concepts

#### Voltage (V)
- Definition: electrical potential difference

  Voltage represents the difference in electrical potential energy between two points in a circuit. It's the force that pushes electrons through a conductor, similar to how pressure differences cause water to flow through pipes.

- Measured in Volts (V)

  The unit of voltage is the Volt, named after Alessandro Volta. One volt is defined as the potential difference that will move one coulomb of charge with one joule of energy.

- Analogy: water pressure in pipes

  Just as higher water pressure causes water to flow more forcefully through pipes, higher voltage causes electrons to flow with more energy through a circuit. The voltage difference between two points determines how much energy each electron carries.

- Common voltages: 3.3V, 5V, 9V, 12V, 120V AC

  In electronics projects, we commonly work with low DC voltages like 3.3V (modern microcontrollers), 5V (USB, Arduino), 9V (batteries), and 12V (power supplies). Household AC voltage is 120V in North America, which is dangerous and requires proper training to work with safely.

- Importance in circuit design

  Choosing the correct voltage is critical because components are designed to work within specific voltage ranges. Too little voltage and components won't function; too much and they can be permanently damaged or create safety hazards.

#### Current (I)
- Definition: flow of electrical charge

  Current is the rate at which electric charge flows through a conductor. It represents how many electrons are moving past a given point per unit of time. Current flows from higher voltage to lower voltage.

- Measured in Amperes/Amps (A) or milliamps (mA)

  One ampere equals one coulomb of charge flowing per second. Since many electronic components use very small currents, we often measure in milliamps (1 mA = 0.001 A) or even microamps (1 µA = 0.000001 A).

- Analogy: water flow rate

  If voltage is water pressure, current is the volume of water flowing through the pipe per second. A large pipe can carry more water (higher current), while a narrow pipe restricts flow (lower current).

- Direct current (DC) vs alternating current (AC)

  DC flows in one constant direction, like water flowing steadily through a pipe, and is what batteries provide. AC periodically reverses direction, like water sloshing back and forth, and is what comes from wall outlets. Most electronics use DC internally.

- Current consumption in components

  Every component draws a specific amount of current to operate. LEDs typically draw 10-20mA, microcontrollers might draw 5-200mA depending on activity, and motors can draw several amps. Knowing current draw is essential for selecting appropriate power sources and protecting circuits.

#### Resistance (R)
- Definition: opposition to current flow

  Resistance is the property of a material that restricts the flow of electric current. All materials resist current flow to some degree - conductors have very low resistance while insulators have extremely high resistance.

- Measured in Ohms (Ω)

  The unit of resistance is the Ohm (Ω), named after Georg Ohm. One ohm of resistance will allow one ampere of current to flow when one volt is applied. We also use kilohms (1 kΩ = 1,000 Ω) and megohms (1 MΩ = 1,000,000 Ω) for larger values.

- Resistors and their purpose

  Resistors are components specifically designed to provide a precise amount of resistance. We use them to limit current (protecting LEDs), divide voltage (reading sensors), and set timing in circuits. They're one of the most common components you'll use.

- Variable resistance (potentiometers)

  Potentiometers are adjustable resistors that let you change resistance by turning a knob or sliding a lever. They're used for volume controls, brightness adjustment, and sensor inputs. They typically have three pins: two ends of the resistive element and one wiper that moves along it.

- Resistance in different materials

  Conductors like copper and silver have very low resistance (good for wires), semiconductors like silicon have medium resistance (good for transistors and sensors), and insulators like plastic and rubber have extremely high resistance (good for safety and insulation).

### Ohm's Law
- **V = I × R** (Voltage = Current × Resistance)

  Ohm's Law is the fundamental relationship between voltage, current, and resistance. It states that voltage across a component equals the current through it multiplied by its resistance. This simple equation is the foundation of almost all circuit calculations.

- Solving for different variables

  You can rearrange Ohm's Law to solve for any variable: V = I × R (find voltage), I = V / R (find current), or R = V / I (find resistance). This flexibility makes it incredibly useful for circuit design and troubleshooting.

- Practical calculations for circuit design

  Use Ohm's Law to calculate the right resistor value to limit LED current, determine how much current a circuit will draw from a battery, or find out what voltage drop occurs across a component. It's an essential tool for planning any circuit.

- Using Ohm's law to protect components

  Most components have maximum current ratings that cannot be exceeded. By using Ohm's Law to calculate and limit current with appropriate resistors, you can protect sensitive components like LEDs, microcontroller pins, and sensors from damage.

- Online calculators and tools

  Many websites offer Ohm's Law calculators where you enter two known values and it calculates the third. These are helpful for quick checks and learning, though understanding the underlying math is important for troubleshooting and design.

### Power
- **P = V × I** (Power = Voltage × Current)

  Power is the rate at which electrical energy is consumed or converted. It's calculated by multiplying voltage by current. This tells you how much energy per second a circuit or component uses, which is essential for selecting appropriate power sources and managing heat.

- Measured in Watts (W)

  One watt equals one joule of energy per second. Small electronics might use milliwatts (mW), while household appliances use watts or kilowatts (1 kW = 1,000 W). A typical LED might use 0.1W, while a laptop charger might supply 65W.

- Heat generation in circuits

  When electrical energy flows through resistance, some energy converts to heat. The amount of heat follows the power equation - higher power means more heat. This is why resistors and voltage regulators can get hot, and why proper ventilation is important in electronic enclosures.

- Power ratings of components

  Every component has a maximum power rating indicating how much power it can safely dissipate as heat. Resistors commonly come in 1/4W (0.25W) or 1/2W (0.5W) ratings. Exceeding these ratings can cause components to overheat and fail, sometimes dramatically.

- Battery capacity and power consumption

  Batteries are rated in amp-hours (Ah) or milliamp-hours (mAh), indicating how much current they can supply over time. By calculating your circuit's power consumption, you can estimate battery life. For example, a 1000mAh battery powering a 100mA circuit will last approximately 10 hours.

### Circuit Components

#### Essential Components
- **Resistors:** Limit current, divide voltage

  Resistors are passive components that reduce current flow and drop voltage. They're used to protect LEDs, create voltage dividers for sensors, set timing values, and pull inputs high or low. They come in various tolerances (typically 5% or 1%) and power ratings.

- **LEDs:** Light emitting diodes, polarity matters

  LEDs are semiconductor devices that emit light when current flows through them in the correct direction. They have polarity - the longer leg (anode) connects to positive, the shorter leg (cathode) to negative. They require current-limiting resistors to prevent burnout.

- **Switches:** Control circuit flow

  Switches mechanically connect or disconnect parts of a circuit. Push buttons provide momentary connections, toggle switches provide lasting connections, and DIP switches offer multiple independent channels. They're essential for user input and power control.

- **Batteries:** Power sources

  Batteries convert chemical energy into electrical energy, providing portable power for circuits. Common types include alkaline (1.5V per cell), lithium coin cells (3V), and rechargeable lithium-ion (3.7V nominal). Battery voltage decreases as they discharge.

- **Wires:** Conductors

  Wires are the conductors that connect components together. Solid core wire works well in breadboards and stays in place, while stranded wire is more flexible and better for connections that move. Wire gauge (thickness) determines current-carrying capacity.

- **Breadboards:** Prototyping platforms

  Breadboards let you build circuits without soldering by providing interconnected contact points. The rows along the sides are typically connected vertically (for power/ground distribution), while the interior rows connect horizontally (for component connections). They're perfect for testing and learning.

#### Component Properties
- Polarity (LEDs, electrolytic capacitors, diodes)

  Many components only work when connected in the correct direction. LEDs have a long leg (positive/anode) and short leg (negative/cathode), and a flat edge on the negative side. Reversing polarity can damage components or simply prevent them from working. Always check orientation before powering a circuit.

- Power ratings

  Components are designed to handle specific amounts of power safely. Resistors typically come in 1/8W, 1/4W, or 1/2W ratings - physically larger resistors can handle more power. Exceeding power ratings causes overheating and potential component failure.

- Tolerance

  Tolerance indicates how much a component's actual value might vary from its stated value. A 100Ω resistor with 5% tolerance might actually measure between 95Ω and 105Ω. Gold bands indicate 5% tolerance, silver 10%, while precision resistors might be 1% or better.

- Reading component values

  Resistors use color bands to indicate their value, power rating, and tolerance. There are also printed codes on other components. Learning to read these markings is essential for identifying and selecting the right components. Reference charts and calculators can help initially.

- Datasheets and specifications

  Every component has a datasheet - a technical document from the manufacturer listing specifications, operating conditions, dimensions, and usage examples. Datasheets are your primary resource for understanding exactly how a component works and its limitations.

### Circuit Diagrams
- Schematic symbols for common components

  Circuit diagrams use standardized symbols to represent components: resistors are shown as zigzags or rectangles, LEDs as triangles with arrows, batteries as long and short parallel lines, and switches as breaks in lines. Learning these symbols lets you understand any circuit diagram.

- Reading and drawing schematics

  Schematics show how components connect electrically, not physically. They're drawn for clarity and logical flow rather than physical layout. Reading a schematic involves tracing connections from power through components to ground, understanding what each component does.

- Following current flow

  Current conventionally flows from positive to negative (though electrons physically move the opposite direction). When reading a schematic, trace the path current takes from the power source through components and back to ground to understand circuit operation.

- Ground and power symbols

  Ground (GND) is the 0V reference point, shown as parallel horizontal lines or a triangle. Power sources like VCC, VDD, or +5V are shown as circles, arrows, or labeled connection points. These symbols reduce clutter by avoiding explicit wire connections to power and ground.

- Connection vs crossing wires

  When schematic lines cross, a dot indicates an electrical connection, while no dot means wires simply cross without touching. This distinction is critical for understanding circuit topology. Some styles use wire bridges to show crossings explicitly.

- Labeling conventions

  Components are labeled with designators (R1, R2 for resistors, LED1 for LEDs, SW1 for switches) and their values (220Ω, 5V, etc.). Net names label important connections. Good labeling makes circuits easier to understand, build, and troubleshoot.

### Series vs Parallel Circuits
- **Series:** Components in a line, current same, voltage divides

  In series circuits, components connect end-to-end in a single path. The same current flows through all components, but voltage drops across each one. The sum of voltage drops equals the source voltage. If one component fails open, the entire circuit stops working.

- **Parallel:** Components side-by-side, voltage same, current divides

  In parallel circuits, components connect to the same two points, creating multiple current paths. Each component sees the full voltage, but current divides among paths based on each component's resistance. If one component fails, others continue working.

- When to use each configuration

  Use series when you need voltage division, current limiting for all components, or specific voltage drops. Use parallel when components need the same voltage (like multiple LEDs from one power source), for redundancy, or when you want independent operation of components.

- Calculating total resistance

  Series resistance is straightforward: add all resistances together (R_total = R1 + R2 + R3...). Parallel resistance is trickier: 1/R_total = 1/R1 + 1/R2 + 1/R3... For two resistors in parallel, use R_total = (R1 × R2)/(R1 + R2).

- LED arrays and resistor networks

  Multiple LEDs in series share one resistor but require higher voltage (voltage adds). LEDs in parallel each need their own resistor to ensure even current distribution. Series-parallel combinations optimize voltage and current requirements for arrays.

### Safety

#### Safe Practices
- Low voltage DC is relatively safe (< 50V)

  Voltages below 50V DC are generally considered safe to touch and work with, though they can still cause component damage or create fire hazards if short-circuited. The 3.3V, 5V, 9V, and 12V systems we commonly use pose minimal shock risk but still require proper handling.

- Check polarity before powering

  Always verify power supply polarity matches your circuit before connecting power. Use a multimeter to confirm positive and negative terminals. Reversing polarity can instantly destroy components, particularly ICs and polarized components like LEDs and electrolytic capacitors.

- Use appropriate wire gauges

  Wire must be thick enough to safely carry the current your circuit draws. Too thin wire can overheat, melt insulation, and start fires. For low-current electronics (under 1A), 22-26 AWG is typical, but consult wire gauge charts for higher currents.

- Fuses and circuit protection

  Fuses protect circuits by breaking connection when current exceeds a safe threshold. They're your circuit's safety valve, protecting against shorts and overloads. Replace fuses with the correct rating - never bypass them or use higher ratings.

- Heat sinks for high-power components

  Components dissipating significant power need heat sinks - metal pieces that increase surface area for heat dissipation. Voltage regulators, power transistors, and motor drivers often require heat sinks. Without adequate cooling, components overheat and fail or perform unpredictably.

#### Common Hazards
- Short circuits

  A short circuit creates a very low-resistance path between power and ground, allowing excessive current flow. This can drain batteries instantly, overheat wires, damage power supplies, and potentially start fires. Always double-check connections and watch for stray wire strands before powering circuits.

- Reverse polarity

  Connecting power backward is one of the most common errors, often destroying ICs and polarized components instantly. Many microcontrollers and sensors have no reverse polarity protection. Measure twice, connect once, and mark your power connections clearly.

- Exceeding component ratings

  Every component has maximum ratings for voltage, current, and power. Exceeding these limits causes permanent damage - LEDs burn out, resistors char and smoke, and ICs fail silently or spectacularly. Always check datasheets and add safety margins (design for 80% of maximum ratings).

- Overheating

  Excessive heat degrades components even if they don't fail immediately. Hot components indicate excessive power dissipation - you might need larger resistors, heat sinks, better ventilation, or circuit redesign. Never ignore hot components; they're warning signs of problems.

- Battery safety

  Batteries can deliver enormous currents when short-circuited, causing burns, fires, or explosions, particularly with lithium-ion cells. Never short battery terminals, avoid physical damage, don't mix old and new batteries, and follow proper charging procedures for rechargeables.

## Practical Examples

### LED Circuit Design
- Calculating resistor value for LED

  LEDs need current-limiting resistors because their resistance drops dramatically once conducting, causing runaway current. Calculate required resistance using Ohm's Law: R = (V_source - V_LED) / I_LED. This ensures the LED receives safe operating current without damage.

- Typical LED specifications (20mA, 2V forward voltage)

  Most standard LEDs operate at around 20mA (0.020A) current and have a forward voltage drop of about 2V (red) to 3.5V (blue/white). These values vary by LED type and color, so always check datasheets. High-power LEDs can require 350mA or more and have different voltage drops.

- Example calculation: 5V source, red LED

  For a red LED (2V forward voltage, 20mA) powered by 5V: First find voltage across resistor (5V - 2V = 3V), then calculate resistance needed (3V / 0.020A = 150Ω). This 150Ω resistor will limit current to a safe level.

- (5V - 2V) / 0.020A = 150Ω resistor

  This calculation shows the complete process: subtract the LED's voltage drop from supply voltage to find voltage across the resistor, divide by desired current to find required resistance. The result tells you what resistor value protects your LED.

- Choosing standard resistor values

  Resistors come in standard values (E12 or E24 series), so you won't find every calculated value. Round up to the next standard value - a 220Ω instead of 150Ω reduces current slightly, which is safe. Rounding down could exceed maximum current. Common standard values include 100, 220, 330, 470, 1k, 2.2k, 10k ohms.

### Button Input Circuit
- Pull-up vs pull-down resistors

  Digital inputs need defined states (HIGH or LOW) and can't be left "floating" or disconnected. Pull-up resistors connect the input to voltage (making it HIGH when button is open), while pull-down resistors connect to ground (making it LOW when open). The button switches to the opposite state when pressed.

- Debouncing concepts

  Mechanical switches don't close cleanly - they "bounce" making rapid contact multiple times over several milliseconds. This causes microcontrollers to read multiple button presses from one physical press. Debouncing (in software with delays or in hardware with capacitors) filters out these bounces.

- Reading digital input states

  Microcontrollers read inputs as HIGH (typically > 2V) or LOW (typically < 0.8V). With a pull-up resistor, an open button reads HIGH and closed button reads LOW. With pull-down, it's reversed. Software can detect when the state changes to trigger actions.

- Typical resistance values (10kΩ)

  Pull-up and pull-down resistors typically use 10kΩ - high enough to minimize power consumption when the button closes, but low enough to override noise and define clear logic levels. Some microcontrollers have internal pull-ups (20-50kΩ) that can be enabled in software, eliminating external resistors.

### Sensor Circuits
- Voltage dividers

  A voltage divider uses two resistors in series to create a specific output voltage between them. The output voltage is V_out = V_in × (R2/(R1+R2)). This technique is essential for reading variable resistance sensors and scaling voltages to safe levels for analog inputs.

- Reading analog values

  Microcontrollers can read voltage levels through analog-to-digital converters (ADCs), typically measuring 0-5V or 0-3.3V with 10-bit resolution (1024 steps). This lets you read sensor values as numbers proportional to voltage, enabling measurement of light, temperature, position, and many other physical quantities.

- Variable resistance sensors

  Many sensors work by changing resistance based on physical conditions: photoresistors change with light, thermistors with temperature, flex sensors with bending, and force-sensitive resistors with pressure. Use them in voltage divider circuits to convert resistance changes to voltage changes your microcontroller can read.

- Signal conditioning

  Raw sensor signals often need conditioning before microcontroller input: amplification for weak signals, filtering to remove noise, offset adjustment to match input range, or linearization to correct non-linear sensor responses. Simple conditioning uses operational amplifiers and passive components.

## Key Questions

- Why do LEDs need current-limiting resistors?
- What happens if you exceed a component's rating?
- How do you calculate the right resistor value?
- When would you use series vs parallel?
- How do you read a circuit diagram?
- What's the difference between voltage and current?

## Activities

### In-Class Demonstrations
- Multimeter usage (measuring V, I, R)

  Demonstrate how to use a multimeter in voltage mode (parallel to component), current mode (in series with circuit - breaking the connection), and resistance mode (power off, component isolated). Show auto-ranging versus manual range selection and proper probe placement.

- Building simple LED circuit on breadboard

  Build an LED circuit live, talking through each step: identifying breadboard connections, placing components, calculating resistor value, checking polarity, verifying connections, then powering up. Make intentional errors and fix them to show troubleshooting process.

- Showing series and parallel configurations

  Build both series and parallel LED circuits, measuring voltage and current at different points to demonstrate how they divide. Show what happens when one LED fails in each configuration - series breaks everything, parallel keeps others working.

- Circuit troubleshooting demonstration

  Create common problems (reversed LED, wrong resistor value, loose connection, short circuit) and demonstrate systematic troubleshooting: visual inspection, checking power, measuring voltages, verifying continuity, and logical deduction based on symptoms.

- Reading resistor color codes

  Show physical resistors while explaining the color band system: first two bands are digits, third is multiplier, fourth is tolerance. Practice with multiple resistors and verify with multimeter measurements. Distribute reference charts for students.

### Hands-On Workshop
- Following lecture: Basic circuits workshop

  Immediately following the lecture, students move into hands-on workshop time where they apply concepts just learned. This immediate application reinforces understanding and reveals misconceptions while support is available.

- Students build their first circuits

  Students follow instructions to build basic LED circuits, button input circuits, and simple sensor circuits. Starting with guided instructions builds confidence before moving to independent design. Provide clear diagrams and step-by-step procedures.

- Practice with breadboards

  Students learn breadboard topology by building circuits: understanding row and column connections, using power rails, organizing layouts clearly, and developing good prototyping habits. Hands-on practice is essential for understanding the physical implementation of schematics.

- Use multimeters to measure values

  Students practice measuring voltages at different points, verifying component values, and checking for continuity. This hands-on measurement experience builds troubleshooting skills and confirms theoretical calculations with real-world measurements.

- Troubleshoot common problems

  Intentionally introduce problems (or let natural mistakes occur) and guide students through systematic troubleshooting. This teaches the debugging mindset essential for independent work: careful observation, hypothesis formation, testing, and methodical problem-solving.

## Calculations Students Should Master

1. Ohm's Law (V = I × R)

   Students must be able to calculate any of the three variables given the other two, and rearrange the formula correctly. This is the foundation for all circuit calculations.

2. Power calculation (P = V × I)

   Students should calculate power consumption to select appropriately rated components and estimate battery life. They should also understand the heat implications of power dissipation.

3. LED resistor calculation

   Given supply voltage, LED forward voltage, and desired current, students must calculate the correct current-limiting resistor value. This is one of the most common practical calculations they'll use.

4. Series resistance (R_total = R1 + R2 + ...)

   Students should quickly calculate total resistance of series resistor networks and understand that resistances simply add in series. This applies to voltage dividers and current-limiting applications.

5. Parallel resistance (1/R_total = 1/R1 + 1/R2 + ...)

   Students need to calculate parallel resistance using the reciprocal formula, including the simplified version for two resistors: R_total = (R1 × R2)/(R1 + R2). Parallel resistance is always less than the smallest resistor.

6. Voltage divider calculations

   Students should calculate output voltage of voltage dividers using V_out = V_in × (R2/(R1+R2)). This is essential for sensor circuits and understanding how voltage distributes across series resistances.

## Connections to Course

- Immediately applied in Circuit Prototyping Demo

  Concepts from this lecture are demonstrated in the same class session through live circuit building, providing immediate practical context for theoretical concepts.

- Practiced in Basic Circuits Workshop

  Students get hands-on practice building and measuring circuits immediately after lecture, reinforcing learning through direct application and experimentation.

- Circuit Plan assignment (due Week 4)

  Students apply these principles by designing their own circuits, calculating component values, and creating schematics. This assignment assesses their understanding of fundamental electrical concepts.

- Foundation for microcontroller integration

  Understanding electricity is essential before connecting sensors and outputs to microcontrollers. These basics protect microcontroller pins and enable proper interfacing with external components.

- Essential for Final Project

  Final projects require students to design and build circuits safely and effectively. The electrical fundamentals from this lecture are the foundation for all physical aspects of their projects.

- Building on programming knowledge

  Just as programming has syntax and logic, electricity has rules and relationships. Students can leverage their understanding of cause-and-effect from programming to understand how electrical components interact.

## Resources

### Online Resources
- Electronics tutorials (SparkFun, Adafruit, Electronics Club)

  These websites offer excellent free tutorials on electronics basics, component guides, and project ideas. SparkFun and Adafruit are particularly good for beginner-friendly explanations with practical examples.

- Ohm's law calculators

  Online calculators let you enter any two values (voltage, current, resistance) and calculate the third, plus power. Great for quick checks and verification, though understanding the underlying math remains important.

- Resistor color code calculators

  Web-based tools where you select the color bands and get the resistance value, or vice versa. Helpful while learning the color code system, though with practice you'll memorize common values.

- Circuit simulation tools (Tinkercad Circuits, Falstad)

  Simulators let you build and test circuits virtually before building physically. Tinkercad Circuits is beginner-friendly with visual breadboard layout, while Falstad offers detailed electrical behavior visualization. Great for safe experimentation.

- Component datasheets

  Manufacturers publish detailed specifications for every component. Find datasheets through component distributors (Digi-Key, Mouser, SparkFun) or direct from manufacturers. Learning to read datasheets is an essential engineering skill.

### Tools
- Multimeters

  Essential for measuring voltage, current, and resistance. Even basic multimeters are incredibly useful. Auto-ranging models are easier for beginners. Students should have access to multimeters during all hands-on work.

- Breadboards

  Solderless breadboards are the primary prototyping platform for learning electronics. Full-size breadboards (830 connection points) work well for class projects. Understanding breadboard topology is essential for circuit building.

- Wire strippers

  Proper wire strippers make clean, consistent wire preparations. Adjustable strippers work with multiple wire gauges. Clean wire ends ensure reliable breadboard connections. This is a basic tool that students will use constantly.

- Component kits

  Starter kits containing resistors, LEDs, buttons, and basic components let students experiment freely. Having components readily available encourages exploration and reduces barriers to trying ideas.

- Power supplies

  Bench power supplies provide adjustable, stable voltage and current limiting for safe experimentation. USB power (5V) or battery packs work well for basic projects. Wall adapters with appropriate voltage/current ratings are cost-effective alternatives.

### Course Materials
- electricity_intro directory

  Course repository contains dedicated materials for this lecture including code examples, reference sheets, and practice problems. Students should have access to this directory for reference during and after class.

- Component reference guides

  Provide printable or digital quick-reference sheets showing component symbols, typical values, color codes, and common applications. These reduce cognitive load while students are learning and building.

- Circuit examples

  Include well-documented example circuits with schematics, breadboard layouts, calculations, and explanations. Students can study these examples to understand design thinking and best practices.

- Troubleshooting flowcharts

  Visual guides that walk through systematic debugging processes: "LED not lighting? Check power → Check polarity → Check resistor value → Measure voltage..." These teach problem-solving methodology.

## Assessment

Students demonstrate understanding through:

- Circuit Plan assignment (due Week 4)

  Students design a circuit for their project including schematics, component calculations, and parts lists. This demonstrates their ability to apply electrical principles to original designs.

- Basic Circuits Workshop participation

  Active participation in hands-on workshop shows engagement with practical skills. Observe students' ability to build circuits, use tools properly, and troubleshoot problems independently.

- Successful circuit prototyping

  As students progress through the course, their ability to build working circuits demonstrates practical understanding. Success comes from applying theoretical knowledge to physical implementations.

- Proper component selection for projects

  Choosing appropriate components (correct resistor values, adequate power ratings, proper voltage levels) for their projects shows understanding of electrical principles and safety considerations.

- Safe practices in lab work

  Consistently checking polarity, calculating values before building, using tools correctly, and following safety procedures demonstrates professional habits and deep understanding of potential hazards.

## Tips for Teaching

- Use water/plumbing analogies consistently

  The water analogy (voltage = pressure, current = flow, resistance = pipe diameter) provides intuitive understanding of abstract electrical concepts. Use it consistently throughout the lecture to build on students' existing mental models.

- Do live calculations with real numbers

  Work through Ohm's Law and other calculations in real-time using actual component values. Show your thinking process, including rounding to standard values. This demystifies the math and shows it's not intimidating.

- Show real components while discussing them

  Hold up physical resistors, LEDs, switches as you discuss them. Pass them around if class size allows. Connecting abstract concepts to tangible objects aids learning and memory.

- Demonstrate with multimeter measurements

  Measure voltages and resistances live during lecture. Show that measured values match (or explain why they don't) calculated values. This validates theory with observable reality.

- Build circuits in real-time

  Build circuits on a visualizer or document camera so students see the process. Talk through your decisions, show how you check work, and demonstrate that building circuits is a methodical, learnable skill.

- Intentionally create errors and troubleshoot

  Deliberately make common mistakes (reversed LED, wrong resistor value) and troubleshoot them. This normalizes errors as learning opportunities and teaches debugging methodology.

- Emphasize safety without creating fear

  Present safety information matter-of-factly: explain actual risks (shorts can cause fires, reversed polarity damages components) without exaggeration. Students should be cautious but confident, not afraid to experiment.

- Connect to their Python programming knowledge

  Draw parallels: "Just like a function takes inputs and produces outputs, a resistor takes voltage and current and produces a specific voltage drop." Leverage their existing computational thinking.

- Provide reference sheets and charts

  Give students printed or digital resources they can use while working: Ohm's Law triangle, resistor color code chart, common component values, breadboard topology diagram. Reduce memorization burden.

- Make resources available for review

  Post lecture slides, video recordings if available, and supplementary materials for student review. Electricity concepts may need multiple exposures to fully understand.

- Prepare for different math comfort levels

  Some students will grasp calculations immediately; others will struggle. Have extra practice problems ready, offer office hours for additional help, and consider peer tutoring opportunities.

- Encourage questions and experimentation

  Create a classroom culture where questions are welcomed and experimentation is encouraged. "What if" questions lead to deeper understanding. Provide components for students to try ideas safely.

- Link to previous knowledge (batteries, switches, light bulbs)

  Connect to experiences students already have: "You've changed batteries - you knew polarity mattered. Now let's understand why." Building on familiar concepts makes new information more accessible.
