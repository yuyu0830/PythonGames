import random

def fin_err(ins) :
    inc = str(ins)
    if len(inc) != 4 :
        return 0
    else :
        for i in range(0,9) :
            ck = inc.count(str(i))
            if ck >= 2 :
                return 0
            
        return 1

def rand() :
    num = []
    ran = str(random.randint(1,9))
    num.append(ran)
    i = 0
    
    while i != 3 :
        ran = str(random.randint(0,9))
        if ran not in num :
            num.append(ran)
            i += 1
    return num

def sb(num, inc) :
    i = 0
    b = 0
    for i in range(0,4):
        if inc[i] == num[i]:
            b += 1
    return b

def sc(num, inc) :
    i = 0
    c = 0
    for i in range(0,4):
        if inc[i] in num:
            c += 1
    return c

def main() :
    num = rand()
    num_t = str(num[0]) + str(num[1]) + str(num[2]) + str(num[3])
    turn = 1
    b = 0
    
    while turn <= 10 and b != 4 :
        ins = int(input("\n{}번째 턴입니다.\n예상 값을 입력해주세요 : ".format(turn)))
        while fin_err(ins) == False :
            ins = int(input("잘못된 입력입니다.\n값을 다시 입력해주세요 : "))

        inc = str(ins)
        
        b = sb(num, inc)
        c = sc(num, inc)

        if c == 0 and b > 0 :
            continue
        else :
            c = c - b
        

        if b == 4 :
            print("축하합니다! 정답입니다!\n입력횟수 {}번".format(turn))

        elif b!= 4 and turn > 9 :
            print("실패입니다. Game Over\n정답 : " + num_t)

        else :
            print("{}B{}C".format(b, c))
            turn += 1

main()
re = int(input("다시하시려면 1, 아니면 0 을 눌러주세요 : "))
if re == 1 :
    re = 0
    main()
    
