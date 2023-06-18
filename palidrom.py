s = input("введите слово: ")
h = len(s) // 2
if s[:h] == s[:len(s)-h-1]:
     print("True")
else: 
     print("false")