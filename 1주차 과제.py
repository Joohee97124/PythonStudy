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
    
        


























    
    






