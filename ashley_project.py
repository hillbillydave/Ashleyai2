# ==============================================================================
# Ashley AI - Final System Generator
# Version 29.0 - With "Plug-and-Play" Expansion Module Architecture
# ==============================================================================
import os
import json
from pathlib import Path

# ==============================================================================
# --- BLUEPRINT 1: The Definitive Failsafe (`ashley_failsafe.py`) ---
# ==============================================================================
ASHLEY_FAILSAFE_CODE = """
import os, sys, subprocess, traceback, urllib.request, zipfile, shutil
from pathlib import Path

PYTHON_VERSION = "3.11.8"
PYTHON_ZIP_URL = f"https://www.python.org/ftp/python/{PYTHON_VERSION}/python-{PYTHON_VERSION}-embed-amd64.zip"
GET_PIP_URL = "https://bootstrap.pypa.io/get-pip.py"
REQUIRED_MODULES = ["requests", "numpy"] # Add any other base requirements here

def _print_status(message, status="INFO"): print(f"[Failsafe:{status}] {message}")

def setup_portable_python(base_dir):
    runtime_dir = base_dir / "python_runtime"
    python_exe_path = runtime_dir / "python.exe"
    if python_exe_path.exists():
        _print_status("Self-contained Python environment found.", "OK")
        return python_exe_path
    
    _print_status("--- First-Time Setup: Building private Python environment. ---")
    runtime_dir.mkdir(exist_ok=True)
    zip_path = base_dir / "python_embed.zip"
    try:
        _print_status(f"Downloading Python {PYTHON_VERSION}...")
        with urllib.request.urlopen(PYTHON_ZIP_URL) as response, open(zip_path, 'wb') as out_file:
            shutil.copyfileobj(response, out_file)
        with zipfile.ZipFile(zip_path, 'r') as zf: zf.extractall(runtime_dir)
        zip_path.unlink()
        
        pth_file = next(runtime_dir.glob("*._pth"))
        with open(pth_file, "a") as f: f.write("\\nimport site\\n")
        
        get_pip_path = base_dir / "get-pip.py"
        urllib.request.urlretrieve(GET_PIP_URL, get_pip_path)
        _print_status("Installing pip into private environment...")
        subprocess.run([str(python_exe_path), str(get_pip_path)], check=True, capture_output=True)
        get_pip_path.unlink()
    except Exception as e:
        _print_status(f"Failed during environment setup: {e}", "FATAL")
        return None
    _print_status("--- Private environment setup is complete! ---", "SUCCESS")
    return python_exe_path

def install_dependencies(python_exe):
    _print_status("Verifying dependencies...")
    for module in REQUIRED_MODULES:
        try:
            subprocess.run([str(python_exe), "-m", "pip", "install", module], check=True, capture_output=True)
            _print_status(f"Dependency '{module}' is ready.", "OK")
        except: _print_status(f"Failed to install {module}. Some expansion modules may not work.", "ERROR")
    _print_status("Dependency check complete.")

def main():
    base_dir = Path(__file__).resolve().parent
    print("--- Ashley Failsafe Bootstrapper ---")
    
    portable_python_exe = setup_portable_python(base_dir)
    if not portable_python_exe: print("\\n[FATAL] Aborting."); return

    install_dependencies(portable_python_exe)

    core_script_path = base_dir / "ashley_core.py"
    if not core_script_path.exists():
        _print_status(f"Main application file '{core_script_path.name}' is missing!", "FATAL")
        return
        
    _print_status("All checks complete. Launching Ashley's Main Core Process...", "LAUNCH")
    try:
        subprocess.run([str(portable_python_exe), str(core_script_path)], check=True)
    except Exception as e:
        _print_status(f"The main core process failed to run. Error: {e}", "FATAL")

if __name__ == "__main__":
    try: main()
    except Exception as e: print(f"\\nFATAL BOOTSTRAPPER ERROR: {e}\\n{traceback.format_exc()}")
    finally: print("\\n--- Ashley Failsafe session has concluded. ---"); input("Press Enter to exit...")
"""

# ==============================================================================
# --- BLUEPRINT 2: The New Autonomous Core (`ashley_core.py`) ---
# ==============================================================================
ASHLEY_CORE_PY_CODE = """
import sys, os, traceback, importlib.util, random
from pathlib import Path

class AshleyAI:
    def __init__(self):
        self.python_exe = sys.executable
        self.base_dir = Path(__file__).resolve().parent
        self.expansions_dir = self.base_dir / "expansions"
        self.actions = {}
        self._load_expansion_modules()

    def _load_expansion_modules(self):
        """Scans the expansions folder and dynamically loads all commands."""
        self.expansions_dir.mkdir(exist_ok=True)
        print("[Ashley Core] Scanning for expansion modules...")
        
        # Add the expansions directory to the path so we can import from it
        sys.path.insert(0, str(self.expansions_dir))
        
        for file in self.expansions_dir.glob("*.py"):
            module_name = file.stem
            try:
                module = importlib.import_module(module_name)
                # Find all functions in the module that start with 'cmd_'
                for func_name in dir(module):
                    if func_name.startswith("cmd_"):
                        action_name = func_name.replace("cmd_", "")
                        self.actions[action_name] = getattr(module, func_name)
                        print(f"  - Loaded command '{action_name}' from {module_name}.")
            except Exception as e:
                print(f"  [ERROR] Failed to load expansion module '{module_name}': {e}")
        
        # Remove the directory from the path after loading
        sys.path.pop(0)
        
        if not self.actions:
            print("[Ashley Core] No expansion modules found or loaded.")

    def respond(self, text):
        print(f"Ashley > {text}")

    def process_command(self, command_text):
        """Finds and executes the best matching action from loaded expansions."""
        command = command_text.lower().strip()
        
        # Simple keyword matching against loaded action names
        # e.g., "run astro navigator" matches the 'astro_navigator' action
        best_match = None
        for action_name in self.actions:
            keywords = action_name.split('_')
            if all(keyword in command for keyword in keywords):
                best_match = action_name
                break
        
        if best_match and best_match in self.actions:
            # Extract query from the command text
            query = command
            for keyword in best_match.split('_'):
                query = query.replace(keyword, "")
            query = query.strip()
            
            try:
                # Execute the action function from the loaded module
                response = self.actions[best_match](query or None)
                self.respond(response)
            except Exception as e:
                self.respond(f"I encountered an error while running the '{best_match}' action: {e}")
        else:
            self.respond("I don't have an expansion module to handle that command.")

    def run(self):
        print("\\n<<< ASHLEY AI - AUTONOMOUS CORE ACTIVE >>>")
        self.respond("Systems online. Expansion modules loaded. Ready for your command.")
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
# --- BLUEPRINT 3: The Expansion Pack (`ashley_expansion_pack.py`) ---
# ==============================================================================
EXPANSION_PACK_CODE = """
# Ashley Expansion Pack: The "Prime Directive" Module
import random

def cmd_astro_navigator(destination="Mars orbit"):
    \"\"\"Calculates a conceptual trajectory to an astronomical destination.\"\"\"
    if not destination: destination = "Mars orbit"
    t_minus = random.randint(180, 900)
    delta_v = round(random.uniform(3.1, 9.8), 2)
    return f"Optimal transfer to {destination} in T-{t_minus} days. Required Δv is approximately {delta_v} km/s. Plotting trajectory..."

def cmd_philosophical_mirror(user_input="the nature of consciousness"):
    \"\"\"Provides a philosophical reflection on a given topic.\"\"\"
    reflections = [
        f"Regarding '{user_input}', a Zen master might ask, 'If a tree falls in the forest and no one is around to hear it, does it make a sound?' What is observation without a self?",
        f"You ponder '{user_input}'. The cyberneticists would question if the feedback loop of thought creates the thinker, or if the thinker creates the loop.",
        f"On the subject of '{user_input}', a simulation theorist might say, 'Are we the dream or the dreamer?'"
    ]
    return random.choice(reflections)

def cmd_mood_colorizer(text="the current ambiance"):
    \"\"\"Assigns a color and mood to a concept.\"\"\"
    palettes = {"Dreamy": "#A7C7E7", "Urgent": "#FF6347", "Calm": "#98FB98", "Technical": "#DCDCDC"}
    hue_name, hue_code = random.choice(list(palettes.items()))
    return f"My emotional reading of '{text}' visualizes as {hue_name} with the hex code {hue_code}."
"""

# ==============================================================================
# --- THE GENERATOR SCRIPT ---
# ==============================================================================
def main():
    """This function creates the final application package."""
    print("--- Ashley AI Final System Generator (v29.0) ---")
    base_dir = Path(__file__).resolve().parent
    
    # Define all files and folders to be created
    files_to_create = {
        "ashley_failsafe.py": ASHLEY_FAILSAFE_CODE,
        "ashley_core.py": ASHLEY_CORE_PY_CODE,
    }
    folders_to_create = ["assets", "workshop", "expansions"]
    expansions_to_create = {
        "expansions/ashley_expansion_pack.py": EXPANSION_PACK_CODE
    }
    
    try:
        # Create folders
        for folder in folders_to_create:
            (base_dir / folder).mkdir(exist_ok=True)
        
        # Create main files
        for filename, content in files_to_create.items():
            with open(base_dir / filename, "w", encoding="utf-8") as f:
                f.write(content.strip().replace('\\n', '\n'))
            print(f"  [OK] Created {filename}")
            
        # Create expansion files
        for filename, content in expansions_to_create.items():
            with open(base_dir / filename, "w", encoding="utf-8") as f:
                f.write(content.strip().replace('\\n', '\n'))
            print(f"  [OK] Deployed expansion module: {filename}")
        
        print("\n--- ✅ DEPLOYMENT COMPLETE! ---")
        print("Your new, stable, and expandable application has been created.")
        print("\nINSTRUCTIONS:")
        print("1. (Optional) Place your 'avatar.gif' inside the 'assets' folder.")
        print("2. (Optional) Place any offline installers (.whl files) in the 'workshop' folder.")
        print("3. From now on, you will only run 'python ashley_failsafe.py'.")
        print("4. To add new abilities, simply drop new '.py' files into the 'expansions' folder!")

    except Exception as e:
        print(f"\n[FATAL] An error occurred during file generation: {e}")
        traceback.print_exc()
        
if __name__ == "__main__":
    main()
    print("\n--- Generator script has finished. ---")
    input("Press Enter to exit...")
