from services.HistoryService import HistoryService

from utils.Colors import RED, RESET, YELLOW, GREEN, WHITE

from exceptions import TerminalError

class HistoryController:

    @staticmethod
    def add_last(args):

        try:
        
            data = HistoryService().add_last(args.count, args.profile)

            if data:
                print(GREEN + "Comandos Agregados al Perfil: " + RESET + "\n\n- " + WHITE + "\n- ".join(data) + RESET)
                
            else:
                print(YELLOW + "Sin comandos nuevos a agregar al perfil actual" + RESET)

        except TerminalError as e:
            print(RED + f"{e}" + RESET)

            

    @staticmethod
    def add_all(args):
        
        try:
            data = HistoryService().add_all(args.profile)

            if data:
                print(GREEN + "Comandos Agregados al Perfil Actual: " + RESET + "\n\n- " + WHITE + "\n- ".join(data) + RESET)
            else:
                print(YELLOW + "Sin comandos nuevos a agregar al perfil actual" + RESET)
            
        except TerminalError as e:
            print(RED +  f"{e}" + RESET)

    @staticmethod
    def delete_index(args):
        try: 
            command_delete = HistoryService().delete_index(args.num_index, args.profile)
            print(YELLOW +  f"Command deleted: {command_delete}" + RESET)
        except TerminalError as e:
           print(RED + f"{e}" + RESET)

    @staticmethod
    def delete_all(args):
        try:
            HistoryService().delete_all(args.profile)
            print(GREEN + "  Perfil Vaciado" + RESET)
        except TerminalError as e:
            print(RED + f"{e}" + RESET)

