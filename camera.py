import cv2

class Camera:
    def __init__(self, camera_index=0):
        self.camera_index = camera_index
        self.cap = None

    def start(self):
        self.cap = cv2.VideoCapture(self.camera_index)
        if not self.cap.isOpened():
            raise Exception("Camera could not be opened.")

    def get_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            return None
        return frame

    def stop(self):
        if self.cap:
            self.cap.release()
        cv2.destroyAllWindows()
