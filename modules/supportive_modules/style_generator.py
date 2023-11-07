from pyfiglet import Figlet
from colorama import Fore, Back, Style, init
from . import text_generator

class styles(text_generator.Text):
    def __init__(self,font='',color = '',background = '',styles = '',justify = 'left'):
        self.font = font
        self.color = color
        self.background = background
        self.styles = styles
        self.justify = justify
        super().__init__(color=self.color,background=self.background,style=self.styles)

    def styler(self,text):
        init(autoreset=True)
        f = Figlet(self.font,justify=self.justify)
        result = f.renderText(text)

        return self.add_background() + self.add_color() + self.add_style() + result
    

