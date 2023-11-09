class break_input:
    def __init__(self, inp):
        self.inp = inp

    def get(self):
        x = self.inp
        x = x.split('|')

        return tuple(x)

