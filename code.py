import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

time.sleep(2)

kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)

# Open Run dialog
kbd.press(Keycode.WINDOWS, Keycode.R)
kbd.release_all()
time.sleep(0.6)

# Launch run.bat
layout.write("D:\\run.bat")
kbd.press(Keycode.ENTER)
kbd.release_all()

# Wait for browser to open and load the page
time.sleep(5)

# Press F to trigger autoplay + fullscreen (works without mouse focus)
kbd.press(Keycode.F)
kbd.release_all()