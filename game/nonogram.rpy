image background = "images/nonogram1.png"

init python:
    grid_size = 10  # 10x10 그리드
    solution = [  # 정답 배열 (1 = 채워짐, 0 = 비어 있음)
        [1, 0, 1, 1, 0, 0, 0, 1, 0, 1],
        [0, 1, 0, 1, 1, 0, 1, 1, 0, 0],
        [1, 1, 0, 0, 1, 1, 0, 0, 1, 1],
        [0, 0, 1, 1, 0, 0, 1, 1, 0, 0],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        [1, 1, 0, 0, 1, 1, 0, 0, 1, 1],
        [0, 0, 1, 1, 0, 0, 1, 1, 0, 0],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    ]

    # 플레이어의 현재 그리드 상태 (0 = 빈 칸, 1 = 채운 칸)
    player_grid = [
        [0] * grid_size for _ in range(grid_size)
    ]

    game_active = True  # 게임 진행 여부
    message = ""  # 게임 상태 메시지
    # 메시지 표시

    def check_solution():
        """플레이어가 정답을 맞췄는지 확인"""
        global game_active, message
        if player_grid == solution:
            message = "축하합니다! 퍼즐을 완성했습니다!"
            game_active = False
            return
        else:
            message = ""

    def toggle_cell(x, y):
        """플레이어가 셀을 클릭했을 때 상태 변경"""
        if game_active:
            # renpy.sound.play("audio/chimhaha.mp3")
            player_grid[y][x] = 1 if player_grid[y][x] == 0 else 0
            check_solution()

# 배경 이미지 추가 (힌트 포함된 이미지)

screen nonogram_game:

    add "background"

    frame:
        align (0.545, 0.5)
        has vbox
        if game_active:
                # 그리드 표시
            for y in range(grid_size):
                hbox:
                    for x in range(grid_size):
                        if player_grid[y][x] == 1:
                            textbutton " ":
                                style "nonogram_button_filled"
                                action Function(toggle_cell, x, y)
                        else:
                            textbutton " ":
                                style "nonogram_button_empty"
                                action Function(toggle_cell, x, y)

            # 메시지 표시
            if message:
                text message size 15 align (0.5, .1)
                
        else:

            # 게임이 끝난 후 재시작 버튼을 새로운 레이어로 추가
            if not game_active:
                # 레이어를 추가하여 그리드 위에 버튼 표시
                frame:
                    align (0.5, 0.5)  # 중앙에 배치
                    style "restart_button_style"
                    textbutton "얏호!!" action Return()

# 버튼 스타일 정의
style nonogram_button_empty is default:
    xsize 40
    ysize 40
    background "#ffffff"  # 빈 셀 색상
    hover_background "#aaaaaa"
    insensitive_background "#888888"

style nonogram_button_filled is default:
    xsize 40
    ysize 40
    background "#000000"  # 채운 셀 색상 (검정색)
    hover_background "#555555"
    insensitive_background "#888888"

# 재시작 버튼 스타일 정의 (이 부분을 추가해야 합니다.)
style restart_button_style is default:
    size 80
    background "#000000"  # 배경색 (녹색)
    hover_background "#5a5a5a"  # 호버 색상
    
