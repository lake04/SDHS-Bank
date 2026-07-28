import json
from pathlib import Path

class SaveManager:

    def __init__(self):
         basePath = Path(__file__).parent
         self.filePath = basePath / "Json" / "account.json"

    def Save(self, data):

        self.filePath.parent.mkdir(parents=True, exist_ok=True)

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