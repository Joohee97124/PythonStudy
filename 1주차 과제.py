"""
파뿌리 1주차 과제
정주희

"""

#변수 1.

K = 50
M = 80
E = 30

print ((K+M+E)/3)



#변수 2.
a = 409298570

if a%2==0 :
    print("짝수입니다.")
elif a%2==1 : 
    print("홀수입니다.")



#변수 3.

word = "국어:수학:영어:프로그래밍"
word2 = word[0:2]+","+word[3:5]+","+word[6:8]+","+word[9:14]
print(word2)



#변수 4.

A = [1,70, 3, 80, 5]
A.reverse()
print(A)



#변수 5.

B = ["파이썬은", "정말", "편하다"]
B.remove("정말")
B.remove("편하다")
B.append("파이썬은 정말 편하다")
B.remove("파이썬은")

print(B)

"""
remove를 이용해서 리스트 안의 요소들을 지운 후 (1개는 남겨둔다)
append를 이용해서 넣고 싶은 요소를 넣는다.
그리고 필요 없는 요소를 마지막으로 다시 제거 한다. (remove 이용)
"""

#변수 6.

C = [1, 50, 410, 10, 3, 4, 5]
C.sort()
print(C)



#변수 7.

D = " I love python "
D.rstrip()

print(D)



#제어문 1.

sum = 0
for i in range(1,101) : 
    sum += i
    print(sum)



#제어문 2.
    
n = 0
sum = 0

while n < 100 :
    n = n+1
    sum += n
    print(sum)




#제어문 3.

n = 0
sum = 0
while n < 100:
    n = n+1
    if n%3==0 :
        sum += n
        print(sum)



#제어문 4.

A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]

i = 0
sum = 0
avg = 0

for i in A :
   sum += i
   avg = sum / len(A)
   print(avg)



#제어문 5.

B = [1, 3, 5, 40, 90, 100, 2020]

for i in B :
    if i%2==1 :
        i = i*2

    print(i)


#제어문 6.

for i in range(1,6) :
    print("*" * i)
    print(end='')



#함수와 입출력 1.
    
a = int(input ("점수를 입력하세요.:"))

if a > 80 :
    print("A")
elif 80 > a > 50 :
    print("B")
elif 50 > a > 30 :
    print("C")
else :
    print("F")



#함수와 입출력 2.

b = int (input ("숫자를 입력하세요.:"))

if b%2 == 0 :
    print("TRUE")
else :
    print("FALSE")
    


#함수와 입출력 3.

c = input ("주민등록번호를 입력하세요.:")

year = c[0:2]

if int(c[6]) == 1 :
    print(year,"남자")
else :
    print(year,"여자")



#함수와 입출력 4.

d = int (input("숫자1:"))
e = input("연산자")
f = int (input("숫자2:"))

def add(x,y) :
    return x+y

def sub(x,y) : 
    return x-y

def mul(x,y) :
    return x*y

def div(x,y) :
    return x/y

def ever(x,y) :
    return x%y

if e == "+" :
    print(add(d,f))
elif e == "-" :
    print(sub(d,f))
elif e == "*" :
    print(mul(d,f))
elif e == "/" :
    print(div(d,f))
elif e == "%" :
    print(ever(d,f))


#함수와 입출력 5.

f = int (input ("거스름돈 입력:"))

f5000 = f//5000
f = f%5000
f1000 = f//1000
f = f%1000
f500 = f//500
f = f%500
f100 = f//100
f = f%100
f50 = f//50
f = f%50
f10 = f//10

print( "5000원 : " , f5000,"개\n" 
       "1000원 : " , f1000, "개\n"
       "500원 : ", f500, "개\n"
       "100원 : ", f100 , "개\n"
       "50원 : ",f50 , "개\n"
       "10원 : ", f10 , "개\n")



#함수와 입출력 6.

import math

a = int (input ("x^2의 계수를 입력하세요: \n"))
b= int (input("x의 계수를 입력하세요: \n"))
c = int (input("상수를 입력하세요 : \n"))

if b**2-(4*a*c) < 0:
    print ("해 없음")
elif b**2-(4*a*c) == 0 :
    print("%d" %(-b/2*a))
elif b**2-(4*a*c) > 0:
    x1 = (-b + (b**2-4*a*c)**0.5) / (2*a)
    x2 = (-b - (b**2-4*a*c)**0.5) / (2*a)
    print("x1 =",x 1, "x2 =", x2)

"""
    이차방정식의 근은 허수, 중근, x2개 인 경우로 나뉘며
    근의 공식을 통해 x2개의 값을 추론했다.
"""








    
    






