#  py -m pip install sphinx-autoapi
# to conf.py add

#extensions.append('autoapi.extension')

#autoapi_type = 'python'
#autoapi_dirs = ['../src']

class Application:
    """this is my application
    """    

    def __init__(self):
        pass

    def do_something(self, your_number : int) -> str:
        """this function does something"""        
        pass


def something():
    """does another things
    """    
    pass
