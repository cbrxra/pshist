from cli.parser import Parser

from services.StartupService import StartupService

from utils.Colors import RED, RESET

class Main:
    def __init__(self):
        self.__parser = Parser()
        StartupService().initialize()
        

    def __execute(self):
        args = self.__parser.get_parser()
        args.handler(args)


        """if args.command == "create":
            CreateCommand(args).exec()

        elif args.command == "list":
            ListCommand(args).exec()

        elif args.command == "use":
            UseCommand(args).exec()

        elif args.command == "view":
            ViewCommand(args).exec()

        elif args.command == "config":
            ConfigCommand(args).exec() 

        elif args.command == "delete" or args.command == "del":
            DeleteCommand(args).exec()

        elif args.command == "add":
            AddCommand(args).exec()

        else:
            print(RED + f"Error: {RESET} Comando '{args.command}' no encontrado")"""

    def run(self):
        self.__execute()



if __name__ == '__main__':
    App = Main()
    App.run()
     