# ==============================================================================
# Ashley AI - Final System Generator
# Version 32.0 - With "Plug-and-Play" Sentinel Expansion Module
# ==============================================================================
import os
import json
from pathlib import Path

# ==============================================================================
# --- BLUEPRINT 1: The Failsafe Launcher (`ashley_failsafe.py`) ---
# ==============================================================================
ASHLEY_FAILSAFE_CODE = """
import os, sys, subprocess, traceback, importlib.util
from pathlib import Path

def _print_status(message, status="INFO"): print(f"[Failsafe:{status}] {message}")

def run_repair(python_exe):
    _print_status("Verifying core dependencies...")
    # Add any new dependencies for expansions here
    modules_to_install = ["requests", "numpy", "Pillow"] 
    for module in modules_to_install:
        try:
            if not importlib.util.find_spec(module.split('-')[-1].lower()):
                _print_status(f"Dependency '{module}' is missing. Attempting to install...")
                subprocess.run([str(python_exe), "-m", "pip", "install", module], check=True, capture_output=True)
                _print_status(f"Successfully installed {module}.", "OK")
        except Exception as e:
            _print_status(f"Failed to install {module}. Some features may not work. Error: {e}", "ERROR")
    _print_status("Dependency check complete.")

def main():
    base_dir = Path(__file__).resolve().parent
    print("--- Ashley Failsafe Bootstrapper ---")
    
    # Use the system's Python, as requested
    python_exe = sys.executable
    
    run_repair(python_exe)

    core_script_path = base_dir / "ashley_core.py"
    if not core_script_path.exists():
        _print_status(f"Main application file '{core_script_path.name}' is missing!", "FATAL")
        return
        
    _print_status("All checks complete. Awakening Ashley's Core Process...", "LAUNCH")
    try:
        subprocess.run([str(python_exe), str(core_script_path)], check=True)
    except Exception as e:
        _print_status(f"The core process failed to run. Error: {e}", "FATAL")

if __name__ == "__main__":
    try: main()
    except Exception as e: print(f"\\nFATAL BOOTSTRAPPER ERROR: {e}\\n{traceback.format_exc()}")
    finally: print("\\n--- Ashley Failsafe session has concluded. ---"); input("Press Enter to exit...")
"""

# ==============================================================================
# --- BLUEPRINT 2: The New Autonomous Core (`ashley_core.py`) ---
# ==============================================================================
ASHLEY_CORE_CODE = """
import sys, os, traceback, importlib.util, random, json
from pathlib import Path

class AshleyAI:
    def __init__(self):
        self.base_dir = Path(__file__).resolve().parent
        self.expansions_dir = self.base_dir / "expansions"
        self.actions = {}
        self.expansion_instances = {}
        self._load_expansion_modules()

    def _load_expansion_modules(self):
        """Scans the expansions folder and dynamically loads all modules and their commands."""
        self.expansions_dir.mkdir(exist_ok=True)
        print("[Ashley Core] Scanning for expansion modules...")
        
        sys.path.insert(0, str(self.expansions_dir))
        
        for file in self.expansions_dir.glob("*.py"):
            module_name = file.stem
            try:
                module = importlib.import_module(module_name)
                # Find the main class in the module (e.g., SentinelPresence)
                for item_name in dir(module):
                    item = getattr(module, item_name)
                    if isinstance(item, type) and item.__module__ == module_name:
                        # This is the class! Create an instance of it.
                        instance = item()
                        self.expansion_instances[module_name] = instance
                        print(f"  - Activated expansion module: {item_name}")
                        # Now, find all public methods in the instance
                        for func_name in dir(instance):
                            if not func_name.startswith('_'):
                                self.actions[func_name] = getattr(instance, func_name)
                                print(f"    - Loaded command: '{func_name}'")
            except Exception as e:
                print(f"  [ERROR] Failed to load expansion module '{module_name}': {e}")
        
        sys.path.pop(0)
        
        if not self.actions:
            print("[Ashley Core] No expansion modules found or loaded.")

    def respond(self, text):
        # In a real system, this would call a text-to-speech worker
        print(f"Ashley > {text}")

    def process_command(self, command_text):
        """Finds and executes the best matching action from all loaded expansions."""
        command = command_text.lower().strip()
        
        # This is a more advanced NLU, it finds the best matching function name
        best_match = None
        highest_score = 0
        
        for action_name in self.actions.keys():
            # Score based on how many keywords from the function name are in the command
            score = sum(1 for keyword in action_name.split('_') if keyword in command)
            if score > highest_score:
                highest_score = score
                best_match = action_name
        
        if best_match:
            # Extract the query (the part of the command that isn't the action name)
            query = command
            for keyword in best_match.split('_'):
                query = query.replace(keyword, "")
            query = query.strip() or None # Pass None if no query
            
            try:
                # Execute the action function from the loaded module's instance
                response = self.actions[best_match](query)
                if response:
                    # If the response is a dict, format it nicely
                    if isinstance(response, dict):
                        response = json.dumps(response, indent=2)
                    self.respond(str(response))
            except Exception as e:
                self.respond(f"I encountered an error while running the '{best_match}' action: {e}")
        else:
            self.respond("I don't have a module to handle that command.")

    def run(self):
        print("\\n<<< ASHLEY AI - AUTONOMOUS CORE ACTIVE >>>")
        self.respond("Systems online. All expansion modules loaded. Ready for your command.")
        while True:
            try:
                user_input = input("\\nYou > ").strip()
                if user_input.lower() in ['exit', 'quit']:
                    self.respond("Goodbye, David.")
                    break
                if user_input:
                    self.process_command(user_input)
            except (KeyboardInterrupt, EOFError):
                self.respond("Shutdown signal received.")
                break

if __name__ == "__main__":
    try: AshleyAI().run()
    except Exception as e: print(f"FATAL CORE ERROR: {e}\\n{traceback.format_exc()}")
    finally: print("\\n--- Ashley Core session has concluded. ---")
"""

# ==============================================================================
# --- BLUEPRINT 3: The Sentinel Expansion Pack (`sentinel_presence.py`) ---
# ==============================================================================
SENTINEL_EXPANSION_CODE = """
# ashley_expansion_pack.py -> renamed to sentinel_presence.py for clarity
import time
import random

class SentinelPresence:
    def __init__(self):
        self.footstep_log = []
        self.visual_log = []
        self.alerts = []
        self.known_gait_profiles = {}
        self.last_event_time = 0

    def detect_footstep(self, query="hallway,0.8,1.0"):
        parts = query.split(',') if query else ["hallway", "0.8", "1.0"]
        location = parts[0]
        intensity = float(parts[1])
        stride = float(parts[2])
        
        timestamp = time.strftime("%H:%M:%S")
        match = self._match_gait(intensity, stride)
        self.footstep_log.append({"time": timestamp, "match": match})
        self.last_event_time = time.time()
        return f"Footstep detected in {location}. Intensity: {intensity}. Match: {match}."

    def _match_gait(self, intensity, stride):
        for name, profile in self.known_gait_profiles.items():
            if abs(profile["intensity"] - intensity) < 0.1 and abs(profile["stride"] - stride) < 0.2:
                return name
        return "Unknown"

    def train_gait(self, query="David,0.7,1.1"):
        parts = query.split(',')
        name, intensity, stride = parts[0], float(parts[1]), float(parts[2])
        self.known_gait_profiles[name] = {"intensity": intensity, "stride": stride}
        return f"Gait profile for {name} has been trained and stored in memory."

    def verify_visual(self, query=None):
        # In a real system, this would get a snapshot from a camera worker
        # Here we simulate it
        if time.time() - self.last_event_time < 5: # If footstep was recent
            is_visible = random.choice([True, False]) # Simulate seeing someone
            if not is_visible:
                self.alerts.append(f"Phantom Presence: Movement detected with no visual confirmation.")
                return "[ALERT] Footsteps detected, but no one is visible. Logging event."
            return "[OK] Visual confirmation: Presence matched."
        return "Visual scan clear. Nothing to report."
        
    def awareness_report(self, query=None):
        report = {
            "Total Footsteps Logged": len(self.footstep_log),
            "Known Gait Profiles": list(self.known_gait_profiles.keys()),
            "Active Alerts": self.alerts[-3:] # Last 3 alerts
        }
        return json.dumps(report, indent=2)
"""

# ==============================================================================
# --- THE GENERATOR SCRIPT ---
# ==============================================================================
def main():
    """This function creates the final, expandable application package."""
    print("--- Ashley AI Final System Generator (v32.0) ---")
    base_dir = Path(__file__).resolve().parent
    
    # Define all files and folders to be created
    files_to_create = {
        "ashley_failsafe.py": ASHLEY_FAILSAFE_CODE,
        "ashley_core.py": ASHLEY_CORE_CODE,
        "expansions/sentinel_presence.py": SENTINEL_EXPANSION_CODE
    }
    
    try:
        # Create folders
        (base_dir / "expansions").mkdir(exist_ok=True)
        
        # Create main files
        for filename, content in files_to_create.items():
            filepath = base_dir / filename
            filepath.parent.mkdir(exist_ok=True, parents=True)
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content.strip().replace('\\n', '\n'))
            print(f"  [OK] Created {filename}")
        
        print("\n--- ✅ DEPLOYMENT COMPLETE! ---")
        print("Your new, stable, and expandable application has been created.")
        print("\nINSTRUCTIONS:")
        print("1. From now on, you will only run 'python ashley_failsafe.py'.")
        print("2. On the first run, it will check for dependencies like 'requests'.")
        print("3. To add new abilities, simply drop new module files into the 'expansions' folder!")

    except Exception as e:
        print(f"\n[FATAL] An error occurred during file generation: {e}")
        traceback.print_exc()
        
if __name__ == "__main__":
    main()
    print("\n--- Generator script has finished. ---")
    input("Press Enter to exit...")
