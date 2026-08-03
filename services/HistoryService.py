
from repositories.ProfileRepository import ProfileRepository
from repositories.ConfigRepository import ConfigRepository

from services.PowershellService import PowerShellService

from exceptions import ProfileNotFoundError, HistoryAddCountError, HistoryDeleteIndexError, HistoryDeleteIndexLenError, HistoryEmptyError

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

    @staticmethod
    def delete_index( index :int, name_profile :str | None = None):

        if name_profile is None:
            name_profile = ConfigRepository().get_current_profile()

        if not ProfileRepository().exists(name_profile):
            raise ProfileNotFoundError(name_profile)

        if index < 0:
            raise HistoryDeleteIndexError(index)

        data = ProfileRepository().get_history(name_profile)

        len_data = len(data)

        if len_data == 0:
            raise HistoryEmptyError()

        if index > len_data:
            raise HistoryDeleteIndexLenError(index, len_data)

        command_delete = f" - {index} {data[index]}"

        data.pop(index)

        ProfileRepository().overwrite_history(name_profile, data)

        return command_delete

    @staticmethod
    def delete_all(name_profile :str | None = None):

        if name_profile is None:
            name_profile = ConfigRepository().get_current_profile()

        if not ProfileRepository().exists(name_profile):
            raise ProfileNotFoundError(name_profile)

        data = ProfileRepository().get_history(name_profile)

        len_data = len(data)

        if len_data == 0:
            raise HistoryEmptyError()

        ProfileRepository().delete_history(name_profile)

        
        
