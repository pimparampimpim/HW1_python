n=int(input())

n1=n%10
n2=n%60
n3=n2%10
if n>8:
    if n>34 :
        if n>59:
            if n2<9:
                print(n2,'0',n//60)
            else:
                if n2<35:
                    if n3<9:
                        print(n3,n2//10,n//60)
                    else:
                        if n2%10!=0:
                            print('0',n2//10+1,n//60)
                        else:
                            print('0',n2//10,n//60)
                else:
                    if n2!=0:
                         print('0','0',n//60+1)
                    else:
                        print('0','0',n//60)
        else:
            if n>34:
                print('0','0','1')
            else:
                if n1<9:
                    print(n1,n//10,'0')
                else:
                    if n1%10!=0:
                        print('0',n//10+1,'0')
                    else:
                         print('0',n//10,'0')
    else:
        if n1<9:
            print(n1,n//10,'0')
        else:
            if n1%10!=0:
                print('0',n//10+1,'0')
            else:
                print('0',n//10,'0')
else:
    (n,'0','0')


                       
                


