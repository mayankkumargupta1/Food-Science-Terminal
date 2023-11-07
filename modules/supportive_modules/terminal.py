import os
class terminal:
    def __init__(self):
        self.__data = ''''''
    
    
    def get_data(self) -> str:
        return self.__data
    
    def set_data(self,text: str) -> None:
        self.__data = text

    def add_data(self,text) -> None:
        self.__data += text

    def clear() -> None:
        os.system('cls')