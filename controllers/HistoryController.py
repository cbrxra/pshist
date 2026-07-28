from services.HistoryService import HistoryService

from utils.Colors import RED, RESET, YELLOW, GREEN, WHITE

from exceptions import TerminalError

class HistoryController:

    @staticmethod
    def add_last(args):

        try:
        
            data = HistoryService().add_last(args.count)

            if data:
                print(GREEN + "Comandos Agregados al Perfil Actual: " + RESET + "\n\n- " + WHITE + "\n- ".join(data) + RESET)
                
            else:
                print(YELLOW + "Sin comandos nuevos a agregar al perfil actual" + RESET)

        except TerminalError as e:
            print(RED + f"{e}" + RESET)

            

    @staticmethod
    def add_all(args):
        
        try:
            data = HistoryService().add_all()

            if data:
                print(GREEN + "Comandos Agregados al Perfil Actual: " + RESET + "\n\n- " + WHITE + "\n- ".join(data) + RESET)
            else:
                print(YELLOW + "Sin comandos nuevos a agregar al perfil actual" + RESET)
            
        except TerminalError as e:
            print(RED +  f"{e}" + RESET)

            

