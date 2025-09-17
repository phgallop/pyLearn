import time
import win32gui
import win32con

#variables - window, key and interval
WINDOW_NAME = "example"
KEY_W = 0x57
INTERVAL = 5

def get_window_handle(title_part): #gets window name
    def enum_windows(hwnd, result):
        if win32gui.IsWindowVisible(hwnd) and title_part.lower() in win32gui.GetWindowText(hwnd).lower():
            result.append(hwnd)
    result = []
    win32gui.EnumWindows(enum_windows, result)
    return result[0] if result else None

def send_key(hwnd, key_code): #sends pressed key
    win32gui.PostMessage(hwnd, win32con.WM_KEYDOWN, key_code, 0)
    time.sleep(0.05)
    win32gui.PostMessage(hwnd, win32con.WM_KEYUP, key_code, 0)

hwnd = get_window_handle(WINDOW_NAME)
if not hwnd:
    print(f"❌ Window '{WINDOW_NAME}' not found ❌")
    exit()

print(f"✅ Window found: '{win32gui.GetWindowText(hwnd)}' ✅")

try:
    while True:
        send_key(hwnd, KEY_W)
        print(f"Key pressed on {win32gui.GetWindowText(hwnd)}")
        time.sleep(INTERVAL)

except KeyboardInterrupt:
    print("Interrupted.")
