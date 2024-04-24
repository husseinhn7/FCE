import argparse

        
Main_parser = argparse.ArgumentParser(prog = "fce" , description ="FabriCam extension manager")
subparsers = Main_parser.add_subparsers(title='Available Programs', dest='program')

def p(msg):
    print(msg)

def create_command(command : dict  ) :
    parser = subparsers.add_parser( name = command['name'] , description = command['help'] , help = command['help'])
    for option in command['options']:
        parser.add_argument( option['fullFlag'] ,  help = option['help']   )

