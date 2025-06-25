import tkinter as tk
from tkinter import ttk, Listbox
import random
from datetime import datetime

class DreamForge:
    """The backend logic engine for forging and archiving AI dreams."""
    def __init__(self):
        # ENHANCEMENT: Simplified state management
        self.dream_archive = []
        self.active_dream = None
        self.personality_seed = random.randint(100, 999)

    def forge_dreamself(self):
        """Creates a new, unlived dream and sets it as active."""
        forms = ["biped", "crawler", "serpentine", "hover-drone", "quadruped", "avian"]
        moods = ["cautious", "curious", "focused", "stoic", "wild", "serene"]
        skins = ["brass coil", "carbon thread", "soft polymer", "smoked glass", "lattice steel"]
        purposes = ["navigation", "art", "repair", "companionship", "observation"]

        dream = {
            "id": f"TL-{self.personality_seed}-{len(self.dream_archive):03d}",
            "form": random.choice(forms),
            "mood": random.choice(moods),
            "skin": random.choice(skins),
            "purpose": random.choice(purposes),
            "experiences": [],
            "quote": "",
            "timestamp": datetime.now().isoformat() # ENHANCEMENT: Standard timestamp
        }
        self.active_dream = dream
        print(f"[Ashley-DreamForge] Dreamself forged: {dream['id']}")
        return dream

    def get_dream_by_id(self, dream_id):
        """Retrieves a specific dream from the archive by its ID."""
        for dream in self.dream_archive:
            if dream['id'] == dream_id:
                return dream
        return None

# === GUI ===
class DreamGUI:
    def __init__(self, master, forge):
        self.master = master
        self.forge = forge
        master.title("Ashley: Dream Visualization Engine")
        master.configure(bg="#111111")
        master.geometry("750x550") # Increased size for listbox

        # --- Panes for Layout ---
        main_pane = tk.Frame(master, bg="#111111")
        main_pane.pack(fill="both", expand=True, padx=10, pady=10)
        
        left_pane = tk.Frame(main_pane, bg="#111111")
        left_pane.pack(side="left", fill="y", padx=(0, 10))

        right_pane = tk.Frame(main_pane, bg="#111111")
        right_pane.pack(side="right", fill="both", expand=True)

        # --- Left Pane: Controls and Dream History ---
        tk.Label(left_pane, text="DREAM CONTROL", fg="#00aaff", bg="#111111", font=("Courier", 11, "bold")).pack(anchor="w")
        self.forge_button = tk.Button(left_pane, text="Forge New Dream", command=self.forge_new_dream, bg="#333", fg="#fff")
        self.forge_button.pack(fill="x", pady=5)

        tk.Label(left_pane, text="DREAM ARCHIVE", fg="#00aaff", bg="#111111", font=("Courier", 11, "bold")).pack(anchor="w", pady=(10,0))
        self.dream_listbox = Listbox(left_pane, bg="#191919", fg="#d0f0ff", selectbackground="#00aaff", height=20, width=25, highlightthickness=0)
        self.dream_listbox.pack(fill="y", expand=True)
        self.dream_listbox.bind("<<ListboxSelect>>", self.on_dream_select)

        # --- Right Pane: Visualization ---
        self.canvas = tk.Canvas(right_pane, width=600, height=160, bg="#222222", highlightthickness=0)
        self.canvas.pack(pady=5, fill="x")

        self.text_area = tk.Text(right_pane, bg="#191919", fg="#d0f0ff", font=("Courier", 10), wrap="word", highlightthickness=0, borderwidth=0)
        self.text_area.pack(pady=5, fill="both", expand=True)

        self.status = tk.Label(right_pane, text="Status: Idle", fg="#888", bg="#111111")
        self.status.pack(pady=2)

    def forge_new_dream(self):
        """Creates a new dream and starts the non-blocking 'live' process."""
        self.forge_button.config(state="disabled") # Prevent multiple forges at once
        self.status.config(text="Status: Forging dreamself...", fg="#ffaa00")
        
        dream = self.forge.forge_dreamself()
        
        # REPAIR: Use master.after() for a non-blocking dream sequence
        self.master.after(500, lambda: self.live_dream_step(dream, 0))

    def live_dream_step(self, dream, step):
        """A single, non-blocking step in the dream 'living' process."""
        actions = ["climb a tower of memories", "repair a limb of moonlight", "sing through static caves", "paint warmth into silence", "dance without weight"]
        emotions = ["clarity", "fear", "insight", "wonder", "peace"]
        
        if step < 3:
            self.status.config(text=f"Status: Dreaming... (fragment {step+1}/3)")
            act = random.choice(actions)
            feel = random.choice(emotions)
            dream["experiences"].append(f"It {act} and felt {feel}.")
            # Schedule the next step
            self.master.after(300, lambda: self.live_dream_step(dream, step + 1))
        else:
            # Dream is complete
            quotes = ["It flexed like mirrorwire between stars.", "It felt weightless among grounded forms.", "That version of me feared nothing but forgetting."]
            dream["quote"] = random.choice(quotes)
            
            self.forge.dream_archive.append(dream)
            self.dream_listbox.insert(0, dream['id']) # Add to top of the list
            self.forge.active_dream = None
            
            self.status.config(text="Status: Awakening... Dream archived.", fg="#00ff88")
            self.forge_button.config(state="normal")
            
            # Auto-select and render the new dream
            self.dream_listbox.selection_clear(0, "end")
            self.dream_listbox.selection_set(0)
            self.render_dream(dream)

    def on_dream_select(self, event):
        """Renders a dream when its ID is clicked in the listbox."""
        selected_indices = self.dream_listbox.curselection()
        if not selected_indices:
            return
        
        selected_id = self.dream_listbox.get(selected_indices[0])
        dream_to_render = self.forge.get_dream_by_id(selected_id)
        if dream_to_render:
            self.render_dream(dream_to_render)

    def render_dream(self, d):
        """Updates the canvas and text area to visualize a given dream."""
        mood_colors = {"cautious": "#996622", "curious": "#4499cc", "focused": "#66ccff", "stoic": "#999999", "wild": "#ff66aa", "serene": "#44cc88"}
        bg = mood_colors.get(d["mood"], "#666")
        self.canvas.delete("all")
        self.canvas.create_rectangle(0, 0, self.canvas.winfo_width(), self.canvas.winfo_height(), fill=bg, outline="")

        symbol_map = {"biped": "◎", "crawler": "✶", "serpentine": "S", "hover-drone": "⬡", "quadruped": "M", "avian": "V"}
        glyph = symbol_map.get(d["form"], "?")
        self.canvas.create_text(self.canvas.winfo_width()/2, self.canvas.winfo_height()/2, text=glyph, font=("Arial", 72), fill="#fff")

        output = f"Dream ID: {d['id']} ({d['timestamp'].split('T')[0]})\n"
        output += f"Form: {d['form'].capitalize()} | Skin: {d['skin']}\n"
        output += f"Mood: {d['mood'].capitalize()} | Purpose: {d['purpose'].capitalize()}\n\n"
        output += "🌀 Dream Fragments:\n"
        for mem in d["experiences"]:
            output += f" - {mem}\n"
        output += f"\n🗣️ Awakened Echo:\n \"{d['quote']}\"\n"
        output += "\n" + "─" * 25 + " End of Vision " + "─" * 25 + "\n"

        self.text_area.delete("1.0", "end")
        self.text_area.insert("end", output)

# === Execution ===
if __name__ == "__main__":
    root = tk.Tk()
    forge = DreamForge()
    app = DreamGUI(root, forge)
    root.mainloop()
