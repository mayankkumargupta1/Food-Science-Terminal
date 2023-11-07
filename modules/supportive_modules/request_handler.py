import requests
import json


class j_handler:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_json(self):
        with open(self.file_path, 'r') as file:
            data = json.load(file)
        return data

    def create_json(self, data):
        with open(self.file_path, 'w') as file:
            json.dump(data, file)


class urls:
    def __init__(self, root, api_key):
        self.root = root
        self.api_key = api_key

    @staticmethod
    def proteins(min, max) -> str:
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
        return c

    def search(self, id) -> str:
        hex = ''
        hex += self.root
        hex += str(id)
        hex += '/information/?apiKey={}'.format(self.api_key)
        a = requests.get(hex, timeout=30)
        b = a.content
        c = b.decode()
        return c


if __name__ == "__main__":
    a = urls('https://api.spoonacular.com/recipes/', 'd4eaca8356904aafa8957ae5c3eb00ec')
    url = a.build('pasta', (50, 100), (500, 1000), (0, 1000), '')
    js = json.loads(url)

    handler = j_handler('memory/build.json')
    handler.create_json(js)
    print(handler.read_json())
