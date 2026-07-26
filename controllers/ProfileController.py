from services.ProfileService import ProfileService

from utils.Colors import RESET, GREEN, YELLOW, WHITE, RED

class ProfileController:
    
    @staticmethod
    def create(args):
        
        if ProfileService().create(args.name):
            print(GREEN + f"Perfil '{args.name}' creado." + RESET)

        else:
            print(YELLOW + f"Perfil '{args.name}' ya existe." + RESET)
    
    @staticmethod
    def list(args):

        data = ProfileService().list()
        
        if data != None:
            print(GREEN + "  Perfiles: " + RESET + WHITE + "\n- " + "\n- ".join(data.keys()) + RESET)

        else:
            print(YELLOW + "  Sin perfiles creados. " + RESET)
    
    @staticmethod
    def view(args):
        
        data = ProfileService().view(args.name)

        if data != False:
            print(GREEN +  f"  Comandos del perfil '{args.name}': " + RESET + "\n\n- " + WHITE + "\n- ".join(data) + RESET)

        else:
            print(YELLOW +  f"  El perfil '{args.name}' no existe" +  RESET)

    @staticmethod
    def use(args):

        if ProfileService().use(args.name):
            print(GREEN + f"  Perfil cambiado a '{args.name}'." + RESET)
        else:
            print(YELLOW + f"  El perfil '{args.name}' no existe" + RESET)

    @staticmethod
    def delete(args):

        if ProfileService().delete(args.name):
            print(GREEN + f"  Perfil {args.name} eliminado." + RESET)
            
        else:
            print(YELLOW + f"  Perfil {args.name} no existe." + RESET)

    @staticmethod
    def exit(args):

        if ProfileService().exit() == True:
            print(YELLOW + f"  Saliendo del Perfil" + RESET)

        else:
            print(RED + f"  Error al salir" + RESET)