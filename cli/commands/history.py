from controllers.HistoryController import HistoryController


def init_history_command(subparsers):
    history_parser = subparsers.add_parser(
        "history", help = "Administrar historial"
    )

    history_subparser = history_parser.add_subparsers(
        dest = "history_command",
        required = True
    )

    add_parser = history_subparser.add_parser(
        "add",
        help = "agregar comandos al historial del perfil actual"
    )

    add_subparser = add_parser.add_subparsers(
        dest = "add_command",
        required = True
    )

    all_parser = add_subparser.add_parser(
        "all", help = "Agregar todos los comandos pendientes"
    )

    all_parser.set_defaults(handler = HistoryController.add_all)
    
    last_parser = add_subparser.add_parser(
        "last", help = "Agregar los últimos comandos"
    )

    last_parser.add_argument(
        "count", metavar = "N", type = int, help = "Cantidad de comandos"
    )

    last_parser.set_defaults(handler = HistoryController.add_last)