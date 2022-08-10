class Father:

    def __init__(self, v):
        self.value = v

    def works_for(self, c):
        company = c
        print("Father's value is:", self.value)
        print("father's company is:", company)


class Son(Father):

    def __init__(self, nv):
        super().__init__(2000)
        self.new_value = nv

    def is_working(self, c):
        company = c
        print("Son is working for:", company)
        print("Son new value is:", self.new_value)


calling_son = Son(1000)
calling_son.is_working("Nokia")
calling_son.works_for("PWD")
