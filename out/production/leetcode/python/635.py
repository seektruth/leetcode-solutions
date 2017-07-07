from datetime import datetime
comparelevel = {
    "Year": 1,
    "Month": 2,
    "Day": 3,
    "Hour": 4,
    "Minute": 5,
    "Second": 6
}

startChangeMap ={
    1: 1,
    2: 1,
    3: 0,
    4: 0,
    5: 0
}

endChangeMap = {
    1: 12,
    2: 31,
    3: 23,
    4: 59,
    5: 59
}


class LogSystem(object):
    def __init__(self):
        self.table = []

    def put(self, id, timestamp):
        t = timestamp.split(":")
        t = [int(x) for x in t]
        d = datetime(t[0], t[1], t[2], t[3], t[4], t[5])
        self.table.append((id, d))

    def retrieve(self, s, e, gra):
        """
        :type s: str
        :type e: str
        :type gra: str
        :rtype: List[int]
        """
        level = comparelevel[gra]
        t = s.split(":")
        t = [int(x) for x in t]
        i = level
        while i < len(t):
            t[i] = startChangeMap[i]
            i += 1
        s = datetime(t[0], t[1], t[2], t[3], t[4], t[5])
        t = e.split(":")
        t = [int(x) for x in t]
        i = level
        while i < len(t):
            t[i] = endChangeMap[i]
            i += 1
        else:
            if level == 2:
                if t[1] == 2:
                    t[2] = 28
                elif t[1] in [4, 6, 9, 11]:
                    t[2] = 30
        e = datetime(t[0], t[1], t[2], t[3], t[4], t[5])
        return list(map(lambda x: x[0], filter(lambda x: s <= x[1] <= e, self.table)))

a = LogSystem()
a.put(1, "2017:01:01:23:59:59")
a.put(2, "2017:01:01:22:59:59")
a.put(3, "2016:01:01:00:00:00")
print a.retrieve("2016:01:01:01:01:01", "2017:01:01:23:00:00", "Year")
print a.retrieve("2016:01:01:01:01:01", "2017:01:01:23:00:00", "Hour")