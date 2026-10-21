# Windows Setup Guide - Unified Solar Time Clock

Complete instructions to run the Unified Solar Time (UST) clock on your Windows PC.

## Quick Start (30 seconds)

1. **Download** the `index.html` file from the GitHub repository
2. **Double-click** `index.html` to open it in your default browser
3. **Done!** Your UST clock is running

---

## Method 1: Simple Browser Launch (Recommended)

### Step-by-Step:

1. **Clone or Download the Repository**
   ```bash
   git clone https://github.com/jordon-sudo/unified-solar-time.git
   ```
   Or download as ZIP and extract

2. **Open in Browser**
   - Right-click on `index.html`
   - Select "Open with" → Choose your browser (Chrome, Firefox, Edge, etc.)
   - The clock starts immediately

3. **That's it!** The app is now running

### Notes:
- No installation required
- No internet connection needed (fully offline)
- Works in any modern browser
- Updates automatically every second

---

## Method 2: Create Desktop Shortcut

### Make it Easy to Launch:

1. **Locate the `index.html` file**
2. **Right-click** on it
3. **Select "Create shortcut"**
4. **Move the shortcut** to your Desktop
5. **Double-click the shortcut** anytime to launch

**To customize the shortcut icon:**
- Right-click shortcut → Properties
- Click "Change Icon"
- Browse to find an icon you like (or download a sun icon)

---

## Method 3: Pin to Start Menu (Windows 10/11)

1. **Create a shortcut** (see Method 2)
2. **Right-click the shortcut**
3. **Select "Pin to Start"**
4. **Find the tile in your Start Menu**
5. **Click it anytime** to launch your UST clock

---

## Method 4: Create a Batch File Launcher

For a more "app-like" experience:

### Create `LaunchUST.bat`:

1. **Open Notepad**
2. **Paste this code:**
   ```batch
   @echo off
   REM Unified Solar Time Clock Launcher
   start "" "%~dp0index.html"
   ```
3. **Save as:** `LaunchUST.bat` (in the same folder as `index.html`)
4. **Double-click** `LaunchUST.bat` to launch

**Optional:** Right-click → Create shortcut for an extra quick-launch icon

---

## Method 5: Advanced - Nativefier (True Desktop App)

Convert to a standalone Windows executable:

### Prerequisites:
- Node.js installed (https://nodejs.org/)
- Command Prompt or PowerShell

### Steps:

1. **Open Command Prompt** and navigate to your project folder:
   ```bash
   cd C:\path\to\unified-solar-time
   ```

2. **Install Nativefier globally:**
   ```bash
   npm install -g nativefier
   ```

3. **Create the executable:**
   ```bash
   nativefier --name "Unified Solar Time" --icon sun.png "file://%cd%/index.html"
   ```
   (Replace `sun.png` with an icon path, or omit `--icon` to use default)

4. **Find your app:**
   - A new folder called `Unified Solar Time-win32-x64` appears
   - Inside is `Unified Solar Time.exe`
   - **Double-click to run!**

5. **Optional:** Copy the `.exe` to your Desktop or Programs folder

**Advantages:**
- Looks like a native Windows app
- Runs in its own window
- Can pin to taskbar and Start Menu
- Single-click launch

---

## Method 6: Windows Portable App (Using Chromium)

Alternative to Nativefier:

1. **Download Portable Chromium** from https://chromium.woolyss.com/
2. **Extract to a folder**
3. **Create a shortcut** to `chrome.exe`
4. **In the Target field, add:**
   ```
   --app=file:///C:/path/to/index.html
   ```
5. **Launch and enjoy!**

---

## Browser-Specific Tips

### Microsoft Edge
- Best Windows integration
- Auto-updates with Windows
- Pin to Start Menu support
- Command: `start msedge file:///path/to/index.html`

### Google Chrome
- Fast and responsive
- Good memory management
- Good add-on ecosystem
- Command: `start chrome file:///path/to/index.html`

### Firefox
- Privacy-focused
- Good offline support
- Smooth animations
- Command: `start firefox file:///path/to/index.html`

---

## Troubleshooting

### Clock not updating?
- Refresh the page (F5)
- Clear browser cache
- Try a different browser

### File won't open?
- Make sure file is saved as `.html` (not `.txt`)
- Right-click → "Open with" → Choose specific browser
- Check file permissions

### Shortcut not working?
- Verify the path in shortcut target
- Use full path: `C:\Users\YourName\Documents\index.html`
- Check for spaces in folder names

### Converter giving wrong results?
- Verify input time format (00-23 hours, 00-59 min/sec)
- Clear the calculator and re-enter values
- Refresh page

---

## System Requirements

✓ **Operating System:** Windows 7 or later (Windows 10/11 recommended)  
✓ **Browser:** Chrome, Edge, Firefox, or Safari  
✓ **Memory:** < 50 MB  
✓ **Disk Space:** < 15 KB  
✓ **Internet:** Not required  
✓ **Administrator:** Not required  

---

## File Information

- **File Name:** `index.html`
- **File Size:** ~11 KB
- **Format:** Standalone HTML + CSS + JavaScript
- **Dependencies:** None
- **License:** Open Source (MIT)

---

## Advanced Configuration

### Use a Local Web Server (Optional)

For advanced users, you can serve via local Python web server:

```bash
# Navigate to project folder
cd C:\path\to\unified-solar-time

# Python 3
python -m http.server 8000

# Then visit: http://localhost:8000
```

---

## Frequently Asked Questions

**Q: Does it need internet?**  
A: No, it runs completely offline.

**Q: Can I modify it?**  
A: Yes! Edit `index.html` with any text editor to customize colors, fonts, layout, etc.

**Q: Will it run on older Windows?**  
A: Needs Windows 7 or later with a modern browser.

**Q: Can I use it on my phone?**  
A: Yes, but open `index.html` in a phone browser or email it to yourself.

**Q: How do I update it?**  
A: Download the latest `index.html` from GitHub and replace your copy.

---

## Tips & Tricks

### Hide the Title Bar
Edit the HTML and add to the `<body>` tag:
```html
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
```

### Dark Mode
Edit the CSS `body` background gradient to:
```css
background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
```

### Always On Top
Use external tools like [AlwaysTopmost](https://www.softorino.com/alwaystopmost-always-on-top/) or [Keep in View](https://github.com/davisfrancis/KeepInView)

### Autostart on Windows Login
1. Press `Win + R`
2. Type `shell:startup`
3. Copy your shortcut into this folder
4. Clock will launch automatically at startup

---

## Support & Issues

- **GitHub Issues:** https://github.com/jordon-sudo/unified-solar-time/issues
- **Feature Requests:** Open an issue with your idea
- **Bug Reports:** Include your Windows version and browser

---

## Next Steps

- **Customize** the colors and layout by editing `index.html`
- **Share** the app with colleagues and friends
- **Contribute** improvements back to the GitHub project
- **Learn** about Unified Solar Time in `SYSTEM.md`

---

**Happy Solar Time Tracking!** ⊙

*Unified Solar Time (UST) - A Metric Time System*  
*Created: 2026 | Dublow Digital*
