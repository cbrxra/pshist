from services.PowershellService import PowerShellService
from repositories.ProfileRepository import ProfileRepository
from repositories.ConfigRepository import ConfigRepository
import os

class ProfileService:
    
    @staticmethod
    def create(name_profile: str) -> bool: 

        if ProfileRepository().exists(name_profile):    
            
            return False

        ProfileRepository().create(name_profile)

        return True
        
    @staticmethod
    def list() -> list[str]:
        Folders = ProfileRepository().get_profiles()
        return Folders
             
    @staticmethod
    def use(name_profile :str) -> bool:

        if not ProfileRepository().exists(name_profile):
            return False
        
        history = ProfileRepository().get_history(name_profile)

        PowerShellService().save_history(history)

        ConfigRepository().set_current_profile(name_profile)

        os.system("cls")

        return True

    @staticmethod
    def view(name_profile: str):
        
        if not ProfileRepository().exists(name_profile):
            return False
        
        history = ProfileRepository().get_history(name_profile)

        return history

    @staticmethod
    def delete(name_profile :str):
        if not ProfileRepository().exists(name_profile):
            return False
        
        ProfileRepository().delete(name_profile)

        return True

    @staticmethod
    def add_last(count: int, name_profile: str | None = None):
                
        if name_profile is None:
            name_profile = ConfigRepository().get_current_profile()

        if not ProfileRepository().exists(name_profile):
            return False

        history_profile = ProfileRepository().get_history(name_profile)

        history_powershell = PowerShellService().get_history()

        history_powershell.reverse()

        history_powershell = history_powershell[1: count + 1]
        
        new_history = []

        for command in history_powershell:

            if not(command in history_profile) and command != "" and command != "\n" and not (command in new_history):
                new_history.append(command)

        new_history.reverse()

        ProfileRepository().append_history(name_profile, new_history)

        return new_history
    
    @staticmethod
    def exit(default_profile :str | None = None) -> bool:

        current_profile = ConfigRepository().get_current_profile()
        
        if default_profile is None:
            default_profile = ConfigRepository().get_default_profile()

        if current_profile == default_profile:
            return False

        if not ProfileRepository().exists(default_profile):
            return False

        history = ProfileRepository().get_history(default_profile)

        PowerShellService().save_history(history)
        
        ConfigRepository().set_current_profile(default_profile)

        return True
        

        
        
