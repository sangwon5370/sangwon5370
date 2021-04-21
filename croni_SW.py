import sys
from PyQt5.QtWidgets import *
from PyQt5.Qt import *
from PyQt5.QtGui import *

qss = """
    QLabel {
        color: rgb(100, 100, 100);
    }
    QPushButton {
        color: rgb(100, 0, 0);
    }
    QPushButton:hover {
        color: rgb(255, 255, 255);
        background-color: rgb(0, 0, 0);
    }

    QPushButton#start {
        color: rgb(250, 0, 100);
    }
    QPushButton#start:hover {
        color: rgb(100, 100, 100);
        background-color: rgb(250, 200, 20);
    }
    QProgressBar {
        color: rgb(250, 0, 100);
        border: 1px solid grey;
        border-radius: 8px;
        background-color: rgb(200,200,200); 
    }
     QProgressBar::chunk {
     background-color: rgb(20,20,20);
     border-radius: 8px;
     }

"""


class SubWindow(QWidget):
    def __init__(self, parent=None):
        super(SubWindow, self).__init__()
        self.setWindowTitle('SubWindow')
        self.setStyleSheet(qss)

        self.move(200, 200)
        self.resize(400, 200)


class MyBtn(QPushButton):
    def __init__(self, parent, txt_name='', prop=''):
        super(MyBtn, self).__init__(parent=parent)
        self.parent = parent  # parent 뭐죵? 왜 쓰는거죵?
        # self.setGeometry(x, y, 100, 100)
        self.setObjectName(prop)
        self.setText(txt_name)
        self.click_count = 0

    def mousePressEvent(self, e) -> None:
        print(f'{self} Click !! {self.click_count}')
        self.click_count += 1


class MyLabel(QLabel):
    qss = """
        QLabel#AlarmItemInfo {
            background: rgb(62, 72, 84);
            border-radius: 3px;
            font-size: 11px;
            color: rgb(255, 255, 255);
        }

        QLabel#AlarmItemInfo:hover {
            background: rgb(255, 193, 7);
            color: rgb(31, 39, 42);
        }

        QLabel#AlarmItemInfo:selected {
            background: rgb(255, 193, 7);
            color: rgb(31, 39, 42);
        }
    """

    def __init__(self, parent, txt_name='', prop=''):
        super(MyLabel, self).__init__(parent=parent)
        self.setAttribute(Qt.WA_StyledBackground, True)  # 상위 스타일 상속
        self.parent = parent
        self.setStyleSheet(self.qss)
        self.setObjectName(prop)
        self.setText(txt_name)
        # self.dis_update(alarm_info)

        # def dis_update(self, alarm_name):
        #     """ 알람 정보 디스플레이 업데이트 """
        #     self.setText(alarm_name)
        self.setAlignment(Qt.AlignVCenter | Qt.AlignCenter)  # 텍스트 정렬


class ProgressbarBtn(QProgressBar):
    def __init__(self, parent, x, y, prop=''):
        super(ProgressbarBtn, self).__init__(parent=parent)
        self.parent = parent
        self.setGeometry(x, y, 100, 100)
        self.setObjectName(prop)
        # 숫자값의 위치
        self.setAlignment(Qt.AlignCenter)

    def mousePressEvent(self, e) -> None:
        SubWindow(self)


class AlarmTable(QTableWidget):
    """ Diagnosis Module 테이블 위젯"""
    qss = """
           QTableWidget#AlarmTable {
               background: rgb(31, 39, 42);
               border-radius: 6px;
               border: none;
           }

           QTableWidget#AlarmTable QHeaderView::section {
               background: rgb(31, 39, 42);
               border-radius: 3px;
               border: 2px inset rgb(62, 74, 84);
               font: bold 12px;
               color: rgb(255, 255, 255);
           }
       """

    def __init__(self, parent):
        super(AlarmTable, self).__init__(parent=parent)
        # self.setAttribute(Qt.WA_StyledBackground, True)  # 상위 스타일 상속
        self.setObjectName('AlarmTable')
        self.setStyleSheet(self.qss)

        # 테이블 프레임 모양 정의
        self.verticalHeader().setVisible(False)  # Row 넘버 숨기기

        # 테이블 셋업
        col_info = [('비정상 절차서', 115), ('진단 확률', 175), ('긴급조치', 55)]  # (name,width)

        self.setColumnCount(len(col_info))
        self.setRowCount(4)

        col_names = []
        for i, (l, w) in enumerate(col_info):
            self.setColumnWidth(i, w)
            col_names.append(l)

        self.setHorizontalHeaderLabels(col_names)
        self.horizontalHeader().setStretchLastSection(True)


class MyApp(QWidget):
    def __init__(self, parent=None):
        super(MyApp, self).__init__()

        self.setWindowTitle('My First Application')
        self.setStyleSheet(qss)

        self.move(300, 300)
        self.resize(400, 200)

        btn1 = MyBtn(self, txt_name='Call1', prop='start')
        # a.clicked.(self.Subwindow)
        btn2 = MyBtn(self, txt_name='Call2')
        pbar1 = ProgressbarBtn(self, 0, 0)
        pbar1.setValue(50)  # progressbar 값 세팅 %
        ###############################################################
        # diagnosis module table 생성
        alarmtable = AlarmTable(self)
        # 비정상 절차서 part
        ex_procedure = '가압기 PORV 개방'
        procedure_label1 = MyLabel(self, txt_name=ex_procedure)
        procedure_label2 = MyLabel(self, txt_name=ex_procedure)
        procedure_label3 = MyLabel(self, txt_name=ex_procedure)
        procedure_label4 = MyLabel(self, txt_name=ex_procedure)

        # w진단 확률 part
        # 진단확률 색 변화는 if문을 통해 prop에 변수 넣어서 qss로!!
        prop_para = 'AlarmItemInfo'
        dignosis_percent = 99
        dig_percent_label1 = MyLabel(self, txt_name=f'{dignosis_percent}%', prop=prop_para)
        dig_percent_label2 = MyLabel(self, txt_name=f'{dignosis_percent}%', prop=prop_para)
        dig_percent_label3 = MyLabel(self, txt_name=f'{dignosis_percent}%', prop=prop_para)
        dig_percent_label4 = MyLabel(self, txt_name=f'{dignosis_percent}%', prop=prop_para)

        # 증상 만족 여부 part
        symptom_percent = 50
        symptom_check1 = MyBtn(self, txt_name=f'{symptom_percent}%')
        symptom_check2 = MyBtn(self, txt_name=f'{symptom_percent}%')
        symptom_check3 = MyBtn(self, txt_name=f'{symptom_percent}%')
        symptom_check4 = MyBtn(self, txt_name=f'{symptom_percent}%')

        # table에 버튼 넣기
        alarmtable.setCellWidget(0, 0, procedure_label1)
        alarmtable.setCellWidget(1, 0, procedure_label2)
        alarmtable.setCellWidget(2, 0, procedure_label3)
        alarmtable.setCellWidget(3, 0, procedure_label4)
        alarmtable.setCellWidget(0, 1, dig_percent_label1)
        alarmtable.setCellWidget(1, 1, dig_percent_label2)
        alarmtable.setCellWidget(2, 1, dig_percent_label3)
        alarmtable.setCellWidget(3, 1, dig_percent_label4)
        alarmtable.setCellWidget(0, 2, symptom_check1)
        alarmtable.setCellWidget(1, 2, symptom_check2)
        alarmtable.setCellWidget(2, 2, symptom_check3)
        alarmtable.setCellWidget(3, 2, symptom_check4)
        # table 안에 글자 가운데 정렬
        # alarmtable.setItem(1, 1, QTableWidgetItem('aa'))
        #
        #
        # alarmtable.item(1, 1).setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)

        layer = QVBoxLayout()
        layer_db = QHBoxLayout()

        layer_db.addWidget(pbar1)
        layer_db.addWidget(btn1)
        layer_db.addWidget(btn2)

        layer.addWidget(alarmtable)
        layer.addLayout(layer_db)

        self.setLayout(layer)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())