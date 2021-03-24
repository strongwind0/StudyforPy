import turtle as tt


tt.setup(600, 500)
tt.penup()  # 抬起画笔，无痕迹
tt.fd(-250)  # 前行(bk后行) forward()
tt.pendown()  # 放下画笔
tt.pensize(25)  # 线条粗细
tt.pencolor('cyan')  # 线条颜色
tt.seth(-40)  # 改变方向，setheading 绝对角度
# left,right 改变方向（相对目标），旋转角度
for i in range(2):
    tt.circle(40, 80)  # 转圈 第一个参数是半径，第二个参数是角度，原点默认在左侧
    tt.circle(-40, 80)
tt.circle(40, 80/2)
tt.fd(40)
tt.circle(16, 180)
tt.fd(40 * 2/3)
tt.done()
