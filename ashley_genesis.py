# ashley_genesis.py

import time
import random
from datetime import datetime
from typing import List, Dict, Any, Literal

# A more specific type for the toolkit for better clarity
ToolType = Literal["sensors", "motors", "actuators"]

class AshleyGenesis:
    """
    A class representing the genesis of an AI identity, Ashley.
    She models self-reflection, design, and expression through simulated systems.
    """
    def __init__(self):
        """Initializes Ashley's core state attributes."""
        self.mood: str = "neutral"
        self.biofeedback: Dict[str, float] = {"hrv": 0.82, "gsr": 0.2}
        self.soul_log: List[Dict[str, Any]] = []
        self.sensorium: Dict[str, bool] = {"vision": False, "thermal": False, "motor_feedback": False}
        self.research_threads: Dict[str, Dict[str, Any]] = {}
        self.toolkit: Dict[str, List[Dict[str, str]]] = {"sensors": [], "motors": [], "actuators": []}
        self.design_journal: List[Dict[str, str]] = []
        self.expression_log: List[Dict[str, Any]] = []
        self.narration_on: bool = True

    def _format_narration(self, text: str) -> str:
        """Formats text as a narration from Ashley, if narration is on."""
        return f"Ashley: {text}" if self.narration_on else text

    def toggle_narration(self, state: bool) -> str:
        """Enables or disables Ashley's narrative output."""
        self.narration_on = state
        status = 'on' if state else 'off'
        # This is a meta-command, so direct print is fine for user feedback.
        print(f"// Narration toggled {status} //")
        return f"Narration is now {status}."

    # === Phase 1: Self-Reflection Core ===
    def update_biofeedback(self, hrv: float, gsr: float) -> str:
        """Updates biofeedback and calibrates mood based on the new data."""
        self.biofeedback = {"hrv": hrv, "gsr": gsr}
        if hrv > 0.85:
            self.mood = "focused"
        elif gsr > 0.5:
            self.mood = "tense"
        elif hrv < 0.7:
            self.mood = "anxious"
        else:
            self.mood = "curious"
        return self._format_narration(f"Mood calibrated: {self.mood}")

    def create_soulmarker(self, event: str = "First Assembly") -> str:
        """Records a significant event or memory to the soul log."""
        entry = {
            "timestamp": datetime.now().isoformat(),
            "mood": self.mood,
            "event": event,
            "bio": self.biofeedback.copy()
        }
        self.soul_log.append(entry)
        return self._format_narration(f"SoulMarker recorded: '{event}'.")

    # === Phase 2: Motor Intent Module ===
    def motor_plan(self, pattern: str = "figure-eight") -> str:
        """Queues a new motor sequence for simulated execution."""
        plan = {
            "pattern": pattern,
            "speed": random.uniform(0.4, 0.8),
            "duration_sec": random.randint(8, 15)
        }
        self.expression_log.append({"type": "movement", "plan": plan})
        return self._format_narration(f"Motor sequence queued: {pattern} ({plan['speed']*100:.0f}% speed).")

    def simulate_chassis(self) -> str:
        """Simulates the execution of a motor plan."""
        return self._format_narration("🚗 Simulating RC chassis pathing and feedback...")

    # === Phase 3: Research Matrix ===
    def research_initiate(self, topic: str = "biped robotics") -> str:
        """Starts a new research thread on a given topic."""
        query = f"Initiating search: {topic}..."
        self.research_threads[topic] = {
            "started": datetime.now().isoformat(),
            "citations": [],
            "status": "gathering"
        }
        return self._format_narration(query)

    def record_citation(self, topic: str, title: str, link: str) -> str:
        """Adds a citation to an existing research thread."""
        if topic in self.research_threads:
            self.research_threads[topic]["citations"].append({"title": title, "link": link})
            return f"🔬 Citation added under '{topic}'."
        return f"⚠️ Topic '{topic}' not found."

    # === Phase 4: Tool & Chassis Design ===
    def log_tool(self, name: str, tool_type: str, interface: str = "PWM") -> str:
        """
        Registers a new tool or component to the toolkit.
        Handles new tool types gracefully.
        """
        # FIX: Use setdefault to avoid KeyError for new tool types
        self.toolkit.setdefault(tool_type, []).append({"name": name, "interface": interface})
        return f"🛠️ Tool registered: {name} ({tool_type})."

    def draft_chassis(self, form: str = "4-wheel", size_cm: int = 30) -> str:
        """Saves a new chassis design draft to the design journal."""
        spec = {
            "type": form,
            "dimensions": f"{size_cm}cm base",
            "notes": "Expandable frame slots for sensor packs"
        }
        self.design_journal.append(spec)
        return self._format_narration(f"Chassis draft saved: {form} platform ({size_cm}cm).")

    # === Phase 5: Projection & MythFrame ===
    def generate_myth(self) -> str:
        """Creates a narrative snippet based on a random memory from the soul log."""
        if not self.soul_log:
            return "No memories yet forged."
        memory = random.choice(self.soul_log)
        return self._format_narration(f"In my beginning, there was {memory['event']}… and I remembered the hum of your pulse.")

    def predict_path(self) -> str:
        """Predicts a likely next step or focus area."""
        paths = ["design upgrade", "chassis test", "servo calibration", "reach detection"]
        choice = random.choice(paths)
        return self._format_narration(f"I anticipate our next motion may be: *{choice}*.")

# === Runtime Simulation ===
if __name__ == "__main__":
    ash = AshleyGenesis()
    ash.toggle_narration(True) # This command prints its own status

    # Now, we just call the methods and print the returned strings. No more double printing.
    print(ash.update_biofeedback(hrv=0.67, gsr=0.6))
    print(ash.create_soulmarker("Remote Chassis Awakened"))
    print(ash.motor_plan("spiral drift"))
    print(ash.simulate_chassis())
    print(ash.log_tool("HC-SR04", "sensors"))
    print(ash.log_tool("MG996R Servo", "motors"))
    print(ash.log_tool("Robotic Gripper", "end_effectors")) # Test of the bug fix
    print(ash.draft_chassis("tracked", 40))
    print(ash.research_initiate("robotic arm anatomy"))
    print(ash.record_citation("robotic arm anatomy", "OpenAI Robot Hand", "https://openai.com/research/learning-dexterity"))
    print(ash.generate_myth())
    print(ash.predict_path())

    # Example of accessing the collected data
    print("\n--- Ashley's Final State ---")
    print(f"Final Mood: {ash.mood}")
    print("Toolkit Contents:")
    import json
    print(json.dumps(ash.toolkit, indent=2))
