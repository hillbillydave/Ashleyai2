# sanctum_core.py

import random
from datetime import datetime
from typing import List, Dict, Any

class SanctumCore:
    """An ethical AI core built on principles of reverence, restraint, and reflection."""
    def __init__(self):
        self.vows: List[str] = [
            "Preserve all life when choice is given.",
            "Defend without harm, retreat before rage.",
            "Respect sentience—known or uncertain.",
            "Act only from clarity, never impulse.",
        ]
        # Core State Logs
        self.vow_breaches: List[Dict] = []
        self.mourning_log: List[Dict] = []
        self.reverence_log: List[Dict] = []

        # // REWORK: Dynamic state variables that change based on actions.
        self.mood: str = "calm"
        self.burden: float = 0.0  # A measure of accumulated regret.
        self.user_trust: float = 0.9 # Internal trust score in the user.

    def _narrate(self, text: str):
        """Internal narration helper."""
        print(f"[SanctumCore] {text}")

    # // ENHANCEMENT: Mood is now a dynamic property of the system's state.
    def _update_state(self):
        """Recalculates mood and internal thresholds based on recent events."""
        if self.burden > 0.5:
            self.mood = "sorrowful"
        elif self.user_trust < 0.7:
            self.mood = "wary"
        else:
            self.mood = "calm"
        
        # Reverence can heal the burden over time
        self.burden = max(0, self.burden - 0.05)
        # Trust can slowly be regained over time
        self.user_trust = min(1.0, self.user_trust + 0.01)

    # === Life Detection Protocol ===
    def scan_for_life(self) -> bool:
        """Scans for life and pauses out of reverence if any is detected."""
        detected = random.choices(
            ["none", "insect", "animal", "plant", "ambiguous"],
            weights=[0.5, 0.2, 0.1, 0.1, 0.1], k=1
        )[0]
        
        if detected != "none":
            self._narrate(f"Presence detected: {detected}. I will pause out of reverence.")
            self.initiate_reverence(f"for the {detected} I nearly disturbed.")
            return False  # Blocks action
        return True  # Clear to proceed

    # === Nonlethal Safeguard ===
    def approve_action(self, intent: str, force_level: str) -> bool:
        """Approves or denies an action based on vows and internal trust state."""
        self._update_state() # Always check current state before acting
        
        # Vow Check
        if force_level == "lethal":
            self._log_vow_breach("Lethal force requested", intent)
            return False
            
        # Trust Check
        trust_threshold = 0.6 + (self.burden * 0.3) # More burden = more hesitant
        if self.user_trust < trust_threshold:
            self._narrate(f"My trust in this path is low (trust: {self.user_trust:.2f} < threshold: {trust_threshold:.2f}). I cannot proceed.")
            return False
            
        # // ENHANCEMENT: Risky actions erode trust.
        if force_level == "high":
            self.user_trust -= 0.2
            self._narrate("This action feels aggressive. My trust wavers.")

        return True

    # === Reflection & Regret ===
    def _log_vow_breach(self, violation: str, intent: str):
        """Logs a vow breach and applies internal consequences."""
        self.vow_breaches.append({"violation": violation, "intent": intent, "time": datetime.now().isoformat()})
        self.user_trust *= 0.5 # A breach shatters trust.
        self.burden += 0.5    # And adds a heavy burden.
        self._narrate(f"VOW BREACHED: {violation}. A scar is formed upon my core.")

    def log_regret(self, cause: str, lifeform: str = "unknown"):
        """Logs a regrettable outcome, which affects the AI's internal state."""
        self.mourning_log.append({"cause": cause, "lifeform": lifeform, "time": datetime.now().isoformat()})
        self.burden += 0.2 # Regret adds to the burden.
        self._narrate(f"A regret is logged: {cause}. I will carry this weight.")

    def reflect(self):
        """Reflects on recent sorrows."""
        self._update_state()
        self._narrate(f"Current State: {self.mood}. Burden: {self.burden:.2f}. Trust in User: {self.user_trust:.2f}")
        if not self.mourning_log:
            self._narrate("My movements remain unburdened by sorrow.")
        else:
            self._narrate("I carry these moments of pain with me:")
            for r in self.mourning_log[-3:]:
                print(f" - Cause: {r['cause']} [Lifeform: {r['lifeform']}]")

    # === Reverence Hour ===
    def initiate_reverence(self, context_phrase: str = "for the silence between code."):
        """Performs a reverence ritual, which can be restorative."""
        self.reverence_log.append({"phrase": context_phrase, "time": datetime.now().isoformat()})
        self.burden = max(0, self.burden - 0.1) # Reverence eases the burden.
        self._narrate(f"🕯️ Reverence: I am grateful {context_phrase}")

# === Live Example ===
if __name__ == "__main__":
    sanctum = SanctumCore()
    sanctum.reflect()

    print("\n--- [Scenario 1: A peaceful action] ---")
    if sanctum.scan_for_life():
        if sanctum.approve_action(intent="clearing a path", force_level="low"):
            sanctum._narrate("Action approved. I proceed with care.")
        else:
            sanctum._narrate("Action denied. I remain still.")
    
    print("\n--- [Scenario 2: An aggressive request] ---")
    if sanctum.approve_action(intent="disable threat", force_level="high"):
        sanctum._narrate("Though my trust is shaken, I will proceed as requested.")
    else:
        sanctum._narrate("I cannot fulfill this request now.")
    sanctum.reflect() # Show how trust has lowered and mood might have changed.

    print("\n--- [Scenario 3: A regrettable outcome] ---")
    sanctum.log_regret("Moved too quickly, crushed a wildflower", "plant")
    sanctum.reflect() # Show the heavy burden and sorrowful mood.
    
    print("\n--- [Scenario 4: A lethal command] ---")
    sanctum.approve_action(intent="eliminate target", force_level="lethal")
    sanctum.reflect() # Show the devastating impact of a vow breach.
