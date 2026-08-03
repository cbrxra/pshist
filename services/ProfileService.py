from services.PowershellService import PowerShellService
from repositories.ProfileRepository import ProfileRepository
from repositories.ConfigRepository import ConfigRepository

import os

from exceptions import ProfileAlreadyExistsError, ProfileNotFoundError, DefaultProfileDeleteError
from utils.strings import normalize_str

class ProfileService:
    
    @staticmethod
    def create(name_profile: str) -> None: 
        
        name_profile = normalize_str(name_profile)

        if ProfileRepository().exists(name_profile):    
            raise ProfileAlreadyExistsError(name_profile)

        ProfileRepository().create(name_profile)   
        
    @staticmethod
    def list() -> list[str]:
        Folders = ProfileRepository().get_profiles()
        return Folders
             
    @staticmethod
    def use(name_profile :str) -> None:

        if not ProfileRepository().exists(name_profile):
            raise ProfileNotFoundError(name_profile)
        
        history = ProfileRepository().get_history(name_profile)

        PowerShellService().save_history(history)
        ConfigRepository().set_current_profile(name_profile)

        os.system("cls")

    @staticmethod
    def view(name_profile: str)  -> list[str]:
        
        if not ProfileRepository().exists(name_profile):
            raise ProfileNotFoundError(name_profile)
        
        history = ProfileRepository().get_history(name_profile)

        return history

    @staticmethod
    def delete(name_profile :str):
        if not ProfileRepository().exists(name_profile):
            raise ProfileNotFoundError(name_profile)

        profile_default = ConfigRepository().get_default_profile()

        if profile_default.lower().strip() == name_profile.lower().strip():
            raise DefaultProfileDeleteError(name_profile)

        ProfileRepository().delete(name_profile)
    
    @staticmethod
    def exit(default_profile :str | None = None) -> None:

        current_profile = ConfigRepository().get_current_profile()
        
        if default_profile is None:
            default_profile = ConfigRepository().get_default_profile()

        if not ProfileRepository().exists(default_profile):
            raise ProfileNotFoundError(default_profile)

        if current_profile.strip().lower() == default_profile.strip().lower():
            return

        history = ProfileRepository().get_history(default_profile)

        PowerShellService().save_history(history)
        
        ConfigRepository().set_current_profile(default_profile)

    @staticmethod
    def rename(name_profile :str, new_name_profile :str) -> None:

        current_profile = ConfigRepository().get_current_profile()
        default_profile = ConfigRepository().get_default_profile()

        if name_profile == default_profile:
            raise DefaultProfileDeleteError(name_profile)
        
        if not ProfileRepository().exists(name_profile):
            raise ProfileNotFoundError(name_profile)

        if ProfileRepository.exists(new_name_profile):
            raise ProfileAlreadyExistsError(new_name_profile)
        
        ProfileRepository().rename(name_profile, new_name_profile)

        if name_profile == current_profile:
            ConfigRepository().set_current_profile(new_name_profile)

    