import sys
import cv2
import os
import numpy as np
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5.QtGui import QImage, QPixmap

from Main.UI.SaveUserImg import Ui_SaveUserImg

from Main.class_file.class_warning_msg import MsgBox
from Main.class_file.class_font import Font


class CaptureUserImage(QWidget, Ui_SaveUserImg):
    SetName = pyqtSignal(str)
    def __init__(self, controller, newbie_name = None):
        super().__init__()

        self.setupUi(self)
        self.set_font()
        self.main = controller
        self.msgbox = MsgBox()
        self.active_name = newbie_name # 이름 사원등록화면에서 가져오기
        self.num_of_images = 0
        self.capture_btn.clicked.connect(self.capimg)
        self.cancel_btn.clicked.connect(self.close)
        self.SetName.connect(self.set_active_name)


    def set_font(self):
        self.title_lab.setFont(Font.title(2))
        self.numimglabel.setFont(Font.text(5))
        self.capture_btn.setFont(Font.button(1))
        self.cancel_btn.setFont(Font.button(1))
        self.user_img.setFont(Font.button(2))


    def set_active_name(self, name):
        self.active_name = name
    @pyqtSlot()
    def capimg(self):
        self.numimglabel.setText("찍힌 사진 = 0")

        # OpenCV를 사용하여 이미지를 캡쳐하고 화면에 보여준다.
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()

        if ret:
            height, width, channel = frame.shape
            bytes_per_line = 3 * width
            q_img = QImage(frame.data, width, height, bytes_per_line, QImage.Format_RGB888).rgbSwapped()
            self.user_img.setPixmap(QPixmap.fromImage(q_img))
            cap.release()

        else:
            msg = '사진 인식 오류입니다.'
            self.msgbox.set_dialog_type(msg=msg)
            self.msgbox.exec_()


        x = self.start_capture(self.active_name)
        self.num_of_images = x
        self.numimglabel.setText(f"찍힌 사진 = {x}")

    def start_capture(self, name):
        current_dir = os.path.dirname(os.path.abspath(__file__))  # 현재 스크립트의 위치
        path = os.path.join(current_dir, "..\..", "img", "face", name)  # 상위 상위 폴더의 img/face/ 하위에 test 폴더의 절대 경로를 구함
        num_of_images = 0
        detector = cv2.CascadeClassifier("../data/haarcascade_frontalface_default.xml")
        try:
            os.makedirs(path)
        except FileExistsError:
            print('폴더가 이미 생성되어 있습니다.')
        vid = cv2.VideoCapture(0)

        while True:
            ret, img = vid.read()
            new_img = None
            grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            face = detector.detectMultiScale(image=grayimg, scaleFactor=1.1, minNeighbors=5)

            for x, y, w, h in face:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 0), 2)
                cv2.putText(img, "Face Detected", (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255))
                # cv2.putText(img, str(str(num_of_images) + " images captured"), (x, y + h + 20),cv2.FONT_HERSHEY_SIMPLEX,0.8, (0, 0, 255))
                new_img = img[y:y + h, x:x + w]

            # img를 PyQt QLabel에 표시
            height, width, channel = img.shape
            bytesPerLine = 3 * width
            qImg = QImage(img.data, width, height, bytesPerLine, QImage.Format_RGB888).rgbSwapped()
            self.user_img.setPixmap(QPixmap.fromImage(qImg))

            key = cv2.waitKey(1) & 0xFF
            try:
                cv2.imwrite(str(path + "/" + str(num_of_images) + name + ".jpg"), new_img)
                num_of_images += 1
            except:

                pass
            if key == ord("q") or key == 27 or num_of_images > 510:
                vid.release()
                self.main.add_emp.face_regist = True
                print(self.main.add_emp.face_regist)
                break
        # self.close()

        cv2.destroyAllWindows()
        return num_of_images



# if __name__ == '__main__':
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     main = CaptureUserImage()
#     main.show()
#     sys.exit(app.exec_())