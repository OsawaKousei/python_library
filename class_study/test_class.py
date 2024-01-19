class Test_class:  # クラス作成(クラス名は大文字で始める)
    # コンストラクタ(selfは必須, 他の引数は任意)
    def __init__(self, v1, v2):
        self.name = "test_class"  # インスタンス変数
        self.v1 = v1  # 引数をインスタンス変数に代入
        self.v2 = v2

    # メソッド
    def print_name(self):
        print(self.name)

    def get_value(self):
        return self.v1, self.v2  # 複数の値を返す

    @staticmethod  # 静的メソッド(インスタンス化しなくても呼び出せる)
    def add(fraction):
        return fraction[0] + fraction[1]  # このようにして複数の値を参照できる


def test_class_test():
    test = Test_class(1, 2)
    test.print_name()
    print(test.get_value())
    print(Test_class.add(test.get_value()))
    print(hasattr(test, "name"))  # インスタンス変数の有無を確認
    print(hasattr(test, "v3"))
    raise Exception("test")  # 例外を発生させる


test_class_test()
