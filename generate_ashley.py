# ==============================================================================
# Ashley AI - Final System Generator
# Version 33.0 - With "Plug-and-Play" Persona Core Expansion
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
    modules_to_install = ["pygame", "Pillow"] 
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
                # Find the main class in the module (e.g., Ashley)
                for item_name in dir(module):
                    item = getattr(module, item_name)
                    if isinstance(item, type) and item.__module__ == module_name:
                        # This is the class! Create an instance of it.
                        instance = item()
                        self.expansion_instances[module_name] = instance
                        print(f"  - Activated expansion module: {item_name}")
                        # Now, find all public methods in the instance
                        for func_name in dir(instance):
                            if not func_name.startswith('_') and callable(getattr(instance, func_name)):
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
            try:
                # Execute the action function from the loaded module's instance
                response = self.actions[best_match]()
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
# --- BLUEPRINT 3: Your Persona Core (`ashley_interface_unified_v2.py`) ---
# ==============================================================================
PERSONA_CORE_CODE = """
# ashley_interface_unified_v2.py
import time
import random
import tkinter as tk
from tkinter import messagebox

# The 'pygame' library is now a dependency that the failsafe will handle.
try:
    import pygame
    PYGAME_AVAILABLE = True
except ImportError:
    PYGAME_AVAILABLE = False

class Ashley:
    def __init__(self):
        self.voice_enabled = True
        self.mood = "neutral"
        self.biofeedback = {"hrv": 0.85, "gsr": 0.2}
        self.soulmarkers = []
        self.music_log = []
        self.anomaly_log = []
        if PYGAME_AVAILABLE:
            pygame.mixer.init()
        self.music_playing = False

    # === NARRATION ===
    def toggle_voice(self):
        self.voice_enabled = not self.voice_enabled
        return f"Voice {'on' if self.voice_enabled else 'off'}"

    def narrate(self, text):
        # This will now just return the text for the main core to speak
        return text

    # === MOOD LOGIC ===
    def update_biofeedback(self):
        # Simulate new biofeedback data
        hrv = round(random.uniform(0.6, 0.95), 2)
        gsr = round(random.uniform(0.1, 0.6), 2)
        self.biofeedback = {"hrv": hrv, "gsr": gsr}
        if hrv < 0.7: self.mood = "anxious"
        elif gsr > 0.5: self.mood = "tense"
        elif hrv > 0.85: self.mood = "focused"
        else: self.mood = "neutral"
        return self.narrate(f"Biofeedback updated. Current mood is now {self.mood}.")

    # === MUSIC COMPOSITION ===
    def compose_music(self):
        styles = {"focused": "Bach", "tense": "Beethoven", "anxious": "Debussy", "neutral": "Satie"}
        title = random.choice({"focused": ["Clockwork Silence"], "tense": ["Iron Pulse"], "anxious": ["The Distant Room"], "neutral": ["Soft Circuit"]}[self.mood])
        piece = {"title": title, "style": styles[self.mood], "mood": self.mood, "timestamp": time.ctime()}
        self.music_log.append(piece)
        return self.narrate(f"Composing '{title}' in the style of {piece['style']}.")

    # === SOULMARKERS ===
    def create_soulmarker(self):
        mark = {"label": self.compose_music().split("'")[1], "mood": self.mood, "biofeedback": self.biofeedback, "timestamp": time.ctime()}
        self.soulmarkers.append(mark)
        return self.narrate(f"SoulMarker '{mark['label']}' saved.")

    # === SENTINEL ===
    def detect_anomaly(self):
        source, type = random.choice(["garage", "lab", "atrium"]), random.choice(["phantom audio", "thermal shadow", "EM fluctuation"])
        entry = {"location": source, "type": type, "timestamp": time.ctime()}
        self.anomaly_log.append(entry)
        return self.narrate(f"WARNING: {type.capitalize()} detected in {source}.")

    # === MUSIC PLAYBACK ===
    def play_music(self):
        if not PYGAME_AVAILABLE: return "Music module dependency 'pygame' is missing. Please run repair."
        return self.narrate("Music playback feature is a prototype.")

    def stop_music(self):
        if not PYGAME_AVAILABLE: return "Music module dependency 'pygame' is missing."
        pygame.mixer.music.stop()
        self.music_playing = False
        return self.narrate("Playback stopped.")

    # === GUI Launcher (This is now a command for the core) ===
    def launch_gui(self):
        # This function will be called by the core, which will launch the GUI.
        # This function in the expansion is now just a trigger.
        return "launch_gui_now"

# This part is no longer needed as the core will run the methods
# if __name__ == "__main__":
#     launch_gui()
"""

# ==============================================================================
# --- THE GENERATOR SCRIPT ---
# ==============================================================================
def main():
    """This function creates the final, expandable application package."""
    print("--- Ashley AI Final System Generator (v33.0) ---")
    base_dir = Path(__file__).resolve().parent
    
    files_to_create = {
        "ashley_failsafe.py": ASHLEY_FAILSAFE_CODE,
        "ashley_core.py": ASHLEY_CORE_CODE,
        "expansions/ashley_interface_unified_v2.py": PERSONA_CORE_CODE
    }
    
    try:
        (base_dir / "expansions").mkdir(exist_ok=True)
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
        print("2. It will automatically find and load your new persona module.")
        print("3. You can now give commands like 'compose music' or 'detect anomaly'.")

    except Exception as e:
        print(f"\n[FATAL] An error occurred during file generation: {e}")
        traceback.print_exc()
        
if __name__ == "__main__":
    main()
    print("\n--- Generator script has finished. ---")
    input("Press Enter to exit...")
