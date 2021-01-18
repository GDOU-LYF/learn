class Myclass(object):
    def __init__(self):
        self._p = None

    @property
    def p(self):
        print("get p:{}".format(self._p))
        return self._p

    @p.setter
    def p(self, value):
        print("set p:{}->{}".format(self._p, value))
        self._p = value

    @p.deleter
    def p(self):
        print("del p:{}".format(self._p))
        del self._p


if __name__ == "__main__":
    cls = Myclass()
    cls.p = 10
    print('current p:{}'.format(cls.p))
    del cls.p
