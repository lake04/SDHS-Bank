import json

class SaveManager:

    def __init__(self):
        self.filePath = r"C:\Users\wjdgh\SDHS-Bank\Json\account.json"

    def Save(self, data):
        with open(self.filePath, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def Load(self):
        try:
            with open(self.filePath, "r", encoding="utf-8") as file:
                load = json.load(file)
                return load
        except (FileNotFoundError, json.JSONDecodeError):
             return self.Init_data()

    def Init_data(self):
        data = {
            "money": 0,
            "history": []
        }

        self.Save(data)
        return data