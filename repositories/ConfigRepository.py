import json

from config.paths import CONFIG_FILE

class ConfigRepository:
    
    @staticmethod
    def get_current_profile() -> str:
        with open(CONFIG_FILE, "r", encoding = "utf-8") as file:
            data = json.load(file)
            
        return data["settings"]["currentProfile"]

    @staticmethod
    def get_default_profile() -> str:
        with open(CONFIG_FILE, "r", encoding = "utf-8") as file:
            data = json.load(file)
            
        return data["settings"]["defaultProfile"]
    
    @staticmethod
    def get_all_config() -> dict:
        with open(CONFIG_FILE, "r", encoding = "utf-8") as file:
            data = json.load(file)

        return data["settings"]
    
    @staticmethod
    def set_current_profile(name_profile: str) -> None:
        with open(CONFIG_FILE, "r", encoding = "utf-8") as file:
            data = json.load(file)
        
        data["settings"]["currentProfile"] = name_profile

        with open(CONFIG_FILE, "w", encoding = "utf-8") as file:
            json.dump(data, file, indent = 4)

    @staticmethod
    def set_default_profile(name_profile: str) -> None:
        with open(CONFIG_FILE, "r", encoding = "utf-8") as file:
            data = json.load(file)
        
        data["settings"]["defaultProfile"] = name_profile

        with open(CONFIG_FILE, "w", encoding = "utf-8") as file:
            json.dump(data, file, indent = 4)

    

        
