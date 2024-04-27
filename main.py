from command import commands  , ls 
from ArgParser import create_command , Main_parser 
from function_handlers import command_handlers


for command in commands :
    create_command( command )
    
arg = Main_parser.parse_args()





command_handlers

try:
    command_handlers[arg.program](arg)
except KeyError:
    print("no command exist ")






# if arg.program == "ls" :
#     if arg.yarn:
#         print(" fuck offffffff ")
f = arg.program
# commands_functions[arg.program](arg)
# print(arg.accumulate(arg.program))


