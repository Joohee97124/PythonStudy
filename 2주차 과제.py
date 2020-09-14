"""
파뿌리 2주차 과제
정주희
"""



#함수응용 1.

#Lotto.py----------------------------------------------------------------
import random

def Lotto () :
    lotto = random.sample(range(1,46),6)
    lotto.sort()
    return print(lotto) 
#Lotto.py----------------------------------------------------------------

import Lotto
print(Lotto.Lotto())

"""None이 나오는 이유가 __name__ == "__main__"가 거짓 (직접 파일 실행X)이기 때문인가요?"""




#함수응용 2.

#op.py--------------------------------------------------------------------
def add(x,y) :
    return x+y

def sub(x,y) : 
    return x-y

def mul(x,y) :
    return x*y

def div(x,y) :
    return x/y

if __name__ == "__main__" :
  while 1 :
    a = input() # 숫자1 입력부
    b = input() # 연산자 입력부
    c = input() # 숫자2 입력부
    if b == "+" :
     print(a, "+", c, "=", a+c)
    elif b == "-" :
      print(a, "-", c, "=", a-c)
    elif b == "*" :
      print(a, "*", c, "=", a*c)
    elif b == "/" :
      print(a, "*", c, "=", a/c)

try:
    4/0
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")

#op.py끝-------------------------------------------------------------

import op

if __name__ == "__main__" :
  while 1 :
    a = input() # 숫자1 입력부
    b = input() # 연산자 입력부
    c = input() # 숫자2 입력부
    if b == "+" :
     print(a, "+", c, "=", a+c)
    elif b == "-" :
      print(a, "-", c, "=", a-c)
    elif b == "*" :
      print(a, "*", c, "=", a*c)
    elif b == "/" :
      print(a, "*", c, "=", a/c)


x = 100
y = 200
print(op.add(x,y))

"""예외처리에서 try : x/0으로 할 수 있는 방법은 없나요? 항상 4/0,3/0처럼 상수만 와야하나요?"""




#함수응용 3. 

a = input("문자 :")
e = a
print(e)

b = len(e)
c = max(e)

d = e[::-1]

print("문자의 개수 : " , b)
print("가장 큰 문자열 : " ,c)
print("뒤집은 문자열 : " ,d )




#함수응용 4.

import datetime
from datetime import timedelta

now = datetime.datetime.now()
print(now)

soon = (now + timedelta(days=49, hours=1, minutes=8, seconds=7))
print(soon)




#함수응용 5.

#dictionary.py---------------------------------------------------------------
dic = {'apple':'사과', 'banana':'바나나','camel':'낙타'}

print("전체출력")

for key, value in dic.items() :
  print(key,value)

search_dic = input("영어로 검색 : ")

for key, value in dic.items():
  if key == search_dic:
    print(value)

search_dic2 = input("한국어로 검색:")
for key, value in dic.items():
  if value == search_dic2:
    print(key)
#dictionary.py---------------------------------------------------------------


import dictionary

try:
    input ()
except:
  print("언어를 잘못입력하셨습니다.")


"""예외처리에 영어로 검색 시에 한글로 쓰거나 한글로 검색 시에 영어로 쓴 경우를 넣고 싶었는데 어떻게 넣어야할지 모르겠어요"""




