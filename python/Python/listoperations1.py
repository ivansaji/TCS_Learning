def List_Op(Mylist, Mylist2):
    # Write your code here
    print(Mylist)
    print(Mylist[1])
    print(Mylist[-1])
    Mylist.append(3)
    Mylist[3] = 60
    print(Mylist)
    print(Mylist[1:5])
    Mylist.append(Mylist2)
    print(Mylist)
    Mylist.extend(Mylist2)
    print(Mylist)
    Mylist.pop()
    print(Mylist)
    print(len(Mylist))