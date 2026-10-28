txt = input("Enter a string: ").lower()
print("Reverse = ", txt[::-1])
if txt == txt[::-1]:
    print(txt, "is Palindrome.")
else:
  print(txt, "is not Palindrome.")