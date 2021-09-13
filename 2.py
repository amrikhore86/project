def convert(l):
    nl=[]
    nl=[l[-1]]+l[0:len(l)-1]
    print(nl)
l=list(map(int,input("Enter a list").split()))
convert(l)
