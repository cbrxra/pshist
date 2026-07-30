
from repositories.ProfileRepository import ProfileRepository
from repositories.ConfigRepository import ConfigRepository

from exceptions import ProfileNotFoundError

class ConfigService:
    
    @staticmethod
    def set_defaultprofile(name_profile :str) -> None:

        last_profile_default_name = ConfigRepository().get_default_profile()
        
        if not ProfileRepository().exists(name_profile):
            raise ProfileNotFoundError(name_profile)

        if last_profile_default_name == name_profile:
            return

        ConfigRepository().set_default_profile(name_profile)


    @staticmethod
    def get_currentprofile() -> str | None:
        name_profile = ConfigRepository().get_current_profile()

        if not ProfileRepository().exists(name_profile):
            return None

        return name_profile
    
    @staticmethod
    def get_defaultprofile() -> str:
        name_profile = ConfigRepository().get_default_profile()
        
        if not ProfileRepository().exists(name_profile):
            raise ProfileNotFoundError(name_profile)
        
        return name_profile

    @staticmethod
    def get_all_config() -> dict:
        dic_config = ConfigRepository().get_all_config()

        return dic_config
    
