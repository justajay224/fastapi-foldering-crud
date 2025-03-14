import os
from importlib import import_module

def include_routers(app):
    for file in os.listdir(os.path.dirname(__file__)): #cek daftar file
        if file.endswith("_route.py") and file not in {"__init__.py", "index.py"}: #validasi file
            module = import_module(f".{file[:-3]}", __package__) #import file dan menghapus ".py"
            if router := getattr(module, "router", None): #ngecek, dalam modul ada atribute router
                app.include_router(router)