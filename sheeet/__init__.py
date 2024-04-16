import requests


class Sheeet:
    def __init__(self, url):
        self.sheet_url = url

    def all(self):
        response = requests.get(self.sheet_url)
        return response.json()

    def insert(self, data):
        response = requests.post(self.sheet_url, json=data)
        return response.json()

    def clear(self):
        response = requests.delete(self.sheet_url)
        return response.json()

    def delete(self, id):
        response = requests.delete(self.sheet_url + "/" + str(id))
        return response.json()
