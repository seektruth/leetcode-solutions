class MinStack(object):
    def __init__(self):
        self.data = []
        self.mins = []

    def push(self, x):
        self.data.append(x)
        if not self.mins:
            self.mins.append(x)
        else:
            self.mins.append(min(x, self.mins[-1]))

    def pop(self):
        self.data.pop()
        self.mins.pop()

    def top(self):
        if len(self.data) > 0:
            return self.data[0]
        return None

    def getMin(self):
        return self.mins[len(self.data)-1]

