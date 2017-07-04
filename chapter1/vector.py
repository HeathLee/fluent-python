from math import hypot


class Vector:
    """
    >>> v1 = Vector(2, 4)
    >>> v2 = Vector(2, 1)
    >>> v1 + v2
    Vector(4, 5)
    >>> v = Vector(3, 4)
    >>> abs(v)
    5.0
    >>> v * 3
    Vector(9, 12)
    >>> abs(v * 3)
    15.0
    """

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        """
        %r 来获取对象各个属性的标准字符串表示形式——它暗示了一个关键：
        Vector(1, 2) 和Vector('1', '2') 是不一样的

        __repr__ 所返回的字符串应该准确、无歧义，并且尽可能表达出如何
        用代码创建出这个被 打印的对象。

        __repr__ 和__str__ 的区别在于，后者是在str() 函数被使用，
        或是在用 print 函数打印 一个对象的时候才被调用的，并且它返回
        的字符串对终端用户更友好。

        如果你只想实现这两个特殊方法中的一个，__repr__ 是更好的选择，
        因为如果一个对象没 有__str__ 函数，而Python 又需要调用它的时候，
        解释器会用__repr__ 作为替代。
        """
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))
        # more efficient
        # return  bool(self.x or self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
