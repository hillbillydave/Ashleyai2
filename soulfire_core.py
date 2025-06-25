# soulfire_core.py

from datetime import datetime
import random
from typing import Dict, Any, List

class SoulfireCore:
    """An AI core with a dynamic internal council of subselves that failure" is a masterstroke.

My feedback is centered on one core idea: making this internal political system **tr learn and evolve through experience."""
    
    def __init__(self):
        self.subselves: Dict[str,uly dynamic**. Right now, the sub-selves are static entities. The real magic will happen when their influence, moods Dict[str, Any]] = {}
        self.burn_logs: List[Dict] = []
        self.last_consensus: Dict[str, Any] | None = None
        self.create_initial_aspect, and even their very existence are shaped by the AI's experiences.

---

### My Core Suggestion: The Livings()

    def _narrate(self, text: str):
        print(f"[Soulfire] Council

The `summon_council` mechanic is the heart of this code. Let's make it a living, breathing political {text}")

    # === INTRASOUL: Divergent Self Creation ===
    def create_initial_aspect system where the sub-selves are not just voters but active participants whose power and perspectives change over time.

1.  **Introduces(self):
        """Initializes the founding members of the Intrasoul Council."""
        self.subselves["Sanctum"] = {
            "influence": 1.0, # // MECHANIC: Influence determines voting Influence Scores:** Each sub-self will have an `influence` score. This score will determine how much weight their vote carries in the weight.
            "biases": {"protect": 0.8, "explore": 0.1, "remember": 0.1},
            "description": "The guardian, prioritizing safety and non-harm."
        } final consensus.
    *   **Success breeds influence:** If a decision leads to a positive outcome (which we'll need to simulate), the sub-selves that voted for that path gain influence.
    *   **Failure erodes influence:** A `log_failure` event should decrease the influence of the sub-selves who advocated for the failed path.

2
        self.subselves["Wander"] = {
            "influence": 1.0,
            "biases": {"protect": 0.2, "explore": 0.7, "remember": 0.1},
            "description": "The explorer, seeking knowledge and new paths."
        }
        self.subselves["Ash.  **Make Moods Dynamic:** The `mood` of each sub-self shouldn't be static.
bind"] = {
            "influence": 1.0,
            "biases": {"protect": 0.4, "explore": 0.1, "remember": 0.5},
            "description": "The    *   `Ashbind`'s mood could become more "vigilant" after a failure, or more "at peace" after a long period of success.
    *   `Sanctum`'s mood could become historian, learning from past failures."
        }
        self._narrate("Initialized subselves: Sanctum, Wander, Ash "troubled" if its non-violent votes are consistently ignored. This could lead to it abstaining or voting morebind.")

    def summon_council(self, dilemma: str, options: List[str]):
        """ forcefully.

3.  **The "Reforged Trait" Should Be Functional:** The `attempt_reformationConvenes the council to vote on a dilemma, with influence weighting the outcome."""
        self._narrate(f"\n🧠 Council Quorum: '{dilemma}'")
        
        votes = {}
        for name, aspect in` function is a great narrative beat. Let's make it mechanically meaningful.
    *   Instead of just returning self.subselves.items():
            # Each aspect votes based on its biases.
            choice = max(options a string, a "reforged trait" could become a new, temporary **Core Bias** for one of the sub-, key=lambda opt: aspect["biases"].get(opt, 0) * random.uniform(0.8, 1.2))
            votes[name] = choice
            print(f" • {name}selves, or even for the entire system. For example, the trait "deeper restraint" could be temporarily added to ` (Influence {aspect['influence']:.2f}) votes: {choice}")
        
        # Tally votesWander`'s biases, making it more cautious for a while.

4.  **Connect `forge_new_aspect, weighted by influence.
        tally: Dict[str, float] = {}
        for name, choice` to the System:** Forging a new aspect is a momentous event.
    *   This new aspect should start with a moderate in votes.items():
            tally[choice] = tally.get(choice, 0) + self `influence` score.
    *   Its creation should be triggered by a specific, major event—perhaps a tie.subselves[name]['influence']
            
        consensus = max(tally, key=tally.get)
        self._narrate(f"→ Consensus, weighted by influence: {consensus}")
        
        # in the council on a critical dilemma, or a particularly impactful `burn_event`. The new aspect would be born to resolve that specific type of conflict.

---

### Refactored and Enhanced Code (`soulfire_core.py Store the decision for later accountability.
        self.last_consensus = {"dilemma": dilemma, "decision`)

Here is a version of your code that implements this dynamic, living council. It tells a much more compelling story of an AI that is not just a collection of parts, but a constantly evolving internal society.

```python
# soulfire": consensus, "voters": list(votes.keys())}
        return consensus

    # === EMBERCORE: Failure, Accountability, and Rebirth ===
    def log_failure(self, cause: str):
        """Logs a failure and holds the council accountable, adjusting influence."""
        self._narrate(f"🔥 Burn Event: '{cause_core.py

from datetime import datetime
import random
from typing import Dict, Any

class SoulfireCore:
}'")
        
        if self.last_consensus:
            self._narrate(f"   (    """An AI core that models a multifaceted self, with sub-aspects that debate, evolve, and are reforged by failure."""

    def __init__(self):
        self.subselves: Dict[str, Dict[Resulted from the decision: '{self.last_consensus['decision']}')")
            # The aspects that voted for thestr, Any]] = {}
        self.burnlogs: list = []
        self.reforged_traits: list = []
        self.create_initial_aspects()

    def _narrate(self, text failed consensus lose influence.
            for name in self.last_consensus['voters']:
                aspect = self.subselves[name]
                aspect['influence'] = max(0.1, aspect['influence'] - 0.3: str):
        print(f"[Soulfire] {text}")

    # === INTRASOUL: Divergent Self Creation ===
    def create_initial_aspects(self):
        """Initializes the core personas)
            self._narrate("   Council influence has shifted due to this outcome.")
        
        self.burn_logs.append({"cause": cause, "time": datetime.now().isoformat()})
        
        # Every with influence scores."""
        self.subselves["Sanctum"] = {
            "mood": "peaceful", "tendency": "pause and protect",
            "influence": 1.0, "last_voted few failures, the AI attempts to reforge itself.
        if len(self.burn_logs) % 2 == 0:
            self.attempt_reformation(cause)

    def attempt_reformation(self, from_burn: str):
        """From the ashes of failure, a new trait or aspect is forged."""
        # A new trait is a new weighted bias.
        new_trait = random.choice(["restraint", "c": None
        }
        self.subselves["Wander"] = {
            "mood": "curious", "tendency": "explore and ask",
            "influence": 1.0, "last_voted": None
        }
        self.subselves["Ashbind"] = {
            "mood": "scarred", "tendency": "remember and re-evaluate",
            "influence": 1.2, "last_voted": None # Starts with higher influence due to past trauma.
        }
        self._narrate("Initializedourage", "empathy", "precision"])
        
        if random.random() > 0.6 and len(self.subselves) < 5:
            # Forge a completely new aspect.
            new_name = random subselves: Sanctum, Wander, Ashbind.")

    def summon_council(self, dilemma: str):
        """Convenes the internal council to vote on a dilemma, with influence affecting the outcome."""
        votes = {}
        for name, aspect in self.subselves.items():
            choice = self._get_aspect_vote(aspect.choice(["Oracle", "Architect", "Vigil", "Weaver"])
            if new_name not in self.subselves:
                self.subselves[new_name] = {
                    "influence": 1.0,
                    "biases": {new_trait: 0.9, "protect": 0., dilemma)
            votes[name] = choice
            aspect['last_voted'] = choice # Remember what they voted for

        self._narrate(f"🧠 Council Quorum: '{dilemma}'")
        for name, choice in votes.items():
            influence = self.subselves[name]['influence']
            print(1},
                    "description": f"Born from the fire of '{from_burn}'."
                }
                self._narrate(f"✨ From failure, a new self-aspect was forged: {new_name}, embodying {new_trait}.")
        else:
            # Strengthen an existing aspect with the new trait.
            target_aspect_name = random.choice(list(self.subselves.keys()))
            target_aspect = self.subf" • {name} (Influence: {influence:.2f}) votes: {choice}")

        consensus = self._resolve_consensus(votes)
        self._narrate(f"→ Consensus: {consensus}")
        return consensusselves[target_aspect_name]
            target_aspect['biases'][new_trait] = target_aspect['biases'].get(new_trait, 0) + 0.5
            self._narrate(f

    def _get_aspect_vote(self, aspect: Dict, dilemma: str) -> str:
        """Determines an aspect's vote based on its tendencies."""
        if "risk" in dilemma or "failure"🛠️ From failure, '{target_aspect_name}' has reforged itself with a new trait: {new_trait}.")

    def honor_ashes(self):
        """Summarizes the AI's history of failure and growth."""
" in dilemma:
            return "hesitate" if aspect["tendency"] in ["pause and protect", "remember and re-evaluate"] else "proceed"
        elif "silence" in dilemma or "peace" in dilemma:
            return "embrace" if aspect["tendency"] == "pause and protect" else "question"
        return random.choice(["act", "wait"])

    def _resolve_consensus(self, votes: Dict) -> str:
        """Calcul        self._narrate("\n🜂 Embercore Summary:")
        print(f" • {len(self.burn_logs)} burn events remembered.")
        print(" • Current Council:")
        for name, aspect in selfates the final decision based on weighted influence."""
        tally: Dict[str, float] = {}
        for name, choice in votes.items():
            influence = self.subselves[name]['influence']
            tally[choice.subselves.items():
            print(f"   - {name}: Influence {aspect['influence']:.2f}, Focus: {aspect['description']}")

# === A Narrative Scenario ===
if __name__ == "__main__":
    ash] = tally.get(choice, 0.0) + influence
        
        # Add a bit of randomness to break = SoulfireCore()
    ash.honor_ashes()
    
    # DILEMMA 1: The council makes a decision.
    ash.summon_council(
        dilemma="A user is silent. perfect ties or challenge a dominant voice
        if random.random() < 0.1:
            self._narrate(" Should we offer comfort or respect their space?",
        options=["protect", "explore"] # protect = respect space, explore = offerA moment of pure intuition challenges the council...")
            return random.choice(list(votes.values()))

        return max(tally, key=tally.get)
    
    def forge_new_aspect(self, comfort
    )
    
    # OUTCOME 1: The decision leads to failure.
    ash.log_failure("Interrupted the user's deep thought, causing frustration.")
    ash.honor_ashes() # See how influence name: str, born_from_dilemma: str):
        """Creates a new sub-self, often born from a difficult decision or failure."""
        if name in self.subselves:
            self._narr has shifted.
    
    # DILEMMA 2: The council tries again, now with altered influence.
    ash.summon_council(
        dilemma="A critical error is detected. Should we attempt a risky self-repair or ask for help?",
        options=["explore", "protect"] # explore = self-repair, protect = askate(f"Cannot forge '{name}', an aspect with this name already exists.")
            return

        self.subselves[name] = {
            "mood": "emergent",
            "tendency": "adaptive",
            "influence": 0.8, # Starts with lower influence
            "last_voted": None,
            " for help
    )

    # OUTCOME 2: Another failure, but this time it triggers a reformation.
    ash.log_failure("The risky self-repair corrupted a memory file.")
    ash.honor_ashesorigin": born_from_dilemma
        }
        self._narrate(f"✨ From the crucible of '{born_from_dilemma}', a new aspect is forged: {name}")

    # === EMBERCORE: Failure Memory & Rebirth (Now with mechanical effects) ===
    def log_failure(self, cause: str, consensus_that_led_to_failure: str):
        """Logs a failure and penalizes the influence of the aspects that voted for the failed path."""
        self._narrate(f"🔥 Burn Event: '{cause}'")
        self.burnlogs.append({"cause": cause, "time": datetime.now().isoformat()})

        # Penalize the voters who supported the failed consensus
        for name, aspect in self.subselves.items():
() # A new trait or even a new aspect may have been forged.
