class SuperStr(str):

    def __init__(self, string):
        self.string = string;

    def is_repeatance(self, s):
        self.s = s
        if type(s) != str:
            return False
        if len(self.string) == 0:
            return False
        l = []
        for i in self.string:
            if i not in l:
                l.append(i)
        l = ''.join(l)
        d = len(l)
        if l == self.s[-d]:
            return True
        else:
            return False

    def is_palindrom(self):
        self.string = self.string.lower().replace(' ', '')
        bar = ''
        num = 0
        while num < len(self.string):
            bar += self.string[-num - 1]
            num += 1
        if bar == self.string:
            return True
        else:
            return False