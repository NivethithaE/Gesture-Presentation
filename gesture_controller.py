import pyautogui
import time

class GestureController:
    def __init__(self):
        self.last_gesture = None
        self.gesture_time = 0
        self.cooldown = 1  # seconds

    def detect_gesture(self, lm_list):
        thumb_tip = lm_list[4][2]  
        index_tip = lm_list[8][2]  

        if index_tip < thumb_tip:
            return 'next'
        else:
            return 'prev'

    def perform_action(self, gesture):
        current_time = time.time()
        if gesture and (gesture != self.last_gesture or current_time - self.gesture_time > self.cooldown):
            if gesture == 'next':
                pyautogui.press('right')
            elif gesture == 'prev':
                pyautogui.press('left')
            elif gesture == 'start':
                pyautogui.press('f5')  # start slideshow
            elif gesture == 'stop':
                pyautogui.press('esc')  # stop slideshow

            self.last_gesture = gesture
            self.gesture_time = current_time
