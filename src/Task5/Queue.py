class Queue(object):
    def __init__(self):
        self.queue = []

    def push(self, data):
        self.queue.append(data)

    def pop(self):
        if len(self.queue) != 0:
            return self.queue.pop(0)
        else:
            return None

    def show(self):
        print self.queue