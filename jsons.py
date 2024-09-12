
from json import load, dump


data = None
def json_load(name):
    global data
    try:
     with open(name, "r", encoding="utf-8") as f:
        return load(f)
    
    except:
       data = {}
     
    
       
        
    
def json_dump(name, path):
    data = json_load()
    print(name)
    print(path)
    data[name] = path
    with open("program_path.json", "w", encoding="utf-8") as f:
        dump(data, f, ensure_ascii=True, indent=4)