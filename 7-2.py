class Student():

    name = None
    config = None
    marks = None

    def __init__(self, name, config):
        self.name = name
        self.config = config
        self.marks = {}
        for i in range(1, self.config['lab_num'] + 1):
            self.marks[i] = 0

    def make_lab(self, m, n = 1):
            if float(m) > float(self.config['lab_max']):
                self.marks[n] = self.config['lab_max']
            else:
                self.marks[n] = m;
            return self

    def make_exam(self, m):
        if m > self.config['exam_max']:
            self.marks['exam'] = self.config['exam_max']
            return(self.config['exam_max'])
        else:
            self.marks['exam'] = m
        return self

    def is_certified(self):
        if sum(self.marks.values()) >= self.config['k']*100:
            return (sum(self.marks.values()), True)
        else:
            return (sum(self.marks.values()), False)