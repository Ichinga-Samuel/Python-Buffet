

class SClass:

    def woo(self):
        print('woo')


class SC:

    def woo(self):
        print('WOO')


class Sub(SClass, SC):

    def boo(self):
        print('boo')
        super().woo()

    def scboo(self):
        SC.woo(self)


s = Sub()
SC.woo(s)