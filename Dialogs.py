import time
def program_info():
    date = '2017년 9월 24일'
    ver = '첫 번째'
    desc = '이 프로그램은 대화형 일기장입니다. 대화를 주도해 보세요.'
    return(print('\n:: 프로그램 정보 ::\n* 아키텍처는 %s에 개발된 %r 버전입니다.\n* %r' % (date,ver,desc)))

# 변수 초기화
dates = []

# Story 내용
dates.append("170924")
m170924_1 = ['오늘.. 9월 24일 일요일 날씨는 맑았어.','오늘은 Dialogs 프로그램을 처음 개발하기 시작한 날이야.','이 프로그램은 대화형 게임인 Lifeline에서 영감을 얻었지.']
q170924_1 = ['그게 뭔데?','어? 나 그 게임 해봤어']
m170924_2 = ['그거 인디게임인데 정말 잼있어. 한번 해보길 추천할게.','오 정말? 나와 동지를 만났군.']

i = 1
while True:
    print("\n"+"-"*20)
    print("| 대화형 일기장입니다.\n| '안녕'을 쳐서 대화를 시작하세요.\n| '정보'를 치면 버전정보가 나옵니다.")
    print("-"*20+"\n")
    time.sleep(1)
    nb = input('dialog #%i: '%i)
    if nb=='정보': program_info()
    elif nb=='안녕':
        print('\n- 내 기억에 온걸 환영해. 어떤 얘길 들려줄까?\n')
        time.sleep(0.5)
        print("********목록********\n* 현재 %i개의 기억이 저장되어 있습니다.\n* 그 목록은 아래와 같습니다." % len(dates))
        print("*"*20)
        time.sleep(0.5)
        print(dates)
        print("\n"+"-"*20)
        time.sleep(0.5)
        nb = input('dialog #%i: '%i)

    # story start
    elif nb=='170924':
        print("")
        for item in m170924_1:
            print("-",item)
            time.sleep(1)
        print("")
        j = 1
        for item in q170924_1:
            print("[%i] %s" % (j,item))
            j+=1
        time.sleep(0.5)
        nb = input('\n번호입력: ')
        print("-"*20)
        if nb=='1':
            time.sleep(1)
            print("-",m170924_2[0])
        elif nb=='2':
            time.sleep(1)
            print('-',m170924_2[1])
        elif nb=='그만':
            print('\n*** 일기장 접속을 종료합니다 ***\n')
            break
        time.sleep(1)
        print('\n- 이 날 이야기는 여기까지야.')
    # story end

    elif nb=='그만':
        print('\n*** 일기장 접속을 종료합니다 ***\n')
        break
    else:
        print("\n'안녕'이라고 쳐보세요.\n이 일기장의 정보는 '정보'를 치면 나옵니다.\n")
    i+=1
