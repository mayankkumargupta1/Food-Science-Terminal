from .supportive_modules import style_generator, text_generator, request_handler
import json


class out:
    def __init__(self):
        pass

    def Print(self, text, color='', background='', style='', justtify='left', font=''):
        render = ''
        match font:
            case '':
                a = text_generator.Text(color=color, background=background, style=style)
                render = a.out(text)
            case _:
                a = style_generator.styles(font=font, color=color, background=background, styles=style,
                                           justify=justtify)
                render = a.styler(text)

        print(render)



