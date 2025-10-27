import cv2
from modules.hand_detector import HandDetector
from modules.gesture_controller import GestureController

def main():
    cap = cv2.VideoCapture(0)
    detector = HandDetector()
    controller = GestureController()

    while True:
        success, frame = cap.read()
        if not success:
            break

        # Flip the camera horizontally (mirror effect)
        frame = cv2.flip(frame, 1)

        # Detect hands and landmarks
        frame = detector.findHands(frame)
        lm_list = detector.findPosition(frame)

        gesture = None
        if lm_list:
            gesture = controller.detect_gesture(lm_list)
            controller.perform_action(gesture)

            # Display gesture on the screen
            if gesture:
                cv2.putText(frame, f'Gesture: {gesture}', (10, 70), 
                            cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 3)

        # Show camera feed
        cv2.imshow("Gesture Controlled PPT", frame)

        # Press 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
