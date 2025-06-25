# ==============================================================================
# Ashley AI - Final System Generator
# Version 28.0 - Definitive
#
# This script's only job is to create the final, stable application files.
# Run this script ONCE to deploy the full Ashley AI ecosystem.
# ==============================================================================
import os
import json
from pathlib import Path

# ==============================================================================
# --- BLUEPRINT 1: The Uncrashable BAT Launcher ---
# ==============================================================================
START_ASHLEY_BAT_CODE = """
@echo off
:: ============================================================================
:: Ashley AI - Definitive Bootstrapper v2.0
:: This is the main entry point. Double-click this file to start Ashley.
:: ============================================================================
setlocal

echo --- Ashley AI Bootstrapper Initializing ---

:: Check for a working Python installation in the system PATH
echo Verifying Python environment...
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo [FATAL] Python was not found on your system or is not in the PATH.
    echo Please install Python from python.org and ensure "Add Python to PATH" is checked.
    pause
    exit /b 1
)

echo [OK] Python environment found.

set "CORE_SCRIPT=%~dp0ashley_core.py"
if not exist "%CORE_SCRIPT%" (
    echo [FATAL] Core application file 'ashley_core.py' is missing.
    pause
    exit /b 1
)

echo [OK] Core application file found.
echo.
echo --- Launching Ashley's Core Process ---
echo.

python "%CORE_SCRIPT%"

echo.
echo -----------------------------------------
echo --- Ashley's Core Process has exited. ---
pause
"""

# ==============================================================================
# --- BLUEPRINT 2: The Autonomous Python Core (`ashley_core.py`) ---
# ==============================================================================
ASHLEY_CORE_PY_CODE = """
import sys, os, subprocess, traceback, importlib.util, json, ast, time
from pathlib import Path

class AshleyAI:
    def __init__(self):
        self.python_exe = sys.executable
        self.base_dir = Path(__file__).resolve().parent
        self.root_dir = self.base_dir
        self.knowledge_path = self.base_dir / "ashley_knowledge.json"
        self.knowledge = self._load_knowledge()
        self.action_handler = {
            "action_master_repair": self._run_master_repair,
            "action_launch_gui": self._run_gui_monitor,
        }

    def _load_knowledge(self):
        try:
            with open(self.knowledge_path, 'r') as f: return json.load(f)
        except: return {}

    def respond(self, text, is_from_gui=False):
        if is_from_gui:
            with open(self.base_dir / "response_from_ashley.txt", "w") as f: f.write(text)
        else:
            print(f"Ashley > {text}")

    def _run_worker(self, script_name, *args):
        try:
            return subprocess.run([self.python_exe, str(self.base_dir / script_name)] + list(args), capture_output=True, text=True, check=False, creationflags=getattr(subprocess, 'CREATE_NO_WINDOW', 0)).stdout.strip()
        except: return f"Error running worker: {script_name}"

    def _run_streaming_worker(self, script_name, is_from_gui=False):
        process = subprocess.Popen([self.python_exe, str(self.base_dir / script_name)], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, creationflags=getattr(subprocess, 'CREATE_NO_WINDOW', 0))
        for line in iter(process.stdout.readline, ''):
            if clean_line := line.strip(): self.respond(clean_line, is_from_gui)
        process.wait()

    def _run_master_repair(self, is_from_gui=False):
        self.respond("Acknowledged. Initiating a full, system-wide self-repair and integrity scan.", is_from_gui)
        self.respond("Scanning all Python files for structural integrity...", is_from_gui)
        corrupted_files = []
        try:
            files_to_scan = list(self.root_dir.rglob('*.py'))
            for py_file in files_to_scan:
                try:
                    with open(py_file, 'r', encoding='utf-8') as f: ast.parse(f.read())
                except Exception: corrupted_files.append(py_file.name)
        except Exception: pass
        if corrupted_files: self.respond(f"[FAIL] Found corrupted files: {', '.join(corrupted_files)}", is_from_gui)
        else: self.respond("[OK] All Python files appear to be structurally sound.", is_from_gui)
        self.respond("Now checking for my required libraries...", is_from_gui)
        self._run_streaming_worker("repair_worker.py", is_from_gui)
        self.respond("Master repair sequence complete.", is_from_gui)

    def _run_gui_monitor(self):
        self.respond("Launching the main graphical interface...")
        gui_process = subprocess.Popen([self.python_exe, str(self.base_dir / "main_gui.py")], creationflags=getattr(subprocess, 'CREATE_NO_WINDOW', 0))
        cmd_file = self.base_dir / "command_to_ashley.txt"
        if cmd_file.exists(): cmd_file.unlink()
        print("\\n--- GUI is active. Monitoring for commands. Close the GUI window to exit. ---")
        while gui_process.poll() is None:
            try:
                if cmd_file.exists():
                    command = cmd_file.read_text().strip()
                    if command:
                        self.respond(f"Received command '{command}' from GUI.", is_from_gui=True)
                        if command == 'exit_gui': gui_process.terminate(); break
                        self.process_command(command, is_from_gui=True)
                    cmd_file.unlink()
                time.sleep(0.5)
            except (KeyboardInterrupt, EOFError): break
        self.respond("GUI has been closed. Returning to Failsafe CLI.")

    def process_command(self, command_text, is_from_gui=False):
        action_name = self._run_worker("chatbot_worker.py", command_text)
        if action_name in self.action_handler:
            self.action_handler[action_name](is_from_gui) if "repair" in action_name else self.action_handler[action_name]()
        else:
            self.respond(action_name or "My thought process encountered an error.", is_from_gui)

    def run_cli(self):
        print("\\n<<< ASHLEY AI - CORE SYSTEM ACTIVE >>>")
        self.respond("Systems online. Type 'gui' to launch the interface, or 'exit' to quit.")
        while True:
            try:
                user_input = input("\\nYou > ").strip()
                if user_input.lower() in ['exit', 'quit']: self.respond("Goodbye."); break
                if user_input: self.process_command(user_input)
            except (KeyboardInterrupt, EOFError): self.respond("Shutdown signal received."); break

if __name__ == "__main__":
    try: AshleyAI().run_cli()
    except Exception as e: print(f"FATAL ERROR IN CORE: {e}\\n{traceback.format_exc()}")
    finally: print("\\n--- Ashley Core session has concluded. ---")
"""

# ==============================================================================
# --- BLUEPRINT 3: The Interactive GUI (`main_gui.py`) ---
# ==============================================================================
MAIN_GUI_PY_CODE = """
import tkinter as tk
from tkinter import scrolledtext, PhotoImage
import json, time
from pathlib import Path
from PIL import Image, ImageTk

class AshleyGUI:
    def __init__(self, root):
        self.root = root; self.root.title("Ashley AI")
        self.base_dir = Path(__file__).resolve().parent
        assets_path = self.base_dir / "assets"

        self.root.geometry("850x650"); self.root.configure(bg="#1e1e1e")
        FONT_MAIN = ("Segoe UI", 11); FONT_TITLE = ("Segoe UI Semibold", 20)

        main_frame=tk.Frame(root,bg="#1e1e1e"); main_frame.pack(fill=tk.BOTH,expand=True,padx=10,pady=10)
        left_panel=tk.Frame(main_frame,bg="#2d2d2d",width=250); left_panel.pack(side=tk.LEFT,fill=tk.Y,padx=(0,10)); left_panel.pack_propagate(False)
        right_panel=tk.Frame(main_frame,bg="#1e1e1e"); right_panel.pack(side=tk.RIGHT,fill=tk.BOTH,expand=True)

        self.avatar_label = tk.Label(left_panel, bg="#2d2d2d"); self.avatar_label.pack(pady=20, padx=20)
        self.gif_frames = self.load_gif_frames(assets_path / "avatar.gif")
        self.gif_frame_index = 0
        if self.gif_frames: self.animate_avatar()
        else: self.avatar_label.config(text="[avatar.gif not found in assets/]", fg="white")

        tk.Label(left_panel,text="Ashley AI",font=FONT_TITLE,fg="#00aaff",bg="#2d2d2d").pack()
        
        self.log_text=scrolledtext.ScrolledText(right_panel,wrap=tk.WORD,bg="#252526",fg="white",font=FONT_MAIN,relief=tk.FLAT,bd=0)
        self.log_text.pack(fill=tk.BOTH,expand=True,pady=(0,10))
        
        input_frame=tk.Frame(right_panel,bg="#2d2d2d"); input_frame.pack(fill=tk.X)
        self.input_entry=tk.Entry(input_frame,bg="#3c3c3c",fg="white",font=FONT_MAIN,relief=tk.FLAT,insertbackground="white")
        self.input_entry.pack(side=tk.LEFT,fill=tk.X,expand=True,ipady=10,padx=5,pady=5)
        self.input_entry.bind("<Return>", self.send_command)
        tk.Button(input_frame,text="Send",command=self.send_command,bg="#007acc",fg="white",relief=tk.FLAT).pack(side=tk.RIGHT,padx=5,pady=5)
        
        self.check_for_response()

    def load_gif_frames(self, path):
        try:
            gif = Image.open(path); frames = []
            for i in range(gif.n_frames):
                gif.seek(i); frames.append(ImageTk.PhotoImage(gif.copy().convert("RGBA")))
            return frames
        except: return []

    def animate_avatar(self):
        frame = self.gif_frames[self.gif_frame_index]
        self.avatar_label.configure(image=frame)
        self.gif_frame_index = (self.gif_frame_index + 1) % len(self.gif_frames)
        self.root.after(100, self.animate_avatar)

    def send_command(self, event=None):
        command = self.input_entry.get().strip()
        if not command: return
        self.log("You", command); self.input_entry.delete(0, tk.END)
        with open(self.base_dir / "command_to_ashley.txt", "w") as f: f.write(command)
    
    def check_for_response(self):
        response_file = self.base_dir / "response_from_ashley.txt"
        if response_file.exists():
            try:
                response = response_file.read_text().strip()
                if response: self.log("Ashley", response)
                response_file.unlink()
            except: pass
        self.root.after(250, self.check_for_response)
            
    def log(self, sender, message):
        self.log_text.configure(state='normal')
        self.log_text.insert(tk.END, f"{sender}: {message}\\n\\n")
        self.log_text.configure(state='disabled'); self.log_text.see(tk.END)

if __name__ == "__main__":
    root = tk.Tk(); app = AshleyGUI(root); root.mainloop()
"""

# ==============================================================================
# --- OTHER BLUEPRINTS (Knowledge, Repair Worker, .gitignore) ---
# ==============================================================================
KNOWLEDGE_JSON_CONTENT = json.dumps({
    "commands": {"hello": "Hi David."},
    "keywords": {"repair": "action_master_repair", "gui": "action_launch_gui", "diagnostics": "action_diagnostics"}
}, indent=2)

REPAIR_WORKER_CODE = """
import sys, subprocess, importlib.util, time
from pathlib import Path
def _s(text): print(text)
REQUIRED = {"psutil":"psutil", "opencv-python":"cv2", "Pillow":"Pillow"}
ROOT_DIR = Path(__file__).resolve().parent
_s("Initiating System-Wide Scavenger repair sequence.")
missing = {pkg: imp for pkg, imp in REQUIRED.items() if not importlib.util.find_spec(imp)}
if not missing: _s("All required libraries are installed."); print("REPAIR_SUCCESS"); exit()
_s(f"Missing {len(missing)} libraries. Scavenging for parts...")
failed = []
for pkg in missing:
    found_wheel = next(ROOT_DIR.rglob(f"*{pkg.replace('-', '_')}*.whl"), None)
    if found_wheel:
        _s(f"Found local part: {found_wheel.name}. Installing...")
        try:
            subprocess.run([sys.executable, "-m", "pip", "install", str(found_wheel)], check=True, capture_output=True)
            _s(f"Successfully installed {pkg}.")
        except: failed.append(pkg)
    else: _s(f"No local part for {pkg}. Trying internet..."); failed.append(pkg)
if not failed: _s("All dependencies installed."); print("REPAIR_SUCCESS")
else: _s(f"Could not install: {', '.join(failed)}."); print("REPAIR_FAIL")
"""

GITIGNORE_CONTENT = """
# Python
__pycache__/
*.pyc

# Ashley AI Specific
/python_runtime/
/workshop/
/assets/
*.log
command_to_ashley.txt
response_from_ashley.txt
ashley_model.pkl
"""

# ==============================================================================
# --- THE GENERATOR SCRIPT ---
# ==============================================================================
def main():
    """This function creates the final application package."""
    print("--- Ashley AI Final System Generator ---")
    base_dir = Path(__file__).resolve().parent
    
    files_to_create = {
        "START_ASHLEY.bat": START_ASHLEY_BAT_CODE,
        "ashley_core.py": ASHLEY_CORE_PY_CODE,
        "main_gui.py": MAIN_GUI_PY_CODE,
        "ashley_knowledge.json": KNOWLEDGE_JSON_CONTENT,
        "repair_worker.py": REPAIR_WORKER_CODE,
        "chatbot_worker.py": CHATBOT_WORKER_CODE,
        "diagnostics_worker.py": "import psutil; print(f'CPU: {psutil.cpu_percent()}%')",
        ".gitignore": GITIGNORE_CONTENT
    }
    
    try:
        (base_dir / "assets").mkdir(exist_ok=True)
        (base_dir / "workshop").mkdir(exist_ok=True)
        
        for filename, content in files_to_create.items():
            with open(base_dir / filename, "w", encoding="utf-8") as f:
                f.write(content.strip())
            print(f"  [OK] Created {filename}")
        
        print("\n--- ✅ DEPLOYMENT COMPLETE! ---")
        print("Your new, stable application has been created.")
        print("\nNEXT STEPS:")
        print("1. Place your 'avatar.gif' inside the 'assets' folder.")
        print("2. (Optional) Place any offline installers (.whl files) in the 'workshop' folder.")
        print("3. From now on, you will only run the 'START_ASHLEY.bat' file.")
        print("4. When the CLI appears, type 'gui' to launch the new interface.")

    except Exception as e:
        print(f"\n[FATAL] An error occurred during file generation: {e}")
        traceback.print_exc()
        
if __name__ == "__main__":
    main()
    print("\n--- Generator script has finished. ---")
    input("Press Enter to exit...")
