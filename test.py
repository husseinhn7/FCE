from ArgParser import create_command , Main_parser
from command import ls , pack


create_command(ls)
create_command(pack)



Main_parser.parse_args()











