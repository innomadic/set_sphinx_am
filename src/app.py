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

    def do_some_new_feature(self, your_number, your_string):
        """this is a great new feature with

        Args:
            your_number (int): hello
            your_string (str): hello2
        """
        pass


def something():
    """does another things
    """    
    pass
