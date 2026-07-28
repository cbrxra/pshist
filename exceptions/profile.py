from exceptions.base import TerminalError

class ProfileError(TerminalError):
    pass

class ProfileNotFoundError(ProfileError):

    def __init__(self, profile_name: str):
        super().__init__(f"Profile '{profile_name}' does not exist.")
        self.profile_name = profile_name

class ProfileAlreadyExistsError(ProfileError):

    def __init__(self, profile_name :str):
        super().__init__(f"Profile '{profile_name}' already exists.")
        self.profile_name = profile_name

class DefaultProfileDeleteError(ProfileError):

    def __init__(self, profile_name :str):
        super().__init__(f"Profile '{profile_name}' is the default profile and cannot be deleted.")
        self.profile_name = profile_name


