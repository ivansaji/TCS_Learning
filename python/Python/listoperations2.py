def tuplefunction(list1, list2, string1, n):
    # Write your code here
    tuple1 = tuple(list1)
    tuple2 = tuple(list2)
    c = tuple1+tuple2
    print(c)
    print(c[4])
    nest = (tuple1,tuple2)
    print(nest)
    print(len(nest))
    rep = tuple((string1,)*n)
    print(rep)
    print(max(tuple1))