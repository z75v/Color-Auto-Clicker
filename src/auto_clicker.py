import pyautogui
from PIL import ImageGrab
import keyboard
import time
import tkinter as tk
from tkinter import simpledialog
import re
import os

# === Theme Configuration ===
APP_NAME = "AutoClicker"
config_dir = os.path.join(os.getenv('LOCALAPPDATA'), APP_NAME)
os.makedirs(config_dir, exist_ok=True)

theme_config_file = os.path.join(config_dir, "theme_config.txt")

theme_colors = {
    "light": {
        "bg": "#ffffff",
        "fg": "#000000",
        "button_bg": "#f0f0f0",
        "button_fg": "#000000"
    },
    "dark": {
        "bg": "#1f2529",  # RGB(31, 37, 41)
        "fg": "#ffffff",
        "button_bg": "#2a2f33",
        "button_fg": "#ffffff"
    }
}

def save_theme_preference(theme):
    with open(theme_config_file, "w") as f:
        f.write(theme)

def load_theme_preference():
    if os.path.exists(theme_config_file):
        with open(theme_config_file, "r") as f:
            return f.read().strip()
    return "light"

# === Core auto clicker settings ===
TARGET_COLOR = (0, 255, 255)
COLOR_TOLERANCE = 10
toggle_key = 't'
shutdown_key = 'q'
clicking_enabled = False
shutdown = False

# === Auto clicker logic ===
def get_pixel_color(x, y):
    screen = ImageGrab.grab()
    return screen.getpixel((x, y))

def color_matches(c1, c2, tolerance):
    return all(abs(a - b) <= tolerance for a, b in zip(c1, c2))

def toggle_clicking():
    global clicking_enabled
    clicking_enabled = not clicking_enabled
    status_label.config(text=f"Clicking: {'ON' if clicking_enabled else 'OFF'}")

def quit_program():
    global shutdown
    shutdown = True
    root.quit()

def is_valid_key(input_string):
    if len(input_string) == 1 and input_string.isalnum():
        return True
    elif re.match(r"^F[1-9]$|^F1[0-2]$", input_string):
        return True
    return False

def is_valid_color_input(color_input):
    pattern = r'^\d{1,3},\d{1,3},\d{1,3}$'
    if re.match(pattern, color_input):
        rgb_values = color_input.split(',')
        return all(0 <= int(val) <= 255 for val in rgb_values)
    return False

# === Custom themed error popup ===
def themed_error_popup(title, message):
    colors = theme_colors[current_theme]
    error_win = tk.Toplevel(root)
    error_win.title(title)
    error_win.config(bg=colors["bg"])
    error_win.resizable(False, False)

    msg_label = tk.Label(error_win, text=message, bg=colors["bg"], fg=colors["fg"])
    msg_label.pack(padx=20, pady=(15, 5))

    def close_popup():
        error_win.destroy()

    ok_button = tk.Button(error_win, text="OK", command=close_popup,
                          bg=colors["button_bg"], fg=colors["button_fg"])
    ok_button.pack(pady=(0, 15))

def update_color():
    global TARGET_COLOR
    color_input = simpledialog.askstring("Update Color", "Enter the target color (e.g., 255,0,0):")
    while color_input and not is_valid_color_input(color_input):
        themed_error_popup("Invalid Color Format", "Color must be in format XXX,XXX,XXX (0-255)")
        color_input = simpledialog.askstring("Update Color", "Enter the target color (e.g., 255,0,0):")

    if color_input:
        TARGET_COLOR = tuple(map(int, color_input.split(',')))
        color_label.config(text=f"Target Color: {TARGET_COLOR}")

def update_toggle_key():
    global toggle_key
    new_key = simpledialog.askstring("Update Toggle Key", "Enter toggle key (letter, number, or F1-F12):")
    while new_key and not is_valid_key(new_key):
        themed_error_popup("Invalid Toggle Key", "Toggle key must be a letter, number, or F1-F12.")
        new_key = simpledialog.askstring("Update Toggle Key", "Enter toggle key (letter, number, or F1-F12):")

    if new_key:
        toggle_key = new_key
        toggle_key_label.config(text=f"Toggle Key: {toggle_key}")

def update_shutdown_key():
    global shutdown_key
    new_key = simpledialog.askstring("Update Quit Key", "Enter quit key (letter, number, or F1-F12):")
    while new_key and not is_valid_key(new_key):
        themed_error_popup("Invalid Quit Key", "Quit key must be a letter, number, or F1-F12.")
        new_key = simpledialog.askstring("Update Quit Key", "Enter quit key (letter, number, or F1-F12):")

    if new_key:
        shutdown_key = new_key
        shutdown_key_label.config(text=f"Quit Key: {shutdown_key}")

def run_clicker():
    global shutdown, clicking_enabled
    if shutdown:
        return

    if clicking_enabled:
        current_x, current_y = pyautogui.position()
        current_color = get_pixel_color(current_x, current_y)
        if color_matches(current_color, TARGET_COLOR, COLOR_TOLERANCE):
            pyautogui.click(current_x, current_y)

    if keyboard.is_pressed(toggle_key):
        toggle_clicking()
        time.sleep(0.5)

    if keyboard.is_pressed(shutdown_key):
        quit_program()

    root.after(50, run_clicker)

# === Theme toggling ===
def apply_theme(theme):
    colors = theme_colors[theme]
    root.config(bg=colors["bg"])
    for widget in root.winfo_children():
        if isinstance(widget, tk.Label):
            widget.config(bg=colors["bg"], fg=colors["fg"])
        elif isinstance(widget, tk.Button):
            widget.config(bg=colors["button_bg"], fg=colors["button_fg"], activebackground=colors["button_bg"])

def toggle_theme():
    global current_theme
    current_theme = "dark" if current_theme == "light" else "light"
    apply_theme(current_theme)
    save_theme_preference(current_theme)

# === GUI Setup ===
root = tk.Tk()
root.title("Auto Clicker Settings")

current_theme = load_theme_preference()

color_label = tk.Label(root, text=f"Target Color: {TARGET_COLOR}")
color_label.pack(pady=5)
color_button = tk.Button(root, text="Update Color", command=update_color)
color_button.pack(pady=5)

toggle_key_label = tk.Label(root, text=f"Toggle Key: {toggle_key}")
toggle_key_label.pack(pady=5)
toggle_key_button = tk.Button(root, text="Update Toggle Key", command=update_toggle_key)
toggle_key_button.pack(pady=5)

shutdown_key_label = tk.Label(root, text=f"Quit Key: {shutdown_key}")
shutdown_key_label.pack(pady=5)
shutdown_key_button = tk.Button(root, text="Update Quit Key", command=update_shutdown_key)
shutdown_key_button.pack(pady=5)

toggle_button = tk.Button(root, text="Toggle Clicker", command=toggle_clicking)
toggle_button.pack(pady=5)

quit_button = tk.Button(root, text="Quit", command=quit_program)
quit_button.pack(pady=5)

theme_toggle_button = tk.Button(root, text="Toggle Theme", command=toggle_theme)
theme_toggle_button.pack(pady=5)

status_label = tk.Label(root, text="Clicking: OFF")
status_label.pack(pady=5)

apply_theme(current_theme)

root.after(100, run_clicker)
root.mainloop()
