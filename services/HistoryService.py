
from repositories.ProfileRepository import ProfileRepository
from repositories.ConfigRepository import ConfigRepository

from services.PowershellService import PowerShellService

from exceptions import ProfileNotFoundError, HistoryAddCountError

class HistoryService:
    
    @staticmethod
    def add_last(count :int, name_profile :str | None = None) -> list[str]:
        
        if name_profile is None:
            name_profile = ConfigRepository().get_current_profile()

        if not ProfileRepository().exists(name_profile):
            raise ProfileNotFoundError(name_profile)
        
        if count <= 0:
            raise HistoryAddCountError(count)
        
        history_profile = ProfileRepository().get_history(name_profile)
        history_powershell = PowerShellService().get_history()
        history_powershell.reverse()
        history_powershell = history_powershell[1:count + 1]

        save_history = []

        for command in history_powershell:
            if not(command in save_history) and not(command in history_profile) and command != "" and command != "\n":
                save_history.append(command)

        save_history.reverse()

        if save_history != []:
            ProfileRepository().append_history(name_profile, save_history)
        
        return save_history
    
    @staticmethod
    def add_all(name_profile :str | None = None) -> list[str]:

        if name_profile is None:
            name_profile = ConfigRepository().get_current_profile()

        if not ProfileRepository().exists(name_profile):
            raise ProfileNotFoundError(name_profile)

        history_profile = ProfileRepository().get_history(name_profile)
        history_powershell = PowerShellService().get_history()
        history_powershell.reverse()

        save_history = []

        for command in history_powershell:
            if not(command in save_history) and not(command in history_profile) and command != "" and command != "\n":
                save_history.append(command)

        save_history.reverse()

        if save_history != []:
            ProfileRepository().append_history(name_profile, save_history)

        return save_history


            

        
