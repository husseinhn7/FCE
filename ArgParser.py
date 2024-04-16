import argparse

# Main_parser = argparse.ArgumentParser(prog = "fce" , description ="FabriCam extension manager")
# subparsers = Main_parser.add_subparsers(title='Available Programs', dest='program')
# class ArgParser:
#     def __init__(self , command : dict  , main , sub ) -> None:     
#         self.command = command
#         self.sub = sub
#         self.main = main
#         self.create_command()
#     def create_command(self):
#         parser = self.sub.add_parser( name = self.command['name'] , description = self.command['help'] , help = self.command['help'])
#         for option in self.command['options']:
#             parser.add_argument( option['fullFlag'] , help = option['help'] ,  action='store_true', )
#     def __str__(self) -> str:
#         return self.command['name']
        
        
Main_parser = argparse.ArgumentParser(prog = "fce" , description ="FabriCam extension manager")
subparsers = Main_parser.add_subparsers(title='Available Programs', dest='program')


def create_command(command : dict  ) :
    parser = subparsers.add_parser( name = command['name'] , description = command['help'] , help = command['help'])
    for option in command['options']:
        parser.add_argument( option['fullFlag'] , help = option['help'] ,  action='store_true', )
