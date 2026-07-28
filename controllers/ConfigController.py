from services.ConfigService import ConfigService

from utils.Colors import GREEN, YELLOW, RESET, RED, WHITE

from exceptions import TerminalError

class ConfigController:

    @staticmethod
    def set_default_profile(args):

        name_profile = args.profile

        try:
            ConfigService().set_defaultprofile(name_profile)
            print(GREEN + f"El perfil por defecto cambio a {name_profile}" +  RESET)

        except TerminalError as e:
            print(RED +  f"{e}" + RESET)

    @staticmethod
    def view_all(args):
        setting_data = ConfigService().get_all_config()

        print(GREEN + "  Configuración: " + RESET + "\n")
        for name, config  in setting_data.items():
            print(YELLOW + f" - {name}" + ": " + RESET + WHITE + config + RESET)

    @staticmethod
    def view_defaultprofile(args):

        try:
            name_profile = ConfigService().get_defaultprofile()

            print(GREEN + f" El perfil por defecto es: '{name_profile}'" + RESET)

        except TerminalError as e:

            print(RED + f"{e}" + RESET)