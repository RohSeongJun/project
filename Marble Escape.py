import time
import random
import tkinter

#게임판 보여주는 함수(list)
def showlistboard(y,game):
    print("\n--------게임판--------")
    for i in range(y):
        print(game[i])

#게임판 보여주는 함수
def showboard(h,y,game):
    print("\n--------게임판--------")
    for j in range(0, y):
        for i in range(0, h):
            print(game[j][i], end="")
            
        print("")


#사용자가 직접 만드는 게임판 제작 함수
def domakegameboard():

    #게임판 크기 설정
    h = int(input("\n게임판의 가로 크기를 입력해주세요 : "))
    y = int(input("게임판의 세로 크기를 입력해주세요 : "))
    
    #게임판 크기 구성
    cnt = 1
    game = [["□"] * h for i in range(y)]    #게임판 2차원 리스트
    print("\n게임판이 구성되었습니다.\n")
    ##게임제작에 도움을 주고자 리스트 안에 순서 지정
    for j in range(0, y):
        for i in range(0, h):
            game[j][i] = str(cnt)
            cnt = cnt + 1
    
    #게임판 제작
    for j in range(0, y):
        for i in range(0, h):
            showlistboard(y,game)
            print("\n")
            print("게임판을 완성하세요( 1. 벽, 2. 빈 공간, 3. 검은 구슬, 4. 하얀 구슬, 5. 구멍)")
            print("%s번째 입력 : " %game[j][i], end="")
            pawn = {1 : "■", 2 : "  ", 3 : "●", 4 : "○", 5 : "□"}
            game[j][i] = pawn[int(input())]

    showboard(h,y,game)

    return h,y,game

#임의의 게임판 제작 함수
def makegameboard():

    #게임판 크기 설정
    h = int(input("\n게임판의 가로 크기를 입력해주세요 : "))
    y = int(input("게임판의 세로 크기를 입력해주세요 : "))

    game = [["□"] * h for i in range(y)]    #게임판 2차원 리스트
    cnt = 0
    for j in range(0, y):
        for i in range(0, h):
            game[j][i] = str(cnt)
            cnt = cnt + 1
    
    
    #테두리 벽 세우기
    for j in range(0, y):
        game[j][0] = "■"
    for i in range(0, h):
        game[0][i] = "■"
    for k in range(0, y):
        game[k][h-1] = "■"
    for l in range(0, h):
        game[y-1][l] = "■"
    
    

    #검은 구슬 위치 설정
    while(1):
        check = 0
        marble = random.randrange(0, h*y)
        for j in range(0, y):
            for i in range(0, h):
                if (game[j][i] == str(marble)):
                    game[j][i] = "●"
                    check = 1
                    break
        if (check == 0):
            continue
        else:
            break

    #하얀 구슬 위치 설정
    while(1):
        check = 0
        marble = random.randrange(0, h*y)
        for j in range(0, y):
            for i in range(0, h):
                if (game[j][i] == str(marble)):
                    game[j][i] = "○"
                    check = 1
                    break
        if (check == 0):
            continue
        else:
            break

    #구멍 위치 설정
    while(1):
        check = 0
        marble = random.randrange(0, h*y)
        for j in range(0, y):
            for i in range(0, h):
                if (game[j][i] == str(marble)):
                    game[j][i] = "□"
                    check = 1
                    break
        if (check == 0):
            continue
        else:
            break
        
    #게임판 중간중간 벽 설정
    
    if(h*y <= 49):
        check = 0
    elif(50 <= h*y and h*y <= 81):
        check = 2
    elif(82 <= h*y and h*y <= 100):
        check = 4
    else:
        check = 6

    if(check != 0):
        while(1):
            a = 0
            marble = random.randrange(0, h*y)
            for j in range(0, y):
                for i in range(0, h):
                    if (game[j][i] == str(marble)):
                        game[j][i] = "■"
                        check = check - 1
                        a = 1
                        break
                if (a == 1):
                    break
            if (check == 0):
                break 

    #빈공간 위치 설정
    while(1):
        for j in range(0, y):
            for i in range(0, h):
                if (game[j][i] != "●" and game[j][i] != "○" and game[j][i] != "□" and game[j][i] != "■"):
                    game[j][i] = "  "
        break
    
    return h,y,game


#구슬위치를 찾고 그 위치를 저장하기 위한 함수
def direction(h,y,game):
    check = 0
    for i in range(y):
        for j in range(h):
            if (game[j][i] == "●"):
                hang_b = j
                yeol_b = i
                check = 1
                if(check == 1):
                    break

        if(check == 1):
            break
            
    check = 0
    for i in range(y):
        for j in range(h):
            if (game[j][i] == "○"):
                hang_w = j
                yeol_w = i
                check = 1
                if(check == 1):
                    break

        if(check == 1):
            break
                
    return hang_b,hang_w,yeol_b,yeol_w


#밑
def Down(hang_b, hang_w):
    #구슬이 굴러가기 위한 조건 설정
    if(hang_b>hang_w):
        check = 0
        for i in range(y):
            for j in range(h):
                #이동을 위한 조건
                if (game[j][i] == "●" and game[j+1][i] == "  "):
                    game[j][i] = "  "
                    game[j+1][i] = "●"
                    check = 1
                
                #게임 승리 조건
                elif (game[j][i] == "●" and game[j+1][i] == "□"):
                    game[j][i] = "  "
                    print("\n\n★★★★승리!★★★★")
                    check = 1

                if(check == 1):#코드줄 실행 횟수를 줄이기 위한 코드
                    break

            if(check == 1):#코드줄 실행 횟수를 줄이기 위한 코드
                break
                
        check = 0
        for i in range(y):
            for j in range(h):
                #이동을 위한 조건
                if (game[j][i] == "○" and game[j+1][i] == "  "):
                    game[j][i] = "  "
                    game[j+1][i] = "○"
                    check = 1

                #게임 패배 조건
                elif (game[j][i] == "○" and game[j+1][i] == "□"):
                    game[j][i] = "  "
                    print("\n\n☆☆☆☆패배!☆☆☆☆")
                    check = 1

                if(check == 1):
                    break

            if(check == 1):#코드줄 실행 횟수를 줄이기 위한 코드
                break

    #구슬이 굴러가기 위한 조건 설정
    else:
        check = 0
        for i in range(y):
            for j in range(h):
                #이동을 위한 조건
                if (game[j][i] == "○" and game[j+1][i] == "  "):
                    game[j][i] = "  "
                    game[j+1][i] = "○"
                    check = 1

                #게임 패배 조건
                elif (game[j][i] == "○" and game[j+1][i] == "□"):
                    game[j][i] = "  "
                    print("\n\n☆☆☆☆패배!☆☆☆☆")
                    check = 1

                if(check == 1):#코드줄 실행 횟수를 줄이기 위한 코드
                    break

            if(check == 1):#코드줄 실행 횟수를 줄이기 위한 코드
                break

        check = 0
        for i in range(y):
            for j in range(h):
                #이동을 위한 조건
                if (game[j][i] == "●" and game[j+1][i] == "  "):
                    game[j][i] = "  "
                    game[j+1][i] = "●"
                    check = 1

                #게임 승리 조건
                elif (game[j][i] == "●" and game[j+1][i] == "□"):
                    game[j][i] = "  "
                    print("\n\n★★★★승리!★★★★")
                    check = 1

                if(check == 1):#코드줄 실행 횟수를 줄이기 위한 코드
                    break

            if(check == 1):#코드줄 실행 횟수를 줄이기 위한 코드
                break

#위
def Up(hang_b,hang_w):
    if(hang_b<hang_w):
        check = 0
        for i in range(y):
            for j in range(h):
                if (game[j][i] == "●" and game[j-1][i] == "  "):
                    game[j][i] = "  "
                    game[j-1][i] = "●"
                    check = 1

                elif (game[j][i] == "●" and game[j-1][i] == "□"):
                    game[j][i] = "  "
                    print("\n\n★★★★승리!★★★★")
                    check = 1

                if(check == 1):
                    break

            if(check == 1):
                break

        check = 0
        for i in range(y):
            for j in range(h):            
                if (game[j][i] == "○" and game[j-1][i] == "  "):
                    game[j][i] = "  "
                    game[j-1][i] = "○"
                    check = 1

                elif (game[j][i] == "○" and game[j-1][i] == "□"):
                    game[j][i] = "  "
                    print("\n\n☆☆☆☆패배!☆☆☆☆")
                    check = 1

                if(check == 1):
                    break

            if(check == 1):
                break


    else:
        check = 0
        for i in range(y):
            for j in range(h):
                if (game[j][i] == "○" and game[j-1][i] == "  "):
                    game[j][i] = "  "
                    game[j-1][i] = "○"
                    check = 1

                elif (game[j][i] == "○" and game[j-1][i] == "□"):
                    game[j][i] = "  "
                    print("\n\n☆☆☆☆패배!☆☆☆☆")
                    check = 1

                if(check==1):
                    break

            if(check == 1):
                break

        check = 0       
        for i in range(y):
            for j in range(h):            
                if (game[j][i] == "●" and game[j-1][i] == "  "):
                    game[j][i] = "  "
                    game[j-1][i] = "●"
                    check = 1

                elif (game[j][i] == "●" and game[j-1][i] == "□"):
                    game[j][i] = "  "
                    print("\n\n★★★★승리!★★★★")
                    check = 1

                if(check == 1):
                    break

            if(check == 1):
                break

#오른쪽
def Right(yeol_b, yeol_w):
    if(yeol_b>yeol_w):
        check = 0
        for j in range(h):
            for i in range(y):
                if (game[j][i] == "●" and game[j][i+1] == "  "):
                    game[j][i] = "  "
                    game[j][i+1] = "●"
                    check = 1

                elif (game[j][i] == "●" and game[j][i+1] == "□"):
                    game[j][i] = "  "
                    print("\n\n★★★★승리!★★★★")
                    check = 1

                if(check == 1):
                    break

            if(check == 1):
                break

        check = 0            
        for j in range(h):
            for i in range(y):           
                if (game[j][i] == "○" and game[j][i+1] == "  "):
                    game[j][i] = "  "
                    game[j][i+1] = "○"
                    check = 1

                elif (game[j][i] == "○" and game[j][i+1] == "□"):
                    game[j][i] = "  "
                    print("\n\n☆☆☆☆패배!☆☆☆☆")
                    check = 1

                if(check == 1):
                    break

            if(check == 1):
                break

    else:
        check = 0
        for j in range(h):
            for i in range(y):
                if (game[j][i] == "○" and game[j][i+1] == "  "):
                    game[j][i] = "  "
                    game[j][i+1] = "○"
                    check = 1

                elif (game[j][i] == "○" and game[j][i+1] == "□"):
                    game[j][i] = "  "
                    print("\n\n☆☆☆☆패배!☆☆☆☆")
                    check = 1

                if(check == 1):
                    break

            if(check == 1):
                break

        check = 0
        for j in range(h):
            for i in range(y):            
                if (game[j][i] == "●" and game[j][i+1] == "  "):
                    game[j][i] = "  "
                    game[j][i+1] = "●"
                    check = 1

                elif (game[j][i] == "●" and game[j][i+1] == "□"):
                    game[j][i] = "  "
                    print("\n\n★★★★승리!★★★★") 
                    check = 1

                if(check == 1):
                    break

            if(check == 1):
                break

#왼쪽
def Left(yeol_b, yeol_w):
    if(yeol_b<yeol_w):
        check = 0
        for i in range(y):
            for j in range(h):
                if (game[j][i] == "●" and game[j][i-1] == "  "):
                    game[j][i] = "  "
                    game[j][i-1] = "●"
                    check = 1

                elif (game[j][i] == "●" and game[j][i-1] == "□"):
                    game[j][i] = "  "
                    print("\n\n★★★★승리!★★★★")
                    check = 1

                if(check == 1):
                    break

            if(check == 1):
                break

        check = 0
        for i in range(y):
            for j in range(h):
                if (game[j][i] == "○" and game[j][i-1] == "  "):
                    game[j][i] = "  "
                    game[j][i-1] = "○"
                    check = 1

                elif (game[j][i] == "○" and game[j][i-1] == "□"):
                    game[j][i] = "  "
                    print("\n\n☆☆☆☆패배!☆☆☆☆")
                    check = 1

                if(check == 1):
                    break

            if(check == 1):
                break

    else:
        check = 0
        for i in range(y):
            for j in range(h):
                if (game[j][i] == "○" and game[j][i-1] == "  "):
                    game[j][i] = "  "
                    game[j][i-1] = "○"
                    check = 1

                elif (game[j][i] == "○" and game[j][i-1] == "□"):
                    game[j][i] = "  "
                    print("\n\n☆☆☆☆패배!☆☆☆☆")
                    check = 1
                    
                if(check == 1):
                    break

            if(check == 1):
                break

        check = 0
        for i in range(y):
            for j in range(h):            
                if (game[j][i] == "●" and game[j][i-1] == "  "):
                    game[j][i] = "  "
                    game[j][i-1] = "●"
                    check = 1

                elif (game[j][i] == "●" and game[j][i-1] == "□"):
                    game[j][i] = "  "
                    print("\n\n★★★★승리!★★★★")
                    check = 1
                    
                if(check == 1):
                    break

            if(check == 1):
                break


#방향 입력 받는 함수
def KeyClick(e):
    key=0
    key = e.keycode
        
    if(key == 37):
        Left(yeol_b,yeol_w)
    elif(key == 38):
        Up(hang_b,hang_w)
    elif(key == 40):
        Down(hang_b,hang_w)
    elif(key == 39):
        Right(yeol_b,yeol_w)

    if(bd == 1):
        showboard(h,y,game)
    elif(bd == 2):
        showlistboard(y,game)



#------------------------------------게임 시작--------------------------------------

#게임 설명
print(" ----- 구슬탈출 -----")
print("이 게임은 구슬을 탈출시키는 게임입니다.")
print("이 게임은 빈공간과 4개의 모형이 있습니다.")
print("벽: ■, 색칠한 구슬: ●, 하얀구슬: ○, 구멍: □, 빈 공간  ")
print("벽과 구멍은 움직이는 모형이 아니며, 색칠한 구슬과 하얀구슬만 움직일 수 있습니다.")
print("구슬은 방향키를 눌러 구슬을 상하좌우로 움직일 수 있습니다.")
print("구슬이 이동하고자 하는 방향에  벽이 있으면 더 이상 움직이지 못합니다.")
print("색칠한 구슬을 구멍에 먼저 넣으면 성공! 하얀구슬 실패! 입니다.")

#게임 보드 출력 형태 선택
while(1):
    print("\n게임보드 출력을 게임 형태만 보이고자 하면 1")
    print("게임보드 출력을 리스트 형태로 보이고자 하면 2")
    bd = int(input("숫자를 입력하세요: "))
    if(bd == 1):
        break
    elif(bd == 2):
        break
    else:
        print("잘못입력하셨습니다. 다시 입력해주세요.")

#게임 선택
while(1):
    print("\n사용자 제작 게임을 실행하고자 하면 1")
    print("임의로 만들어질 게임을 실행하고자 하면 2")
    ch = int(input("1 또는 2를 입력하세요: "))
    if(ch == 1):
        break
    elif(ch == 2):
        break
    else:
        print("잘못입력하셨습니다. 다시 입력해주세요.")

#사용자 제작 게임 실행
if(ch == 1):
    h,y,game = domakegameboard()
#임의로 만들어진 게임 실행
elif(ch == 2):
    h,y,game = makegameboard()

if(bd == 1):
    showboard(h,y,game)
elif(bd == 2):
    showlistboard(y,game)

hang_b,hang_w,yeol_b,yeol_w = direction(h,y,game)

root = tkinter.Tk() # tk모듈객체 root생성
root.title("키 입력") # 키 입력 창 이름
root.bind("<Key>", KeyClick) # 키 입력할 때 키값을 KeyClick함수의 매개변수로 전
root.mainloop() # tkinter 모듈이 실행되게 함
