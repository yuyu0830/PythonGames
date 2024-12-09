import random

n = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] #숫자 중복 방지용

a = random.randint(1,9) #랜덤 숫자 지정
n.remove(a)
b = random.choice(n)
n.remove(b)
c = random.choice(n)
n.remove(c)
d = random.choice(n)

i = []    #랜덤 숫자 그룹
i.append(a)
i.append(b)
i.append(c)
i.append(d)

p = 1000 #입력값수
t = 1 #턴수
bb = 0 #bulls 값
cc = 0 #cows 값
truea = 1 #입력오류찾기용 논리값
trueb = 0

while t <= 10 and trueb == 0 : #10턴 이하, 4개 다 맞추지 않았을 때
  while p < 1234 or p > 10000 or truea == 1 : # 1234 이상, 9999 미만 입력
    p = int(input("예상 숫자를 입력해주세요 : "))
    
    w = p//1000
    x = (p%1000)//100
    y = (p%100)//10
    z = p%10

    if p < 1234 or p > 10000 :
      print("다시입력해주세요")
      truea = 1
    
    elif w == x or w == y or w == z or x == y or x == z or y == z :
      print("중복되는 숫자가 없게 입력해주세요")
      truea = 1

    else :
      truea = 0


  if a == w : #bulls값 구하기
    bb += 1
  if b == x :
    bb += 1
  if c == y :
    bb += 1
  if d == z :
    bb += 1
    
  if w in i : 
    cc += 1
  if x in i : 
    cc += 1
  if y in i : 
    cc += 1
  if z in i : 
    cc += 1

  if cc == 0 and bb > 0 :
    continue
    
  else :
    cc = cc - bb

  t += 1

  if bb == 4 : #성공
    trueb = 1
    print("성공하셨습니다!")

  elif t>10 : #실패
    print("실패하셨습니다..")
    print("정답은 "+str(a)+str(b)+str(c)+str(d)+"입니다")
    

  else : #다시
    trueb = 0
    print(str(bb)+"B"+str(cc)+"C")
    print("현재 "+str(t)+"턴째 입니다.")

  bb = 0 #값들 초기화
  cc = 0
  p = 1000


