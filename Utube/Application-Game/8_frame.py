import pygame
##########################################
#기본 초기화 (반드시 해야하는 것들)
pygame.init()   #초기화

#화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("Injun Game") #게임이름

# FPS
clock = pygame.time.Clock()
###########################################

#1. 사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, 속도, 폰트 등 )


#이벤트 루프
running = True
while running:
    dt = clock.tick(30) #게임화면의 초당 프레임수를 설정

    #케릭터가 100만큼 이동을 해야함
    #10 fps: 1초동안에 10번 동작 -> 1번에 몇 만큼 이동? 10만큼! 10*10 = 100
    #20 fps: 1초 동안에 20번 동

    #2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #창이 닫히는 이벤트 발생
            running = False


    #3. 게임 케릭터 위치 정의

    #4. 충돌 처리

    #5. 화면에 그리기
    pygame.display.update() #게임 화면을 계속 다시 그리기


#pygame 종료
pygame.quit()
