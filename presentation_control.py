import pyautogui

class PresentationControl:
    def __init__(self):
        pyautogui.PAUSE = 0.2

    def control_presentation(self, gesture):
        if gesture == "next":
            pyautogui.press("right")
            print("👉 Next Slide")
        elif gesture == "previous":
            pyautogui.press("left")
            print("👈 Previous Slide")
        elif gesture == "start":
            pyautogui.press("f5")
            print("🚀 Presentation Started")
        elif gesture == "stop":
            pyautogui.press("esc")
            print("🛑 Presentation Stopped")
