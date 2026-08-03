from controllers.HistoryController import HistoryController
from argparse import _SubParsersAction

def init_history_command(subparsers :_SubParsersAction):
    history_parser = subparsers.add_parser(
        "history", help = "Administrar historial"
    )

    history_subparser = history_parser.add_subparsers(
        dest = "history_command",
        required = True
    )

    history_parser.add_argument(
        "-p", "--profile", help = "Nombre del perfil. Si se omite, se usa el perfil actual."
    )

    #ADD PARSER
    add_parser = history_subparser.add_parser(
        "add",
        help = "agregar comandos al historial del perfil actual"
    )


    add_subparser = add_parser.add_subparsers(
        dest = "add_command",
        required = True
    )

    #ADD ALL PARSER
    all_parser = add_subparser.add_parser(
        "all", help = "Agregar todos los comandos pendientes"
    )

    all_parser.set_defaults(handler = HistoryController.add_all)

    #ADD LAST
    last_parser = add_subparser.add_parser(
        "last", help = "Agregar los últimos comandos"
    )

    last_parser.add_argument(
        "count", metavar = "N", type = int, help = "Cantidad de comandos"
    )

    last_parser.set_defaults(handler = HistoryController.add_last)

    #DELETE PARSER

    delete_parser = history_subparser.add_parser(
    "delete", help = "elimina un comando del un perfil"
    )

    delete_subparser = delete_parser.add_subparsers(
        dest = "delete_action", required = True,
    )

    delete_all = delete_subparser.add_parser(
        "all", help = "todos los comandos"
    )

    delete_all.set_defaults(handler = HistoryController.delete_all)

    delete_num = delete_subparser.add_parser(
        "index", help = "indice del comandos"
    )

    num_index = delete_num.add_argument(
        "num_index", metavar = "N", type = int, help = " indice del comando"
    )

    delete_num.set_defaults(handler = HistoryController.delete_index)

    

    



    