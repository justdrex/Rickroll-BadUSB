# USB RickRoll — CircuitPython HID Attack

A CircuitPython-based USB HID device that automatically Rick Rolls anyone who plugs it in. Opens a fullscreen, autoplay YouTube video that's nearly impossible to close.

## How it works

When plugged into a Windows PC, the device emulates a keyboard, opens a hidden HTTP server from the drive, and launches a fake "Windows Update" page in the browser. The page plays Rick Astley in fullscreen with all keyboard shortcuts blocked. If the user escapes fullscreen, a fake "Critical System Error" screen forces them to click — which puts them right back into fullscreen.

## Requirements

- Raspberry Pi Pico (or any CircuitPython-compatible board with HID support)
- CircuitPython installed on the board
- `adafruit_hid` library in the `/lib` folder (download from [circuitpython.org/libraries](https://circuitpython.org/libraries))
- Python installed on the target Windows PC (for the HTTP server)
- Target machine must be running Windows

## Files

| File | Description |
|------|-------------|
| `code.py` | Main payload — runs on the Pico, emulates keyboard input |
| `run.bat` | Starts a local HTTP server and opens the rickroll page |
| `rickroll.html` | The Rick Roll page — fullscreen, autoplay, key blocking |

> `boot.py`, `wsgiserver.py`, `webapp.py`, `duckinpython.py` are part of the base CircuitPython/DuckyPython firmware and are **not** part of this project.

## Setup

1. Flash CircuitPython onto your Pico
2. Copy `adafruit_hid` into the `/lib` folder on the CIRCUITPY drive
3. Copy `code.py`, `run.bat`, and `rickroll.html` to the **root** of the CIRCUITPY drive
4. Plug into a Windows PC and watch

## Timing

If the video doesn't start automatically, the target PC may be too slow. Increase the delay in `code.py`:

```python
time.sleep(5)  # increase this value
```

## Disclaimer

This project is intended for **educational purposes and pranks among friends only**. Do not use on devices you don't own or without permission.
