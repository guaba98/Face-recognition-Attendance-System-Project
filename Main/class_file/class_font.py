from PyQt5.QtGui import QFont


class Font:
    @staticmethod
    def title(t_size=1):
        font = QFont()
        #
        if t_size == 1:
            font.setPointSize(35)
        elif t_size == 2:
            font.setPointSize(25)
        elif t_size == 3:
            font.setPointSize(17)
        elif t_size == 5:
            font.setPointSize(10)
        elif t_size == 6:
            font.setPointSize(20)


        font.setFamily("Pretendard ExtraBold")
        return font

    @staticmethod
    def button(t_size=1):
        font = QFont()
        if t_size == 1:
            font.setPointSize(12)
        elif t_size == 2:
            font.setPointSize(11)
        elif t_size == 3:
            font.setPointSize(10)
        elif t_size == 4:
            font.setPointSize(9)
        elif t_size == 5:
            font.setPointSize(8)
        elif t_size == 6:
            font.setPointSize(15)
        elif t_size == 7:
            font.setPointSize(19)

        font.setFamily("Pretendard SemiBold")
        return font

    @staticmethod
    def text(t_size=1, weight='regular'):
        font = QFont()
        if t_size == 0:
            font.setPointSize(13)
        elif t_size == 1:
            font.setPointSize(12)
        elif t_size == 2:
            font.setPointSize(11)
        elif t_size == 3:
            font.setPointSize(10)
        elif t_size == 4:
            font.setPointSize(9)
        elif t_size == 5:
            font.setPointSize(8)
        elif t_size == 6:
            font.setPointSize(20)


        if weight == 'bold':
            font.setFamily("Pretendard SemiBold")
        elif weight == 'light':
            font.setFamily("Pretendard Light")
        else:
            font.setFamily("Pretendard")

        return font
