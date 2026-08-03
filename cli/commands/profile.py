from controllers.ProfileController import ProfileController
from argparse import _SubParsersAction

def init_profile_command(subparsers :_SubParsersAction):

    profile_parser = subparsers.add_parser(
        "profile", help = "Administrar Perfiles"
    )

    profile_subparsers = profile_parser.add_subparsers(
        dest = "profile_command", required = True
    )

    #CREATE PARSER

    create_parser = profile_subparsers.add_parser(
        "create", help = "Crear un perfil"
    )

    create_parser.add_argument(
        "name", help = "Nombre del perfil",
    )

    create_parser.set_defaults(handler = ProfileController.create)

    #DELETE PARSER

    delete_parser = profile_subparsers.add_parser(
        "delete", help = "Eliminar un perfil"
    )

    delete_parser.add_argument(
        "name", help = "Nombre del perfil"
    )

    delete_parser.set_defaults(handler = ProfileController.delete)

    #USE PARSER

    use_parser = profile_subparsers.add_parser(
        "use", help = "Cambiar al perfil"
    )

    use_parser.add_argument("name", help = "Nombre del perfil")

    use_parser.set_defaults(handler = ProfileController.use)

    #LIST PARSER

    list_parser = profile_subparsers.add_parser(
        "list", help = "Ver lista de perfiles"

    )
    
    list_parser.set_defaults(handler = ProfileController.list)

    #VIEW PARSER

    view_parser = profile_subparsers.add_parser(
        "view", help = "Ver lista de comandos de un perfil"
    )

    view_parser.add_argument("name", help = "nombre del perfil")

    view_parser.set_defaults(handler = ProfileController.view)

    #Exit Parser

    exit_parser = profile_subparsers.add_parser(
        "exit", help = "Salir del perfil actual"
    )

    exit_parser.set_defaults(handler = ProfileController.exit)

    # RENAME PROFILE

    rename_parser = profile_subparsers.add_parser(
        "rename", help = "Renombrar un perfil"
    )

    rename_parser.add_argument(
        "name", help = "nombre actual del perfil"
    )

    rename_parser.add_argument(
        "new_name", help = "nombre actual del perfil"
    )

    rename_parser.set_defaults(handler = ProfileController.rename)
    
    #RELOAD

    reload_parser = profile_subparsers.add_parser(
        "reload", help = "Recarga el perfil actual"
    )

    reload_parser.set_defaults(handler = ProfileController.reload)