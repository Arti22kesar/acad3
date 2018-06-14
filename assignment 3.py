#Ques1.

list=[]
name1=input("enter the input for the list")
list.append(name1)
name2=input("enter the input for the list")
list.append(name2)
print("the list is",list)


#Ques2.

a=[]
b="google","apple","facebook","microsoft","tesla"
a.append(b)
print(a)

#Ques3.

a="google","apple","google","facebook","google"
print(a.count("google"))


#Ques4.

a=[1,8,4,3,6]
a.sort()
print(a)


#Ques5.

a=[1,2,3,4]
b=[5,6,7]
c=a+b
print(c)

#Ques6.

a=[1,2,3,4,5]
a.pop()
print(a)


#Ques7.

number =(1,2,3,4,5,6,7)
print("total evens:",len([i for i in number if(i%2==0)]))
print("total odds:",len([i for i in number if(i%2!=0)]))