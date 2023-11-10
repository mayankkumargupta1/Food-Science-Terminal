


class break_input:
    def __init__(self, inp):
        self.inp = inp

    def get(self):
        x = self.inp
        x = x.split('|')
        x = [i.split(',') if ',' in i else i for i in x]

        return tuple(x)
