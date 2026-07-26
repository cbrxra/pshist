from services.ConfigService import ConfigService

from utils.Colors import GREEN, YELLOW, RESET, RED, WHITE

class ConfigController:

    @staticmethod
    def set_default_profile(args):
        name_profile = args.profile
        if ConfigService().set_defaultprofile(name_profile) == True:
            print(GREEN + f"El perfil por defecto cambio a {name_profile}" +  RESET)

        else:
            print(YELLOW +  f"Error al cambiar el perfil por defecto" + RESET)

    @staticmethod
    def view_all(args):
        setting_data = ConfigService().get_all_config()

        print(GREEN + "  Configuración: " + RESET + "\n")
        for name, config  in setting_data.items():
            print(YELLOW + f" - {name}" + ": " + RESET + WHITE + config + RESET)

    @staticmethod
    def view_defaultprofile(args):
        name_profile = ConfigService().get_defaultprofile()

        if name_profile is None:
            print(RED + f"  El perfil por defecto no existe" + RESET)

        else:
            print(YELLOW + f" El perfil por defecto es: '{name_profile}'" + RESET)