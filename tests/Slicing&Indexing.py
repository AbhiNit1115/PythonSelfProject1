class A:
    def __init__(self):
        print("I'm in class A")


class B(A):
    def __init__(self):
        super().__init__()
        print("I'm in class B")


class C(B):
    def __init__(self):
        super().__init__()
        print("I'm in class C")


obj1 = C()
