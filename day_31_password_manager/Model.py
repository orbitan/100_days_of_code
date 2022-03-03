import json

dummie_data = {
    "website": {
        "email": "email",
        "password": "password",
    }
}

class Model:
    def __init__(self, password):
        self.password = password

    @property
    def account(self):
        return self.__password

    @account.setter
    def account(self, value):
        self.__password = value

    def save(self, new_data):
        try:
            with open('passwords.json', 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            with open('passwords.json', 'w') as f:
                json.dump(dummie_data, f, indent=4)
        else:
            data.update(new_data)
            with open('passwords.json', 'w') as f:
                json.dump(data, f, indent=4)

    def search(self, website):
        with open('passwords.json', 'r') as f:
            data = json.load(f)
            if website in data:
                return data[website]
            else:
                return None

