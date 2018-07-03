good_modules = ["numpy","math", "random"]

def sandbox(text):
    import sys, __builtin__, importlib
    
    my_modules = {}
    for m in good_modules:
        my_modules[m] = importlib.import_module(m)
        
    def my_import(name, *params):
        if not name in my_modules and not name.split(".")[0] in my_modules:
            raise ImportError(name)

        if '.' in name:
            return saved_import(name, *params)
        else:
            return my_list[name]
        
    try:
        saved_open = __builtin__.open
        saved_file = __builtin__.file
        saved_import = __builtin__.__import__

        __builtin__.__import__ = my_import
        del __builtin__.open
        del __builtin__.file

        exec text in {}, {}
    except:
        raise
    finally:
        __builtin__.__import__ = saved_import
        __builtin__.open = saved_open
        __builtin__.file = saved_file
