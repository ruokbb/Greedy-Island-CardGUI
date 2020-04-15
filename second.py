from PyQt5.Qt import *
import sys
from card_list import Ui_Form
from single_instance import conn,MAX_CARD_ID
from card_list_item import Ui_Form as Item
import json


class ItemWidget(QWidget,Item):

    signal_delete = pyqtSignal(int)
    signal_load = pyqtSignal(int)

    def __init__(self,id,data,parent=None):
        super(ItemWidget, self).__init__(parent=parent)
        self.setupUi(self)
        self.get_ui()
        self.load_data(id,data)

    def get_ui(self):
        self.id: QLabel = self.findChild(QLabel,'id')
        self.name: QLabel = self.findChild(QLabel, 'name')
        self.level: QLabel = self.findChild(QLabel, 'level')
        self.describe: QLabel = self.findChild(QLabel, 'describe')
        self.kind: QLabel = self.findChild(QLabel, 'kind')
        self.load: QPushButton = self.findChild(QPushButton, 'load')

    def load_data(self,id,data):
        self.id.setText(str(int(id)))
        self.name.setText(data['name'])
        self.level.setText(data['level'])
        self.describe.setText(data['describe'])
        self.kind.setText(data['kind'])

    def load_card(self):
        self.signal_load.emit(int(self.id.text()))

    def delete_card(self):
        self.signal_delete.emit(int(self.id.text()))


class SecondWidget(QWidget, Ui_Form):

    signal_load = pyqtSignal(int,object)

    def __init__(self,parent=None):
        super(SecondWidget, self).__init__(parent=parent)
        self.setupUi(self)
        self.get_ui()
        self.perfect_ui()

    def get_ui(self):
        self.list_view: QListWidget = self.findChild(QListWidget, 'listWidget')
        self.reverse: QCheckBox = self.findChild(QCheckBox,'reverse')
        self.low_id: QSpinBox = self.findChild(QSpinBox,'low_id')
        self.high_id: QSpinBox = self.findChild(QSpinBox, 'high_id')
        self.no_btn: QRadioButton = self.findChild(QRadioButton,'no_btn')
        self.a_btn: QRadioButton = self.findChild(QRadioButton, 'a_btn')
        self.b_btn: QRadioButton = self.findChild(QRadioButton, 'b_btn')
        self.c_btn: QRadioButton = self.findChild(QRadioButton, 'c_btn')
        self.d_btn: QRadioButton = self.findChild(QRadioButton, 'd_btn')

    def perfect_ui(self):
        self.low_id.setMaximum(MAX_CARD_ID)
        self.high_id.setMaximum(MAX_CARD_ID)
        self.high_id.setValue(MAX_CARD_ID)

    def reload(self):
        self.list_view.clear()
        temp = conn.hgetall('card:info')
        #排序
        result={}
        for key,value in temp.items():
            result[key] = json.loads(value)
        if self.reverse.isChecked():
            result = sorted(result.items(),key=lambda x:int(x[0]),reverse=True)
        else:
            result = sorted(result.items(), key=lambda x: int(x[0]))

        #区间
        low = self.low_id.value()
        high = self.high_id.value()
        if low<0 or high>MAX_CARD_ID or low>high:
            low=0
            high = MAX_CARD_ID
            self.low_id.setValue(low)
            self.high_id.setValue(high)

        #等级筛选
        level = 'NO'
        if self.a_btn.isChecked():
            level='A'
        elif self.b_btn.isChecked():
            level='B'
        elif self.c_btn.isChecked():
            level='C'
        elif self.d_btn.isChecked():
            level='D'

        for key,value in result:
            if int(key)<low or int(key)>high:
                continue
            if level!='NO' and value['level']!=level:
                continue
            item = QListWidgetItem()
            item.setSizeHint(QSize(690,100))
            widget = ItemWidget(key,value)
            self.list_view.addItem(item)
            self.list_view.setItemWidget(item,widget)
            widget.signal_delete.connect(self.delete_card)
            widget.signal_load.connect(self.load_card)

    def load_card(self,card_id:int):
        self.signal_load.emit(card_id,self)

    def delete_card(self,card_id):

        conn.hdel('card:describe',card_id)
        conn.hdel('card:info',card_id)
        conn.hdel('card:kind',card_id)
        conn.hdel('card:level',card_id)
        conn.hdel('card:name',card_id)

        self.reload()



if __name__ == '__main__':
    app = QApplication(sys.argv)

    my_widget = SecondWidget()
    my_widget.show()

    sys.exit(app.exec_())



