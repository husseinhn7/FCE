from utility import read_json_package
from msrest.authentication import BasicAuthentication
from azure.devops.v7_1.gallery import GalleryClient
import io
from store import get_publisher 


def publish(args):
    organization_url = 'https://marketplace.visualstudio.com' 
    print(organization_url)  
    # try:
    #     pat = args.pat
    # except : 
    #     return print("personal access token is required ")
    # try:
    data = read_json_package()
    publisherName = data['publisher']

    publisher = get_publisher(publisherName)
    
    
    if not publisher:
        return NameError("fuck off")
    
    
    pat = publisher[publisherName]  
     
    name = f"{data['name']}-{data['version']}.vsix" 
    with open(rf"{name}" , "rb") as f:
        file = f.read()
        data_stream = io.BytesIO(file)
    # except:
    #     return print(".vsix file is not found ") 
    credentials = BasicAuthentication('', pat)
    client = GalleryClient(base_url = organization_url, creds = credentials)
    client.create_extension(data_stream)


