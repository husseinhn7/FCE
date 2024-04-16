from command import commands
from ArgParser import create_command , Main_parser 



for command in commands :
    create_command(command )
    
Main_parser.parse_args()



