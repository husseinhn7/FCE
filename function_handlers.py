import os 
from utility import read_files , create_vsix

def ls_Handler(args):
    files_list = read_files(".")   
    ignore_file = ".fceignore"  
    if args.ignoreFile:
        ignore_file = args.ignoreFile
    try:       
        with open(ignore_file , 'r' ) as f :
            for file in f :
                ignored = file.strip()
                files_list = [x for x in files_list if ignored not in x ]
    except:
        print(".fceignore file is not found")
    
    for file in files_list:
        print(file)

    









def pack_Handler(args):
    create_vsix()

















def publish_Handler(args):
    pass
def unpublish_Handler(args):
    pass
def login_Handler(args):
    pass
def logout_Handler(args):
    pass
def ls_publishers_Handler(args):
    pass
def delete_publisher_Handler(args):
    pass
def verify_pat_Handler(args):
    pass
def show_Handler(args):
    pass
def search_Handler(args):
    pass



command_handlers = {
    "ls"                :  lambda x : ls_Handler(x),
    "pack"              :  lambda x : pack_Handler(x),
    "publish"           :  lambda x : pack_Handler(x),
    "unpublish"         :  lambda x : unpublish_Handler(x),
    "login"             :  lambda x : login_Handler(x),
    "logout"            :  lambda x : logout_Handler(x),
    "ls_publishers"     :  lambda x : ls_publishers_Handler(x),
    "delete_publisher"  :  lambda x : delete_publisher_Handler(x),
    "verify_pat"        :  lambda x : verify_pat_Handler(x),
    "show"              :  lambda x : show_Handler(x),
    "search"            :  lambda x : search_Handler(x),
}