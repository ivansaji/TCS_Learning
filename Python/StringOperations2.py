def resume(first, second, parent, city, phone, start, strfind, string1):
    # Write your code here
    first=first.replace(" ","").capitalize()
    second=second.replace(" ","").capitalize()
    parent=parent.replace(" ","").capitalize()
    city=city.replace(" ","")
    
    new_str=first+" "+second+" "+parent+" "+city
    print(new_str)
    
    if phone.isdigit():
        print("True")
    else:
        print("False")
    
    if phone[0]==start:
        print("True")
    else:
        print("False")
    
    print(new_str.count(strfind))
    
    x=string1.split()
    print(x)
    
    print(city.find(strfind))
    