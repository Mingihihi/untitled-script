import keyboard
import pygetwindow as gw
import time
import sys


alt_tab_mode = False 

def activate_alt_tab_mode():
    global alt_tab_mode
    alt_tab_mode = not alt_tab_mode
    if alt_tab_mode:
        print("Chế độ Alt+Tab đã bật. Nhấn Alt+Tab để thoát.")
    else:
        print("Chế độ Alt+Tab đã tắt.")

def check_alt_tab():
    global alt_tab_mode
    while True:
        if alt_tab_mode:
            if keyboard.is_pressed("alt") and keyboard.is_pressed("tab"):
                windows = gw.getWindowsWithTitle("Roblox")
                for win in windows:
                    print(win)
                    if "Roblox" in win.title:
                        win.close()
                        sys.exit()
        time.sleep(0.05)

def main():
    print("Nhấn f10 để vào chế độ.")
    keyboard.add_hotkey("f10", activate_alt_tab_mode)

    try:
        check_alt_tab()
    except KeyboardInterrupt:
        print("Đã thoát chương trình.")

if __name__ == "__main__":
    main()
