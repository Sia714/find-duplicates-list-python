def dup(l):
    b=[]
    if " " in l:
        l=l.split(" ")
        for x in l:
            x=int(x)
            b.append(x)
    elif "," in l:
        l=l.split(",")
        for x in l:
            x=int(x)
            b.append(x)
    l1=len(b)
    l2=len(set(b))
    n=[]
    d=[]
    h=[]
    if l1!=l2:
        for i in b:
            if i not in n:
                n.append(i)
            else:
                d.append(i)
        d.sort()
        for k in d:
            if k not in h:
               print(k,":",b.count(k))
               h.append(k)

    else:
        print("no duplicates")


li=input("")
dup(li)
