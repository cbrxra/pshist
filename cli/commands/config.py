from controllers.ConfigController import ConfigController

def init_config_command(subparsers):
    config_parser = subparsers.add_parser(
        "config", help = "Administrar configuraciones"
    )

    config_subparser = config_parser.add_subparsers(
        dest = "config_command", required = True
    )

    set_parser = config_subparser.add_parser(
        "set", help = "Modificar una configuración"
    )

    set_subparser = set_parser.add_subparsers(
        dest = "set_command", required = True 
    )

    default_profile_parser = set_subparser.add_parser(
        "defaultprofile", help = "Cambiar perfil por defecto"
    )

    default_profile_parser.add_argument(
        "profile", metavar = "PROFILE", help = "Nombre del perfil"
    )

    default_profile_parser.set_defaults(handler = ConfigController.set_default_profile)

    view_parser = config_subparser.add_parser(
        "view", help = "Mostrar configuraciones"
    )

    view_subparser = view_parser.add_subparsers(
        dest = "view_command", required = True
    )

    view_all = view_subparser.add_parser(
        "all", help = "Mostrar todas las configuraciones"
    )

    view_all.set_defaults(handler = ConfigController.view_all)
    
    view_default_profile = view_subparser.add_parser(
        "defaultprofile", help = "Mostrar el perfil por defecto"
    )

    view_default_profile.set_defaults(handler = ConfigController.view_defaultprofile)

    