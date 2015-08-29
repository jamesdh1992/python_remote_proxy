#!/usr/bin/python
###########################################################################
#Author:james<jamesh_1992@126.com
#Create Data:2015.08.29
#Last Modify Data:2015.08.29
#Function:Handler Remote Calls
###########################################################################

def remote_proxy(remote, name, *args, **kwargs):
    paths = name.split('.')
    callmodule=remote
    result=None
    for path in paths:
        if hasattr(callmodule,path):
            callmodule=getattr(callmodule,path)
        else:
            result="Path Error:%s" % path
            break

    if result is None:
        if callable(callmodule):
            try:
                result = callmodule(*args, **kwargs)
            except:
                result = "Exception happend where calling method!"
        else:
            result = "Error! Not a Callable Object"
    
    return result

        
