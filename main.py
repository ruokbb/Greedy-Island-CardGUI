from PyQt5.Qt import *
import sys
from main_window import Ui_MainWindow
from single_instance import conn ,MAX_CARD_ID
import json
from second import SecondWidget


class MyWidget(QMainWindow, Ui_MainWindow):
    singal_show_cards = pyqtSignal()

    def __init__(self, parent=None):
        super(MyWidget, self).__init__(parent=parent)
        self.setupUi(self)
        self.get_ui()
        self.perfectUi()

    def get_ui(self):
        self.id: QLineEdit = self.findChild(QLineEdit, 'number')
        self.name: QLineEdit = self.findChild(QLineEdit, 'name')
        self.level: QComboBox = self.findChild(QComboBox, 'level')
        self.kind: QComboBox = self.findChild(QComboBox, 'kind')
        self.describe: QTextEdit = self.findChild(QTextEdit, 'describe')
        self.bar: QStatusBar = self.findChild(QStatusBar, 'statusbar')

    def perfectUi(self):
        self.id.setValidator(QIntValidator(0, 100))

        levels = ['无','A', 'B', 'C', 'D']
        self.level.addItems(levels)
        self.kind.addItems(['无','战斗', '探索', '气运'])
        self.bar.setStyleSheet("QStatusBar{color:red}")

    # redis中卡片相关字段如下
    # hashmap
    # card:info  id  jsoninfo
    # card:name  id   name
    # card:level id   level
    # card:kind  id   kind
    # card:describe  id  describe

    def load_card(self):
        if self.id.text()=='':
            self.bar.showMessage('请输入正确ID', 3500)
            return
        data = conn.hget('card:info', self.id.text())
        if not data:
            self.bar.showMessage('无当前ID卡片', 3500)
            return
        data = json.loads(data)
        self.name.setText(data['name'])
        self.describe.setText(data['describe'])
        self.level.setCurrentText(data['level'])
        self.kind.setCurrentText(data['kind'])

    def clear(self):
        self.name.clear()
        self.describe.clear()
        self.level.setCurrentIndex(0)
        self.kind.setCurrentIndex(0)
        self.id.clear()

    def submit(self):
        id = self.id.text()
        name = self.name.text()
        describe = self.describe.toPlainText()
        level = self.level.currentText()
        kind = self.kind.currentText()
        if id=='' or name == '' or describe == '' or level=='无' or kind == '无':
            self.bar.showMessage('数据缺失',3500)
            return

        data = {'name': name, 'describe': describe,
                "level": level, 'kind': kind}
        conn.hset('card:info', id, json.dumps(data))
        conn.hset('card:name', id, name)
        conn.hset('card:level', id, level)
        conn.hset('card:kind', id, kind)
        conn.hset('card:describe', id, describe)

        self.bar.setStyleSheet('QComboBox{color:rgb(30,144,255)}')
        self.bar.showMessage('更新成功',3500)

    def show_cards(self):
        self.singal_show_cards.emit()

    def load_assign_card(self,card_id,second:SecondWidget):
        self.id.setText(str(card_id))
        self.load_card()
        second.hide()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    my_widget = MyWidget()
    my_widget.show()
    second = SecondWidget()

    # 连接槽函数
    my_widget.singal_show_cards.connect(second.show)
    my_widget.singal_show_cards.connect(second.reload)
    second.signal_load.connect(my_widget.load_assign_card)

    sys.exit(app.exec_())
