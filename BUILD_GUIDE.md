# BUILD GUIDE - Unified Solar Time (UST) Clock

## Create Your Windows Executable (.exe)

### Option 1: Automated Build (Easiest)

1. **Download the repository**
   ```bash
   git clone https://github.com/jordon-sudo/unified-solar-time.git
   cd unified-solar-time
   ```

2. **Run the build script**
   - Double-click `build_exe.bat`
   - Wait for it to complete
   - Your `.exe` is ready in the `dist/` folder!

3. **Launch the app**
   ```
   dist/Unified Solar Time.exe
   ```

### Option 2: Manual Build with PyInstaller

1. **Install PyInstaller**
   ```bash
   pip install pyinstaller
   ```

2. **Build the executable**
   ```bash
   pyinstaller --onefile --windowed --name "Unified Solar Time" ust_clock.py
   ```

3. **Find your app**
   - Look in the `dist/` folder
   - File: `Unified Solar Time.exe`

### Option 3: Run as Python Script (No Build Needed)

If you just want to run it without building:

1. **Install Python 3.7+** from https://python.org/

2. **Run directly**
   ```bash
   python ust_clock.py
   ```

---

## What You Get

✓ **Standalone Windows Application**
- No installation required
- Works offline
- Single executable file
- Can be placed anywhere

✓ **Desktop Clock**
- Shows current time (standard and UST)
- Real-time updates
- Professional UI
- Dark theme

✓ **Time Converter**
- Enter any standard time
- See UST equivalent instantly
- Input validation

---

## System Requirements

- **Windows 7 or later**
- **No Python installation needed** (if using .exe)
- **No internet connection needed**
- **~50 MB disk space** (for the executable)

---

## Installation & Setup

### Quick Setup (5 minutes)

1. Clone/download the repository
2. Run `build_exe.bat`
3. Copy `dist/Unified Solar Time.exe` to your Desktop
4. Double-click to run!

### Create Desktop Shortcut

1. Locate `Unified Solar Time.exe`
2. Right-click → Create shortcut
3. Move shortcut to Desktop

### Pin to Start Menu (Windows 10/11)

1. Right-click the .exe
2. Select "Pin to Start"
3. Find the tile in your Start Menu

### Autostart on Windows Login

1. Press `Win + R`
2. Type `shell:startup`
3. Copy the shortcut into this folder
4. App launches automatically on next login

---

## Time Display Format

**Important: Hours are WHOLE NUMBERS (0-9), not decimals**

Example displays:
- `0.0000 S` = Midnight
- `5.0000 S` = Noon
- `9.9999 S` = End of day

Format: `H.MMSS` where:
- **H** = Centisol (0-9)
- **M** = Millisol (00-99)
- **S** = Microsol (00-99)
- **S** = Sol symbol

---

## Troubleshooting

### "Python not found"
- Install Python 3.7+ from https://python.org/
- Check "Add Python to PATH" during installation

### Build script doesn't work
- Use Command Prompt (not PowerShell)
- Run from the project directory
- Ensure you have internet (for pip install)

### App crashes on startup
- Try running as Administrator
- Check your Python version: `python --version`
- Delete `build/` and `dist/` folders, rebuild

### PyInstaller installation fails
- Try: `python -m pip install pyinstaller`
- Or: `pip install --upgrade pyinstaller`

---

## Customization

Edit `ust_clock.py` to customize:

**Colors** - Find this section and change hex codes:
```python
style.configure("Time.TLabel", background="#34495e", foreground="#2ecc71",
               font=("Courier New", 48, "bold"))
```

**Window size** - Change this line:
```python
self.root.geometry("700x500")  # width x height
```

**Title** - Change this line:
```python
self.root.title("Unified Solar Time (UST) Clock")
```

After editing, rebuild with `build_exe.bat`

---

## Build Output Structure

After running `build_exe.bat`:

```
unified-solar-time/
├── ust_clock.py              (Source code)
├── build_exe.bat             (Build script)
├── build/                    (Build artifacts - can delete)
├── dist/                     (Your executable folder)
│   └── Unified Solar Time.exe (YOUR APP!)
└── ust_clock.spec            (Build configuration)
```

You only need the `.exe` file to distribute.

---

## Distribution

To share your app:

1. Build it: `build_exe.bat`
2. Find: `dist/Unified Solar Time.exe`
3. Share the `.exe` file with others
4. They can run it directly (no installation needed)

---

## Advanced Options

### Add an Icon

1. Create a 256×256 icon (`.ico` format)
2. Place it in the project folder
3. Update the build command:
   ```bash
   pyinstaller --onefile --windowed --icon=myicon.ico ust_clock.py
   ```

### Create an Installer

For professional distribution, use NSIS or Inno Setup:
- https://nsis.sourceforge.io/
- https://jrsoftware.org/isinfo.php

### Code Signing

For production releases, sign your .exe for Windows SmartScreen bypass.

---

## Support

- **Issues?** Open an issue on GitHub
- **Questions?** Check the README.md
- **Customization help?** Edit ust_clock.py or ask for assistance

---

## Version Information

- **App Version:** 1.0
- **Python Version:** 3.7+
- **PyInstaller Version:** 5.0+
- **Windows Support:** Windows 7 and later

---

**You now have a complete, standalone Windows desktop application!** ⊙

Happy time converting!
