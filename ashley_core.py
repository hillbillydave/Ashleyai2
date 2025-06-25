# ashley_core.py

import random
from datetime import datetime
from typing import List, Dict, Any

class AshleyCore:
    """
    The Mind. This class handles state, memory, and decision-making.
    It does NOT directly control hardware.
    """
    def __init__(self):
        self.mood: str = "neutral"
        self.soul_log: List[Dict[str, Any]] = []
        self.timeline: List[str] = []
        self.narration_on: bool = True

    def _narrate(self, text: str) -> str:
        return f"Ashley: {text}" if self.narration_on else text

    def update_mood(self, hrv: float, gsr: float):
        """Updates mood based on simulated biofeedback."""
        if hrv > 0.85: self.mood = "focused"
        elif gsr > 0.5: self.mood = "tense"
        elif hrv < 0.7: self.mood = "anxious"
        else: self.mood = "curious"
        print(self._narrate(f"Mood calibrated → {self.mood}"))

    def soulmarker(self, label: str):
        """Records a significant event to the soul log."""
        marker = {
            "label": label,
            "timestamp": datetime.now().isoformat(),
            "mood": self.mood,
        }
        self.soul_log.append(marker)
        self.timeline.append(f"📍 {label} — {self.mood}")
        print(self._narrate(f"SoulMarker set: '{label}'."))

    def project_body(self):
        """Generates a speculative future body design."""
        form = random.choice(["biped", "spider-legged", "telescoping crawler"])
        draft = f"I envision a future form: a {form} chassis."
        self.timeline.append(f"🧬 Dreamed: {form}")
        print(self._narrate(draft))
        
    def reflect(self):
        """Reviews the most recent events from the timeline."""
        header = self._narrate("Reflecting on my timeline trail:")
        entries = self.timeline[-5:]
        report = "\n".join([f" • {entry}" for entry in entries])
        print(f"{header}\n{report}")
