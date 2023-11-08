class break_input:
    def __int__(self, input):
        self.input = input

    def get(self):
        x = self.input
        x = x.split('>')
        query = ''
        protein = ''
        fats = ''
        carbohydrates = ''
        calories = ''
        sort = ''

        for i in range(x):
            if x[i] == 's':
                query = x[i+1]
            elif x[i] == 'p':
                protein = x[i+1]
            elif x[i] == 'f':
                fats = x[i+1]
            elif x[i] == 'c':
                calories = x[i+1]
            elif x[i] == 'a':
                carbohydrates = x[i+1]
            e