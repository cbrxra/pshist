
from repositories.ProfileRepository import ProfileRepository
from repositories.ConfigRepository import ConfigRepository

class ConfigService:
    
    @staticmethod
    def set_curretprofile(name_profile :str) -> bool:

        if not ProfileRepository().exists(name_profile):
            return False
        
        ConfigRepository().set_current_profile(name_profile)

        return True
    
    @staticmethod
    def set_defaultprofile(name_profile :str) -> bool:
        
        if not ProfileRepository().exists(name_profile):
            return False
        
        ConfigRepository().set_default_profile(name_profile)

        return True

    @staticmethod
    def get_currentprofile() -> str | None:
        name_profile = ConfigRepository().get_current_profile()

        if not ProfileRepository().exists(name_profile):
            return None

        return name_profile
    
    @staticmethod
    def get_defaultprofile() -> str | None:
        name_profile = ConfigRepository().get_default_profile()
        
        if not ProfileRepository().exists(name_profile):
            return None
        
        return name_profile

    @staticmethod
    def get_all_config() -> dict:
        dic_config = ConfigRepository().get_all_config()

        return dic_config
    
