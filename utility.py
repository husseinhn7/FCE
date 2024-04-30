import os 
import mimetypes
import json
import shutil 

def read_files(path):
    files_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            full_path = os.path.join(root, file)
            files_list.append(full_path)
    return  files_list


def get_all_extensions(path):
    All_files = []
    extensions = set()
    for root, dirs, files in os.walk(path):
        if "node_modules" not in root:
            for file in files:
                All_files.append(root)
                
                _, extension = os.path.splitext(file)
                extensions.add(extension.lower()) 
    extensions = { x for x  in extensions if x != "" }
    return extensions



def create_xml(path):
    with open(f"../{path}/[Content_Types].xml" , "w") as f :
        f.write('<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">')
        f.write(f'<Default Extension=".vsixmanifest" ContentType="text/xml" />')
        f.write(f'<Default Extension=".xml" ContentType="text/xml" />')
        content_type = {
            ".txt" : "text/plain",
            ".pkgdef" : "text/plain",
            ".xml" : "text/xml",
            ".vsixmanifest" : "text/xml",
            ".html" : "text/html",
            ".css" : "text/css",
            ".js" : "text/js",
            ".rtf" : "application/rtf",
            ".pdf" : "application/pdf",
            ".gif" : "image/gif",
            ".jpg" : "image/jpg",
            ".tiff" : "image/tiff",
            ".vsix" : "application/zip",
            ".zip" : "application/zip",
            ".dll" : "application/octet-stream",          
        }
        for ext in get_all_extensions("."):
            try:
                
                type = mimetypes.types_map[ext]
            except KeyError:
                try:               
                    type = content_type[ext]
                except KeyError: 
                    type = "application/octet-stream"
            
            f.write(f'<Default Extension="{ext}" ContentType="{type}" />')
        f.write('</Types >')

def get_value(dict , key):
    try:
        return dict[key]
    except KeyError:
        return ""

def check_value(dict:dict , key:str , tag:str):
    value = get_value(dict , key)
    if value:
        return tag.format(value)
    return ''
    
    
def read_json_package():
    try : 
        with open("package.json" , 'r') as file :
            f = json.load(file)
            return f
    except :
        print("could not found package.json file")


def create_manifest(data, path):
    if data:
        with open(f'../{path}/extension.vsixmanifest' ,  "w" ) as manifest :
            content  = f'''
            <?xml version="1.0" encoding="utf-8"?>
                        <PackageManifest Version="2.0.0" xmlns = "http://schemas.microsoft.com/developer/vsx-schema/2011" xmlns:d="http://schemas.microsoft.com/developer/vsx-schema-design/2011">
                            <Metadata>
                                <Identity Language="en-US" Id="{data["name"]}" Version="{data["version"]}" Publisher="{data["publisher"]}"/>
                                    <DisplayName>{data['displayName']}</DisplayName>
                                        <Description xml:space="preserve">{data["description"]}</Description>
                                    <Tags>markdown,pdf,convert,vscode</Tags>
                                    <Categories>{ data['categories'][0] }</Categories>
                                    <GalleryFlags>Public</GalleryFlags>    
                                    <categories></>
                                        <Properties>
                                            <Property Id="Microsoft.VisualStudio.Code.Engine" Value="{get_value(data , "engines")['vscode']}" />
                                            <Property Id="Microsoft.VisualStudio.Code.ExtensionDependencies" Value="{get_value(data ,"extensionDependencies")}" />
                                            <Property Id="Microsoft.VisualStudio.Code.ExtensionPack" Value="{get_value(data ,"extensionPack")}" />
                                            <Property Id="Microsoft.VisualStudio.Code.ExtensionKind" Value="{get_value(data ,"extensionKind")}" />
                                            <Property Id="Microsoft.VisualStudio.Code.LocalizedLanguages" Value="{get_value(data ,"localizedLanguages")}" />
                                            {check_value(data ,'preRelease' , '<Property Id="Microsoft.VisualStudio.Code.PreRelease"  Value = "{}" />' ) }
                                            {check_value(data ,'sponsorLink' ,'<Property Id="Microsoft.VisualStudio.Code.SponsorLink" Value ="{}" />')}
                                            {check_value(data , "repository" , '<Property Id="Microsoft.VisualStudio.Services.Links.Source" Value="{}" />')}
                                            {check_value(data , "repository" , '<Property Id="Microsoft.VisualStudio.Services.Links.Getstarted" Value="{}" />')}
                                            {check_value(data , "repository" , '<Property Id="Microsoft.VisualStudio.Services.Links.GitHub" Value="{}" />')}
                                            {check_value(data , "bugs" ,  '<Property Id="Microsoft.VisualStudio.Services.Links.Support" Value="{}" />') }
                                            {check_value(data , "homepage" , '<Property Id="Microsoft.VisualStudio.Services.Links.Learn" Value="{}" />') }
                                            {check_value(data , "galleryBanner.color" , '<Property Id="Microsoft.VisualStudio.Services.Branding.Color" Value="{}" />')}
                                            {check_value(data , "galleryBanner.theme" , '<Property Id="Microsoft.VisualStudio.Services.Branding.Theme" Value="{}" />')}
                                            <Property Id="Microsoft.VisualStudio.Services.GitHubFlavoredMarkdown" Value="{get_value(data, "githubMarkdown")}" />
                                            <Property Id="Microsoft.VisualStudio.Services.Content.Pricing" Value="{get_value(data, "pricing")}"/>
                                            {check_value(data , "enableMarketplaceQnA" , '<Property Id="Microsoft.VisualStudio.Services.EnableMarketplaceQnA" Value="{}" />')}
                                            {check_value(data , "customerQnALink" , '<Property Id="Microsoft.VisualStudio.Services.CustomerQnALink" Value="{}" />')}
                                            </Properties>                                                                
                                </Metadata>
                                <Installation>
                                    <InstallationTarget Id="Microsoft.VisualStudio.Code"/>
                                </Installation>
                                <Dependencies/>
                                <Assets>
                                    <Asset Type="Microsoft.VisualStudio.Code.Manifest" Path="extension/package.json" Addressable="true" />
                                    <Asset Type="Microsoft.VisualStudio.Services.Content.Details" Path="extension/README.md" Addressable="true" />
                                    <Asset Type="Microsoft.VisualStudio.Services.Icons.Default" Path="extension/images/icon.png" Addressable="true" />
                                </Assets>
                                </PackageManifest>           
            '''
            manifest.write(content)
            
            


    
  
def ignore_function(directory, contents):
    items_to_exclude = ['extension.vsixmanifest', '[Content_Types].xml' , 'package-lock.json', 'node_modules' , 'vscode-drawio-1.6.6']
    return [item for item in contents if item in items_to_exclude]



       
def create_vsix(data , args):
    output_path = "./"
    if args.out:
        output_path = args.out
    final_name = f"{data['name']}-{data['version']}"
    shutil.copytree('./' , f"../{final_name}/extension" , ignore = ignore_function )
    create_manifest(data , final_name)
    create_xml(final_name)
    shutil.make_archive( f"../{final_name}" , "zip" , f"../{final_name}" )
    os.rename(f"../{final_name}.zip" , f"../{final_name}.vsix")
    shutil.move(f"../{final_name}.vsix" , output_path)
    shutil.rmtree(f"../{final_name}")


