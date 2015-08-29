#!/usr/bin/python

import wrapfunc
import remotecall
import remote

proxy_call = remotecall.remote_proxy
Proxy = wrapfunc.Proxy

def proxy_handler(name, *args, **kwargs):
    print proxy_call(remote, name, *args, **kwargs)

proxy = Proxy(proxy_handler)
proxy.time.now()
proxy.ti.time()
proxy.time()

class DomainClass:
    def __init__(self):
        self.proxy=Proxy(self.proxy_handler)
        self.proxy.time.now()
    
    def proxy_handler(self, name, *args, **kwargs):
        print proxy_call(remote, name, *args, **kwargs)

domain = DomainClass()
domain.proxy.test()
