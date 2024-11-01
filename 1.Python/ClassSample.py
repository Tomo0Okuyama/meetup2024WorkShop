class Animal:
    spec = 'Mammal'             #クラス変数

    def __init__(self, name):   #コンストラクタ
        self.name = name        #インスタンス変数

    def getName(self):          #アクセサ
        return self.name

class Cat(Animal):              # 継承
    spec = 'Cat'

import dataclasses
@dataclasses.dataclass
class DataclassPerson:
    number: int
    name: str
