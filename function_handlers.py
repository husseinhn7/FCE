import os 
from utility import read_files , create_vsix , read_json_package
from msrest.authentication import BasicAuthentication
from azure.devops.v7_1.gallery import GalleryClient
import io

from publish import publish
from store import add_publisher , list_publishers , delete_publisher



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
    data = read_json_package() 
    create_vsix(data , args )


















def publish_Handler(args):
    # print(args)         
    organization_url =  'https://marketplace.visualstudio.com'   

    try:
        pat = args.pat
        
    except : 
        return print("personal access token is required ")
    try:
        data = read_json_package()
        name = f"{data['name']}-{data['version']}.vsix" 
        print(name)      
        with open(rf"{name}" , "rb") as f:
            file = f.read()
            data_stream = io.BytesIO(file)
    except:
        return print(".vsix file is not found ") 
    credentials = BasicAuthentication('', pat)
    m = GalleryClient(base_url=organization_url, creds=credentials)
    m.create_extension(data_stream)









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
    "publish"           :  lambda x : publish(x),
    "unpublish"         :  lambda x : unpublish_Handler(x),
    "login"             :  lambda x : add_publisher(x),
    "logout"            :  lambda x : delete_publisher(x),
    "ls-publishers"     :  lambda x : list_publishers(x),
    "delete_publisher"  :  lambda x : delete_publisher_Handler(x),
    "verify_pat"        :  lambda x : verify_pat_Handler(x),
    "show"              :  lambda x : show_Handler(x),
    "search"            :  lambda x : search_Handler(x),
}