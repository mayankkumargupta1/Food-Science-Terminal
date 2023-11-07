from modules import supportive_modules


class text_input:
    def __init__(self) -> None:
        pass
    def next_line(self):
        text = supportive_modules.text_generator.Text(color='blue').out('--> ')
        a = input(text)
        
        return a
