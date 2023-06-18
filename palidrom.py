#def palindrome(s): 
 #  return s[::-1] == s 

#while True: 
 #   s = input("введите слово: ") 
  #  if palindrome == s:
   #     print("это слово является палиндромом")
   # else:
    #    print("это слово не является палиндромом")


s = input("введите слово: ")
h = len(s) // 2
#print(s[:h] == s[:len(s)-h-1:-1])
if s[:h] == s[:len(s)-h-1]:
     print("True")
else: 
     print("false")