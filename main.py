from cli.parser import Parser

from services.StartupService import StartupService

class Main:
    def __init__(self):
        self.__parser = Parser()
        StartupService().initialize() 

    def __execute(self):
        args = self.__parser.get_parser()
        args.handler(args)

    def run(self):
        self.__execute()

if __name__ == '__main__':
    App = Main()
    App.run()
     