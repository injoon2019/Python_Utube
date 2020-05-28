import pygame

pygame.init()   #초기화

#화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("Injun Game") #게임이름

#배경 이미지 불러오기
background = pygame.image.load("C:\\Users\\injoo\\Desktop\\Python\\Utube\\Application-Game\\background.png")

#캐릭터(스프라이트) 불러오기
character = pygame.image.load("C:\\Users\\injoo\\Desktop\\Python\\Utube\\Application-Game\\character.png")
character_size = character.get_rect().size      #이미지의 크기 구하기
character_width = character_size[0]         #캐릭터의 가로 크기
character_height = character_size[1]        #캐릭터의 세로 크기
character_x_pos = (screen_width)/2 - (character_width/2)       #화면 가로의 절반에 해당하는 곳에 위치
character_y_pos = screen_height - character_height   #화면 세로 크기 가장 아래


#이동할 좌표
to_x = 0
to_y = 0

#이벤트 루프
running = True #게임이 진행중인가?
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #창이 닫히는 이벤트 발생
            running = False

        if event.type == pygame.KEYDOWN: #키가 눌러졌는지 확인
                if event.key == pygame.K_LEFT:  #케릭터를 왼쪽으로
                    to_x -= 5
                elif event.key == pygame.K_RIGHT: #케릭터를 오른쪽으로
                    to_x += 5
                elif event.key == pygame.K_UP: #케릭터를 위로
                    to_y -=5
                elif event.key == pygame.K_DOWN: #케릭터를 아래로
                    to_y +=5

        if event.type == pygame.KEYUP: #방향키에서 손을 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key== pygame.K_RIGHT:
                to_x =0
            elif event.key ==pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x
    character_y_pos += to_y

    #캐릭터가 화면 밖에 나가지 않게 가로경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    #캐릭터가 화면 밖에 나가지 않게 세로경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_width:
        character_y_pos = screen_height -character_width

    screen.blit(background, (0,0)) #배경 그리기

    screen.blit(character, (character_x_pos, character_y_pos)) #캐릭터 그리기
    pygame.display.update() #게임 화면을 계속 다시 그리기

#pygame 종료
pygame.quit()
