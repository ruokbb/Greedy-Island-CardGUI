from  single_instance import conn
import json
from PyQt5.Qt import *

# redis中卡片相关字段如下
# hashmap
# card:info  id  jsoninfo
# card:name  id   name
# card:level id   level
# card:kind  id   kind
# card:describe  id  describe

def load_card(id,name:QLineEdit,level:QComboBox,kind:QComboBox,describe:QTextEdit):
    data = conn.hget('card:info',id)
    data = json.loads(data)

