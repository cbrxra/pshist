from services.HistoryService import HistoryService

from utils.Colors import RED, RESET, YELLOW, GREEN, WHITE

class HistoryController:

    @staticmethod
    def add_last(args):

        data = HistoryService().add_last(args.count)

        if data == False:
            print(RED + "Error al agregar historial nuevo al perfil actual" + RESET)

        elif data == []:
            print(YELLOW + "Sin comandos nuevos a agregar al perfil actual" + RESET)

        elif data:
            print(GREEN + "Comandos Agregados al Perfil Actual: " + RESET + "\n\n- " + WHITE + "\n- ".join(data) + RESET)

    @staticmethod
    def add_all(args):
        data = HistoryService().add_all()

        if data == False:
            print(RED + "Error al agregar historial nuevo al perfil actual" + RESET)

        elif data == []:
            print(YELLOW + "Sin comandos nuevos a agregar al perfil actual" + RESET)

        elif data:
            print(GREEN + "Comandos Agregados al Perfil Actual: " + RESET + "\n\n- " + WHITE + "\n- ".join(data) + RESET)

