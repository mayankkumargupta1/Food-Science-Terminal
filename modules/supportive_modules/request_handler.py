import requests
import json


class j_handler:
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    def read_json(self) -> dict:
        with open(self.file_path, 'r') as file:
            data = json.load(file)
        return data

    def create_json(self, data) -> None:
        with open(self.file_path, 'w') as file:
            json.dump(data, file)


class urls:
    def __init__(self) -> None:
        self.root = r'https://api.spoonacular.com/recipes/'
        self.api_key = r'd4eaca8356904aafa8957ae5c3eb00ec'

    @staticmethod
    def proteins(min: int, max: int) -> str:
        return '&minProtein={}&maxProtein={}'.format(min, max)

    @staticmethod
    def caloriess(min, max) -> str:
        return '&minCalories={}&maxCalories={}'.format(min, max)

    @staticmethod
    def fats(min, max) -> str:
        return '&minFat={}&maxFat={}'.format(min, max)

    def build(self, query, p: tuple, calories: tuple, fat: tuple, sort: str) -> str:
        url = ''
        url += self.root
        url += 'complexSearch/?apiKey=' + self.api_key
        url += '&query=' + query
        url += urls.proteins(min=p[0], max=p[1])
        url += urls.caloriess(min=calories[0], max=calories[1])
        url += urls.fats(min=fat[0], max=fat[1])
        url += '&sort=' + sort
        a = requests.get(url, timeout=30)
        b = a.content
        c = b.decode()
        js = j_handler(file_path='./memory/build.json')
        js.create_json(data=c)
        return c

    def search(self, id: int) -> None:
        hex = ''
        hex += self.root
        hex += str(id)
        hex += '/information/?apiKey={}'.format(self.api_key)
        a = requests.get(hex, timeout=30)
        b = a.content
        c = b.decode()
        js = j_handler(file_path='./memory/search.json')
        js.create_json(data=c)
