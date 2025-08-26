class Demo:
    def test(self):
        print("test calling")


class Sample:
    d = Demo()
    def run(self):
        print("Run calling")


s = Sample()
s.d.test()
