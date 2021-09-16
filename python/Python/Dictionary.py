def myDict(key1, value1, key2, value2, value3, key3):
    # Write your code here
    d={key1:value1}
    print(d)
    
    d[key2]=value2
    print(d)
    
    d[key1]=value3
    print(d)
    d.pop(key3)
    return d