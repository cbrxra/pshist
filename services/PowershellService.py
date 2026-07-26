import subprocess

from pathlib import Path

class PowerShellService:
    
    @staticmethod
    def get_history_path() -> Path:

        result = subprocess.run(["pwsh",
        "-NoProfile",
        "-Command",
        "(Get-PSReadLineOption).HistorySavePath"], encoding = 'utf-8', capture_output = True, text = True, check = True)

        history_path = Path(result.stdout.strip())

        return history_path

    @staticmethod
    def get_profile_path() -> Path:
        result = subprocess.run(["pwsh", "-NoProfile","-Command", "$PROFILE",],  encoding = "utf-8", capture_output = True, text = True, check = True)
        path_profile = Path(result.stdout.strip())

        return path_profile

    @staticmethod
    def ensure_history_path() -> Path:
        history_path = PowerShellService().get_history_path()
        history_path.parent.mkdir(parents = True, exist_ok = True)
        history_path.touch(exist_ok = True)

        return history_path

    @staticmethod
    def ensure_profile_path() -> Path:
        path_profile = PowerShellService().get_profile_path()
        path_profile.parent.mkdir(parents = True, exist_ok = True)
        path_profile.touch(exist_ok = True)

        return path_profile   
    
    @staticmethod
    def get_history() -> list[str]:
        history_path = PowerShellService().get_history_path()

        if not history_path.exists():
            return []
        
        return history_path.read_text(encoding = "utf-8").splitlines()
    
    @staticmethod
    def save_history(data : list[str]):
        path = PowerShellService().get_history_path()

        with open(path, "w", encoding = "utf-8") as file:
            file.write("\n".join(data) + "\n")