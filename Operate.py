# -*- coding: utf-8 -*-


class Operate(object):
    ADD    = 0x01
    DELETE = 0x02
    EDIT   = 0x04

    def __init__(self, operate, *args):
        self.op = operate
        if self.op in {Operate.ADD, Operate.DELETE}:
            self.item = args[0]
        elif self.op == Operate.EDIT:
            self.id = args[0]
            self.title = args[1]
            self.value = args[2]


class Stack(object):
    """ 假装自己是个stack，其实只是一个list\n
    包装一下list的方法作为stack的方法，只能实现几个简单的操作
    """
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.empty() is False:
            return self.stack.pop()
        else:
            return None

    def get_top(self):
        if self.empty() is False:
            return self.stack[-1]
        else:
            return None

    def empty(self) -> bool:
        return self.length() == 0

    def length(self) -> int:
        return len(self.stack)
