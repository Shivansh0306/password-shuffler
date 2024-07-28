list1=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

while True:
    con=input("type yes for continue or no for exit: ")
    if con=='yes':
        name=input("enter the message: ")
        shift=int(input("enter the shift number: "))
        instruction=input("enter encrypt or decrypt: ")
        if instruction =='encrypt':
            for i in name:
                if i in list1:
                    l3=''.join(list1)
                    l2=l3.find(i)
                    l2+=shift
                    if l2>25:
                        l2=l2-25
                    t=list1[l2]
                    print(t,end='')
                else:
                    print(" ",end='')

        elif instruction=='decrypt':
            for j in name:
                if j in list1:
                    l3=''.join(list1)
                    l2=l3.find(j)
                    l2-=shift
                    #if l2<0:
                        #l2=l2+26
                    k=list1[l2]
                    print(k,end='')
                else:
                    print(" ",end='')

        else:
            print("wrong entry")

    else:
        print("goodbye")
        break
    print()
