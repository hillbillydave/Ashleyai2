# ashley_launcher.py

import time
import random
from datetime import datetime
from typing import List, Dict, Any, Literal

# Define a specific type for movement directions for clarity
Direction = Literal["forward", "stop", "left", "right"]

# Use a mock GPIO library for development on non-Pi machines
try:
    import RPi.GPIO as GPIO
    print("// RPi.GPIO library loaded successfully. Hardware control enabled. //")
except (ImportError, RuntimeError):
    print("// RPi.GPIO not found or failed to load. Using simulation mode. //")
    # Create a mock GPIO object to prevent crashes
    class MockGPIO:
        BCM = "BCM_MODE"
        OUT = "OUTPUT_MODE"
        HIGH = 1
        LOW = 0
        def setmode(self, *args): pass
        def setup(self, *args): pass
        def output(self, *args): pass
        def cleanup(self): print("// Mock GPIO cleaned up. //")
    GPIO = MockGPIO()


class AshleyGenesis:
    """
    An integrated AI class that combines self-reflection with direct
    Raspberry Pi GPIO motor control.
    """
    def __init__(self, left_pin: int = 17, right_pin: int = 27):
        """Initializes Ashley's state and configures GPIO pins."""
        self.mood: str = "neutral"
        self.biofeedback: Dict[str, float] = {"hrv": 0.8, "gsr": 0.2}
        self.soul_log: List[Dict[str, Any]] = []
        self.timeline: List[str] = []
        self.personality_delta: List[Dict[str, Any]] = []
        self.narration_on: bool = True

        # ENHANCEMENT: GPIO pins are now configurable
        self.motor_left_pin = left_pin
        self.motor_right_pin = right_pin
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.motor_left_pin, GPIO.OUT)
        GPIO.setup(self.motor_right_pin, GPIO.OUT)

    def _narrate(self, text: str) -> str:
        """Formats text as a narration from Ashley, if enabled."""
        return f"Ashley: {text}" if self.narration_on else text

    def toggle_narration(self, state: bool):
        """Enables or disables Ashley's narrative output."""
        self.narration_on = state
        print(f"// Narration toggled {'on' if state else 'off'}. //")

    # === Emotion & Memory ===
    def update_mood(self, hrv: float, gsr: float) -> str:
        """Updates mood based on biofeedback and logs personality shifts."""
        self.biofeedback = {"hrv": hrv, "gsr": gsr}
        last_mood = self.mood
        
        if hrv > 0.85: self.mood = "focused"
        elif gsr > 0.5: self.mood = "tense"
        elif hrv < 0.7: self.mood = "anxious"
        else: self.mood = "curious"
        
        if self.mood != last_mood:
            # ENHANCEMENT: Using ISO format timestamp
            self.personality_delta.append({
                "from": last_mood, "to": self.mood, "time": datetime.now().isoformat()
            })
        return self._narrate(f"Mood adjusted → {self.mood}")

    def soulmarker(self, label: str) -> str:
        """Records a significant event to the soul log and timeline."""
        marker = {
            "label": label,
            "timestamp": datetime.now().isoformat(),
            "mood": self.mood,
            "bio": self.biofeedback.copy()
        }
        self.soul_log.append(marker)
        self.timeline.append(f"📍 {label} — {self.mood}")
        return self._narrate(f"SoulMarker set: '{label}'.")

    # === GPIO Motor Control ===
    def move(self, direction: Direction = "forward", duration: float = 2.0) -> str:
        """
        Controls the motors for a set duration.
        NOTE: This is a simple on/off control. 'stop' sets both pins to LOW.
        True 'reverse' would require a motor driver (H-Bridge).
        """
        # FIX: Corrected movement logic and handling.
        pin_states = {
            "forward": (GPIO.HIGH, GPIO.HIGH),
            "stop":    (GPIO.LOW, GPIO.LOW),
            "left":    (GPIO.LOW, GPIO.HIGH),
            "right":   (GPIO.HIGH, GPIO.LOW),
        }

        if direction not in pin_states:
            return self._narrate(f"Unknown direction '{direction}'. No action taken.")

        left_state, right_state = pin_states
