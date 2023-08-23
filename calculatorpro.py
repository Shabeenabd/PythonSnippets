def calc(x=0):
    if x==0:
            original=input("ENTER :")
    else:
            original=str(x)
    try :
        
        plus=original.split("+")
        minus=[]
        molus=[]
        for i in plus:
            if "-" in i:
                minus=minus+i.split("-")
            else:
                molus=molus+[i]
        div=[]
        for j in minus:
            if "/" in j:
                div=div+j.split("/")
                for i in div:
                    if "*" in str(i):
                        a=i.split("*")
                        res=1
                        for k in a:
                            res=res*float(k)
                        div[div.index(i)]=res
                        
                res=int(div[0])
                for i in div[1::]:
                    res=res/float(i)
                minus[minus.index(j)]=res
            else:
                if "*" in str(j):
                    b=j.split("*")
                    ans=1
                    
                    for y in b:
                        ans=ans*float(y)
                        
                    minus[minus.index(j)]=ans
        dov=[]
        for j in molus:
            if "/" in j:
                dov=dov+j.split("/")
                for i in dov:
                    if "*" in str(i):
                        a=i.split("*")
                        res=1
                        for k in a:
                            res=res*float(k)
                        dov[dov.index(i)]=res
                        
                res=int(dov[0])
                for i in dov[1::]:
                    res=res/float(i)
                molus[molus.index(j)]=res
            else:
                if "*" in str(j):
                    b=j.split("*")
                    ans=1
                    
                    for y in b:
                        ans=ans*float(y)
                        
                    molus[molus.index(j)]=ans
        plu=0
        for i in molus:
            plu=plu+float(i)
        minu=0
        if len(minus)>0:
            minu=float(minus[0])
            for i in minus[1::]:
                minu=minu-float(i)
        else:
            minu=0

        final=plu+minu
        if ".0" in str(final):
            return (int(final))
        else:
            return(float(final))
                     
    except:
        a="syntax error"
        print(a)  
        return a
print(calc())

