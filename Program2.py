def outer():
    def inner():
        return "hello,im the inner function!"
    
    return inner

retObj = outer()
retInner= retObj()

print(retInner)