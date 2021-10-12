def triplet(color):
    Light_count=0
    Hue_count=0
    result=0
    le = len(color)
    
    for i in range(0,le-1):
        if color[i] == 'L':
            Light_count=Light_count+1
        
    for i in range(0,le-1):
        if color[i] == 'L':
            Light_count=Light_count-1
        
        if color[i] == 'H':
            Hue_count=Hue_count+1
        
        if color[i] == 'S':
            result = result+Hue_count*Light_count
    
    return result

color = "HHSSLLHSSLL"
print("Number of ordered triplets is" + str(triplet(color))