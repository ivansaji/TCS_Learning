def Escape(s1, s2, s3):
    # Write your code here
    s="Python\tRaw\nString\tConcept"
    print(s1,s2,s3,sep="\n")
    print(s1,s2,s3,sep="\t")
    print(s)
    s=repr(s).replace("'","")
    print(s)