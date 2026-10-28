number = [10,25,45,13,56,80,97,100]
print("original list:",number)
n=int(input("enter the number to be searched:"))
if n in number:
  print(n,"is in the list")
else:
    print(n,"is not in the list")
print("original list:",number)
new_number=int(input("enter the number to be update:"))
pos=int(input("enter the position of new number:")) 
number[pos]=new_number
print("updated list:",number)
filtered=[]
num =int(input("enter the number:"))
for i in number:
  if i>num:
   filtered.append(i)
print("filtered list:",filtered)
student=["ram","shyam","hari","gita"]
print("original list:",student)
student.append("sita")
student.sort()
print("updated list:",student)