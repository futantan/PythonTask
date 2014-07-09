class Stack(object):
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if len(self.stack) != 0:
            return self.stack.pop()
        else:
            return None

    def show(self):
        print self.stack