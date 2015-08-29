#!/usr/bin/python
#########################################################################################
#Author:james<jamesh_1992@126.com>
#Create Data:2015.08.29
#Last Modify Data:2015.08.29
#Function:Proxy for remote method
#########################################################################################

syssymbol=['__init__','__repr__','__name__','__qualname__','__module__','__defaults__',\
           '__code__','__globals__','__dict__','__closure__','__annotations__','__kwdefaults__',\
           '__new__','__del__','__rper__','__str__','__bytes__','__format__','__lt__','__le__',\
           '__eq__','__ne__','__gt__','__ge__','__hash__','__bool__','__getattr__','__getattribute__'\
           '__setattr__','__delattr__','__dir__','__get__','__set__','__delete__','__slots__','__prep__']
def callable(o):
    return (type(o) == 'function' or hasattr(o,'__call__'))

class PermitionDenied(Exception):
    def __repr__(self):
        return "Never Call a Remote Method Start With '_'"

class ProxyHandlerError(Exception):
    def __repr__(self):
        return "Proxy Need a Callable Object/Method!"

class ProxyCaller:
        
    def __init__(self, name, handler):
        self.__dict__['.caller_name']=name
        self.__dict__['.caller_handler']=handler
        
    def __call__(self, *args, **kwargs):
        return self.__dict__['.caller_handler'](self.__dict__['.caller_name'], *args, **kwargs)

    def __getattr__(self, name):
#        if name.startswith('_'):
#            print name
#            raise PermitionDenied
            #pass

        if name not in self.__dict__:
            if name.startswith('_'):
                raise PermitionDenied
            self.__dict__[name]=ProxyCaller(self.__dict__['.caller_name']+'.'+name, self.__dict__['.caller_handler'])

        return self.__dict__[name]

    def __rper__(self):
        pass
    
class Proxy:

    def __init__(self, proxy_handler):
        if proxy_handler is not None and callable(proxy_handler):
            self.__dict__['.handler']=proxy_handler
        else:
            raise ProxyHandlerError

    def __getattr__(self, name):
#        if name.startswith('_'):
#            raise PermitionDenied
            #pass

        if name not in self.__dict__:
            if name.startswith('_'):
                raise PermitionDenied
            self.__dict__[name] = ProxyCaller(name, self.__dict__['.handler'])

        return self.__dict__[name]

    def __rpel__(self):
        return "Proxy for Remote Calls"
