import os 
import json





home_dir = os.path.expanduser('~')



    
def open_store():
    store_path =   ".fce"
    try:
        with open(store_path , "r") as store:
            data = store.read()
            store = json.loads(data)
            return store
    except FileNotFoundError:
        with open(store_path , "w") as store:
            data = json.dumps([])
            store.write(data)
            return []








def save(store_data):
   
    store_path =   ".fce"
    with open(store_path , "w") as store :
        store.write(json.dumps(store_data))




def get_publisher(publisher):
    store = open_store()
    for publisher_obj in store :
        if publisher == publisher_obj["name"] :
            return publisher_obj
    return False
    
    


def add_publisher( args ):
    publisher = args.pub
    pat = args.pat
    
    store = open_store()
    if get_publisher(publisher):
        return print("publisher already exists")
    new_publisher  = { "name" : publisher , "pat" : pat }
    store.append(new_publisher)  
    save(store)
    print(f"publisher {publisher} has been logged successfully ")
     
     
     


def delete_publisher(args):
    publisher = args.pub
    store = open_store()
    if not get_publisher(publisher):
        return print("publisher does not  exists")
    for publisher_obj in store:
        if publisher == publisher_obj["name"]:
            store.remove(publisher_obj)
            save(store)
            print(f"publisher {publisher} has been removed")
            break



def list_publishers( args ):
    store = open_store()   
    for publisher_obj in store:
        print(publisher_obj["name"])
