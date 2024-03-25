import pyautogui
import time

# Define the keyboard shortcuts
screenshot_hotkey = ['winleft', 'prtscr']
switch_tab_hotkey = 'ctrlleft'
switch_tab_release = 'tab'

# Number of tabs to switch
num_tabs = 14

# Take screenshot using the specified hotkey
# pyautogui.hotkey(*screenshot_hotkey)
time.sleep(3)  # Wait for the screenshot to be taken

# Switch to the next tab using Ctrl + Tab
for _ in range(num_tabs):
    pyautogui.hotkey(*screenshot_hotkey)
    time.sleep(1)  # Add a small delay to ensure the tab switch is complete
    
    pyautogui.hotkey(switch_tab_hotkey, switch_tab_release)
    # Take screenshot using the specified hotkey
    time.sleep(1)  # Wait for the screenshot to be taken
