# # game부터 시작하면 절대 경로 지정
# import game.sound.echo

# print(echo.echo_test())



# 터미널에서 set 메소드  : 1회성 (닫고 열면 다시 set해줘야됨)
# 터미널 3가지 방법(연습)
# from은 module 까지만 가능 뒤에 변수 function class 다안됨

# import module 까지만 가능
# from game.sound.echo import echo_test 함수는 이렇게 해야됨

from game.graphic.render import render_test

render_test()