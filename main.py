from command import commands  
from ArgParser import create_command , Main_parser 
from function_handlers import command_handlers


for command in commands :
    create_command( command )
    
arg = Main_parser.parse_args()



# try:
command_handlers[arg.program](arg)
# except KeyError:
#     print("no command exist ")

