

class Order(object):
    filename = ''
    orders = []

    def __init__(self, filename):
        self.filename = filename
        f = open(filename, "r")
        for l in f:
            self.orders.append(l.rstrip().split(' '))
        self.orders.reverse()

    def nextOrder(self):
        if self.orders.__len__() > 0:
            return self.orders.pop()
        else:
            return -1