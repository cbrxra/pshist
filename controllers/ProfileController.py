from services.ProfileService import ProfileService

from utils.Colors import RESET, GREEN, YELLOW, WHITE, RED

from exceptions import TerminalError

class ProfileController:
    
    @staticmethod
    def create(args):
        try: 
            ProfileService().create(args.name)
            print(GREEN + f"Perfil '{args.name}' creado." + RESET)

        except TerminalError as e :
            print(YELLOW + f"{e}" + RESET)
    
    @staticmethod
    def list(args):

        data = ProfileService().list()
        
        if data != None:
            print(GREEN + "  Perfiles: " + RESET + WHITE + "\n- " + "\n- ".join(data.keys()) + RESET)

        else:
            print(YELLOW + "  Sin perfiles creados. " + RESET)
    
    @staticmethod
    def view(args):

        try:
            data = ProfileService().view(args.name)

            if data:
                print(GREEN +  f"  Comandos del perfil '{args.name}': " + RESET + "\n\n- " + WHITE + "\n- ".join(data) + RESET)

            else:
                print(YELLOW +  f"  El perfil '{args.name}' aun no tiene comandos" +  RESET)

        except TerminalError as e:

            print(RED + f"{e}" + RESET)

    @staticmethod
    def use(args):

        try:        
            ProfileService().use(args.name)
            print(GREEN + f"  Perfil cambiado a '{args.name}'." + RESET)

        except TerminalError as e:
            print(RED + f"{e}" + RESET)

    @staticmethod
    def delete(args):

        try:
            ProfileService().delete(args.name)
            print(GREEN + f"  Perfil {args.name} eliminado." + RESET)
            
        except TerminalError as e:
            print(RED + f"{e}" + RESET)

    @staticmethod
    def exit(args):
        try:
            ProfileService().exit()
            print(YELLOW + f"  Saliendo del Perfil" + RESET)
        except TerminalError as e:
            print(RED + f"{e}" + RESET)

    @staticmethod
    def rename(args):
        try:
            ProfileService().rename(args.name, args.new_name)
            print(GREEN + f"  Perfil '{args.name}' cambiado a '{args.new_name}'" + RESET)
        except TerminalError as e:
            print(RED + f"{e}" + RESET)