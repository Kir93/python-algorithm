#dict hash
import sys
sys.stdin = open("input.txt", "r")

word1 = input()
word2 = input()

str1 = dict()
str2 = dict()

for x in word1:
    str1[x] = str1.get(x, 0) + 1
for x in word2:
    str2[x] = str2.get(x, 0) + 1

if str1 == str2:
    print('YES')
else:
    print('NO')

#list hash
import sys
sys.stdin = open("input.txt", "r")

word1 = input()
word2 = input()

str1 = [0 for i in range(52)]
str2 = [0 for i in range(52)]

for x in word1:
    if x.isupper():
        str1[ord(x)-65] += 1
    else:
        str1[ord(x)-71] += 1

for x in word2:
    if x.isupper():
        str2[ord(x)-65] += 1
    else:
        str2[ord(x)-71] += 1

for i in range(52):
    if str1[i] != str2[i]:
        print("NO")
        break
else:
    print("YES")

#new mycode
import sys
sys.stdin = open("input.txt", "rt")
a = input()
b = input()
s = dict()
for x in a:
  s[x] = s.get(x, 0) + 1
for x in b:
  s[x] = s.get(x, 0) - 1
for key, val in s.items():
  if val != 0:
    print("NO")
    break
else:
  print("YES")

#new mycode list
