def resume(first, second, parent, city, phone, start, strfind, string1):
    # Write your code here
    first = first.strip()
    first = first.capitalize()
    second = second.strip()
    second = second.capitalize()
    parent = parent.strip()
    parent = parent.capitalize()
    print(first,second,parent,city.strip())
    print(phone.isnumeric())
    print(phone.startswith(start))
    a = first+second+parent+city
    print(a.count(strfind))
    print(string1.split())
    print(city.find(strfind))
    