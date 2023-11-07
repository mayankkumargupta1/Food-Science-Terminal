from colorama import Fore, Back, Style, init

class Text:
    def __init__(self,color: str = '',background: str = '',style:str = '') -> None:
        self.color = color 
        self.background = background
        self.style = style 
        
    def add_color(self) -> None:
        colors = {
            '' : '',
            'red': Fore.RED,
            'green': Fore.GREEN,
            'blue': Fore.BLUE,
            'yellow': Fore.YELLOW
        }
        return colors[self.color] 

    def add_background(self) -> None:
        colors = {
            '' : '',
            'white': Back.WHITE,
            'red': Back.RED,
            'green': Back.GREEN,
            'blue': Back.BLUE,
            'yellow': Back.YELLOW
        }
        return colors[self.background]
    
    def add_style(self) -> None:
        styles = {
            '' : '',
            'bright': Style.BRIGHT,
            'dim': Style.DIM,
            'normal': Style.NORMAL
        }
        return styles[self.style]
    
    def out(self,text: str) -> None:
        init(autoreset=True)
        result = self.add_style() + self.add_background() + self.add_color() + text
        return result
