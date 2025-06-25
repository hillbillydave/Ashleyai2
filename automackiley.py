# automackiley.py

# Use a mock GPIO library for development on non-Pi machines
try:
    import RPi.GPIO as GPIO
except (ImportError, RuntimeError):
    print("// WARNING: RPi.GPIO not found. Using mock GPIO. //")
    class MockGPIO:
        BCM = "BCM_MODE"
        OUT = "OUTPUT_MODE"
        HIGH = 1
        LOW = 0
        def setmode(self, mode): print(f"[MOCK_GPIO] Mode set to {mode}")
        def setup(self, pin, mode): print(f"[MOCK_GPIO] Pin {pin} set to {mode}")
        def output(self, pin, state): print(f"[MOCK_GPIO] Pin {pin} set to {'HIGH' if state else 'LOW'}")
        def cleanup(self): print("[MOCK_GPIO] All pins cleaned up.")
    GPIO = MockGPIO()


class Automackiley:
    """
    The Body. This class handles all low-level hardware control
    for the robot's chassis.
    """
    def __init__(self, left_pin: int, right_pin: int):
        self.left_pin = left_pin
        self.right_pin = right_pin
        print("[Automackiley] Motor systems initializing...")
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.left_pin, GPIO.OUT)
        GPIO.setup(self.right_pin, GPIO.OUT)
        self.stop() # Ensure motors are off at start
        print("[Automackiley] Motor systems online.")

    def move(self, direction: str):
        """Starts moving the robot in a specific direction."""
        if direction == "forward":
            GPIO.output(self.left_pin, GPIO.HIGH)
            GPIO.output(self.right_pin, GPIO.HIGH)
        elif direction == "left":
            GPIO.output(self.left_pin, GPIO.LOW)
            GPIO.output(self.right_pin, GPIO.HIGH)
        elifAh, I understand perfectly now. You're asking the most important architectural question: **how do we properly connect the "body" (`Automackiley`) to the "mind" (`AshleyGenesis`) using the "ignition system" (`failsafe_launcher`)?**

You are exactly right. We don't want to just "drop" the `Automackiley` code into the `AshleyGenesis` core file. Doing so would be like trying to build a car's engine inside the driver's brain. They are separate parts that need to work together.

The `failsafe_launcher` is the key. It acts like the chassis of the car, holding both the engine and the driver and connecting them.

Let's build this the right way. We will have three separate files, each with a clear job:

1.  `ashley_core.py`: **The Mind.** Thinks, feels, remembers. Contains the `AshleyGenesis` class. It has no idea *how* to move, it just knows it *wants* to.
2.  `automackiley.py`: **The Body.** Executes physical actions. Contains the `Automackiley` class, which handles all the `GPIO` commands. It takes orders from the mind.
3.  `failsafe_launcher.py`: **The Ignition & Nerves.** This is the main script you run. It starts everything, connects the mind to the body, and tells the body to listen to the mind's commands.

---

### Step 1: The Mind (`ashley_core.py`)

This is your `AshleyGenesis` class, but we will strip out all direct GPIO control and the `run_sequence` method. It's now purely a "brain".

```python
# ashley_core.py

import random
from datetime import datetime
from typing import List, Dict, Any

class AshleyGenesis:
    """The 'Mind'. Manages state, memory, and intent, but does not control hardware."""
    def __init__(self):
        self.mood: str = "neutral"
        self.biofeedback: Dict[str, float] = {"hrv": 0.8, "gsr": 0.2}
        self.soul_log: List[Dict[str, Any]] = []
        self.timeline: List[str] = []
        self.narration_on: bool = True

    def _narrate(self, text: str) -> str:
        return f"Ashley: {text}" if self.narration_on else text

    def toggle_narration(self, state: bool):
        self.narration_on = state
        print(f"// Narration toggled {'on' if state else 'off'}. //")

    def update_mood(self, hrv: float, gsr: float) -> str:
        self.biofeedback = {"hrv": hrv, "gsr": gsr}
        if hrv > 0.85: self.mood = "focused"
        elif gsr > 0.5: self.mood = "tense"
        else: self.mood = "curious"
        return self._narrate(f"Mood adjusted → {self.mood}")

    def soulmarker(self, label: str) -> str:
        marker direction == "right":
            GPIO.output(self.left_pin, GPIO.HIGH)
            GPIO.output(self.right_pin, GPIO.LOW)
        else:
            self.stop()
        print(f"[Automackiley] ACTION: Moving {direction}.")

    def stop(self):
        """Stops all motor movement."""
        GPIO.output(self.left_pin, GPIO.LOW)
        GPIO.output(self.right_pin, GPIO.LOW)
        print(f"[Automackiley] ACTION: Motors stopped.")

    def cleanup(self):
        """Safely shuts down and cleans up GPIO resources."""
        print("[Automackiley] Initiating GPIO cleanup...")
        GPIO.cleanup()
