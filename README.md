# Color Based Auto Clicker

An auto clicker tool that allows users to automate clicks when cursor is above a target color. The Auto Clicker is fully customizable and includes features like a toggleable on/off switch, color detection, and customizable hotkeys for toggle and quit actions.

## Features

- **Color Based**: This Autoclicker runs off a target color that you choose via RGB, when ever your mouse hovers over the target color it clicks
- **Toggleable**: An Autoclicker wouldnt be very practical if it weren't toggelable. So it has that feature! And you can customize the toggle button.
- **Themes**: In the interface you can choose between dark and light to soothe your eyes!
- **Compatiable**: This Autoclicker is compatiable with both Windows and macOS but mained for Windows (CONTACT FOR MAC ISSUES)


## Installation

### Requirements

Before you can run the auto clicker, you will need to install some Python libraries | **ONLY IF DOWNLOADING VIA SOURCE/UNCOMPILED**

- `pyautogui`
- `pillow`
- `keyboard`
- `tkinter` (usually pre-installed with python) 

To install the libraries, run:

```
pip install pyautogui pillow keyboard
```

### Downloading and Running
Download the latest release via the github release page.

Run the application:

Windows: Double-click the file to Launch the Auto Clicker

macOS: Open the .app file or run the script directly if Python version in use.


### Usage
Once launched the interface for the Auto Clicker will appear:

Target Color: Set the target-color that the clicker looks for(Default is Aqua)

Toggle Key: Set the hotkey to toggle the Autoclicker

Quit Key: Sets the hotkey to quit/stop the Autoclicker entirely.

Update Color: Allows you to change the target color(RGB Values)

Use the "Toggle Clicker" button to start or stop the Autoclicker. The "Quit" button will stop and exit the program.

### Hotkeys
Toggle Key: Press the set key to toggle the Autoclicker

Quit Key: Press the set key to stop and quit the program.

### Themes
Light Mode: Default theme for a bright, but clean GUI.

Dark Mode: A dark theme to reduce flashbanging.

### Troubleshooting
If the program isn't finding and clicking at the right color properly: Ensure that the color you've set it to is accurate. | CHANGING COLOR TOLERANCE COMING WITH FUTURE RELEASES

Hotkey issues: Make sure you're pressing the set key, and that no other open programs are interfere with your input.

Windows Users: If the .exe file doesn't work, ensure you have the correct Python requirements installed. | ONLY IF IN USE VIA UNCOMPILED/SOURCE CODE 

### License
This project is licensed under the MIT License - see the LICENSE file for details.

### Contributing 
We welcome your contributions! Please open an issue or submit a pull if you discover a bug or would like to recommend features.

Create a fork in the repository.

For your feature or bug fix, create a branch.

Put your changes into effect via a commit

Push your fork.

Send in a pull along with a detailed explanation of the changes.

### Acknowledgments
Thanks to the contributors for their improvements and suggestions.

This project uses the pyautogui, pillow, and keyboard libraries for keyboard inputs and screen interactions.
