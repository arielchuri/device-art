#!/usr/bin/env python3
"""
Device Art: Speculative Object In-Class Exercise Prompt Generator
Generates lived, atmospheric, and speculative prompts for in-class Miro mapping.
"""

import random, sys

# =========================================================================
# POETIC & SPECULATIVE PARAMETER POOLS
# =========================================================================

WORLDBUILDING_WORLDS = [
    # Dystopian / Algorithmic / Surveillance
    "Holographic billboards along the avenue call out to you by your childhood nickname, pricing food based on your current pulse rate.",
    "Raw synthetic intelligence and high-bandwidth computation are luxury commodities, rationed by weekly wealth tier.",
    "Municipal biometric scopes sweep the subway station, flagging anyone whose skin response indicates mild agitation or fatigue.",
    "Quietness is a paid subscription service; without it, ambient commercial audio is piped directly into public sidewalks.",
    "Every glass surface in your apartment is an active display that dims only when you close your eyes.",
    "Brainwave monitoring headbands are required attire during all public transit commutes to ensure passive compliance.",
    
    # Utopian / Ecological / Communal
    "Streetlights in your neighborhood only illuminate when a pollinator or nocturnal animal is within three meters.",
    "Community micro-grids trade surplus rooftop solar battery power like homegrown sourdough starters.",
    "Public park benches subtly warm themselves and hum low harmonic tones to soothe overtired strangers.",
    "Soil quality sensors in the neighborhood garden broadcast communal hydration tasks directly to morning walkers.",
    "An underground pneumatic tube network delivers warm, shared tea kettles to anyone working past midnight.",
    "A distributed mesh of citizen air quality beacons automatically redirects bicycle traffic away from heavy smog.",

    # Domestic / Intimate Realism
    "An heirloom radio left behind by a family member only catches static from places where nobody is currently speaking.",
    "A small mechanical desktop instrument grows slightly colder to the touch each time you open an unread message.",
    "The apartment building's shared laundry room has a coin slot that accepts only pressed copper tokens and whispered favors.",
    "A bedside lamp that stays awake as long as you toss and turn, refusing to let you read in total isolation.",
    "Two roommates try to navigate a cramped kitchen together without their elbows ever brushing."
]

LIVED_HUMAN_TENSIONS = [
    "You want to walk to the corner store without being identified, categorized, or greeted by an automated voice.",
    "You need to pass a private message to a neighbor without leaving a single digital trace on the local mesh.",
    "You are pretending to be calm during a routine checkpoint while your adrenaline is secretly hammering against your ribs.",
    "You want to share the quiet warmth of an autumn afternoon with someone living three thousand miles away, without sending a screen notification or photo.",
    "You have ten minutes before your shift starts and need to erase all visible traces of exhaustion from your face.",
    "You need to make a difficult personal decision before the kitchen kettle finishes boiling, refusing to consult an algorithmic prediction.",
    "You want to feel physically anchored during sudden panic without anyone around you noticing.",
    "You want to know if an unseen stranger is standing uncomfortably close behind you in the crowded elevator.",
    "You are trying to resist the compulsive, unconscious urge to reach for a glass screen in your pocket."
]

MATERIAL_OBJECT_RITUALS = [
    "The device must fit entirely inside the cuff of a jacket, operated purely by clenching and releasing your fist.",
    "It has no screen and no battery; it only functions when warmed by human body heat or exposed to direct sunlight.",
    "To activate it, you must flip it completely upside down and wait for three quiet mechanical clicks.",
    "It communicates through subtle shifts in physical weight, rolling a small brass balance ball inside its wooden hull.",
    "When its purpose is finished, it gently prints a single line of paper receipt and locks its hinge until tomorrow.",
    "It rests between two people on a table, requiring both individuals to touch its pads simultaneously before it unlocks.",
    "It cannot emit any audible sound; feedback must rely entirely on subtle thermal warmth and tactile vibrations.",
    "It is operated by blowing a steady stream of breath across its slotted intake vents.",
    "It must be worn on the body and requires a deliberate two-handed squeeze to trigger its primary state."
]

def generate_prompt(index=1):
    world = random.choice(WORLDBUILDING_WORLDS)
    tension = random.choice(LIVED_HUMAN_TENSIONS)
    ritual = random.choice(MATERIAL_OBJECT_RITUALS)
    
    return f"""━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SPECULATIVE DEVICE PROMPT #{index:02d}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[WORLD]
{world}

[HUMAN TENSION]
{tension}

[OBJECT RITUAL]
{ritual}
"""

def main():
    count = 1
    if len(sys.argv) > 1:
        try:
            count = int(sys.argv[1])
        except ValueError:
            count = 1
            
    print(f"\n✨ Generated {count} Speculative Prompt(s) for Device Art Studio:\n")
    for i in range(count):
        print(generate_prompt(i + 1))

if __name__ == "__main__":
    main()
