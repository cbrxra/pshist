from config.paths import PROFILES_DIR, Path

import shutil

class ProfileRepository:

    @staticmethod
    def exists(profile_name :str) -> bool:
        return (PROFILES_DIR / profile_name).exists()

    @staticmethod
    def create(profile_name :str):
        path = PROFILES_DIR / profile_name
        path.mkdir(parents = True, exist_ok = True)

        history = path / "History.txt"
        history.touch(exist_ok = True)

    @staticmethod  
    def get_profiles():
        profiles_dic = {
            folder.name: folder
            for folder in PROFILES_DIR.iterdir()
            if folder.is_dir()
        }

        if profiles_dic:
            return profiles_dic
        
        else:
            return None

    @staticmethod
    def delete(name_profile: str):
        path = PROFILES_DIR / name_profile
        if path.exists():
            shutil.rmtree(path)

    @staticmethod
    def get_history(profile_name :str) -> list[str]:

        path_profile_history = PROFILES_DIR / profile_name / "History.txt"

        return path_profile_history.read_text(encoding = "utf-8").splitlines()
    
    @staticmethod
    def get_history_path(profile_name :str) -> Path:
        return PROFILES_DIR / profile_name / "History.txt"
    
    @staticmethod
    def append_history(name_profile: str, commands: list[str]):
        path = PROFILES_DIR / name_profile / "History.txt"

        with open(path, "a", encoding = "utf-8") as file:
            file.write("\n".join(commands) + "\n")

    @staticmethod
    def rename(name_profile :str, new_name_profile :str):
        path = PROFILES_DIR / name_profile
        path.rename(PROFILES_DIR / new_name_profile)