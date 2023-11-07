import sys

sys.path.append("modules/supportive_modules")

from modules import out_handler
from modules import input_handler

if __name__ == "__main__":
    out = out_handler.out()
    inp = input_handler.text_input()
    out.Print(text="search something tasty ! !", font="speed", color='red', justtify='right')
    out.Print(
        text='                                                                                                                   ',
        background='white')
    print()
    out.Print(text="  A party without cake is just a meeting.  - Julia Child", color="green")
    print()
    print()
    out.Print(text='search format', color='red')
    out.Print(text='query + apetite + min-max protein + ....your imagination', color='red')
    print()
    print()
    a = inp.next_line()
