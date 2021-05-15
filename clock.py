# 第1步：導入模塊
import arcade  # 必須的
import math, time

# 第2步：常量初始化定義
# 屏幕的寬和高
WIDTH = 1000
HEIGHT = 800
# 中心座標點
X0 = WIDTH / 2
Y0 = HEIGHT / 2
# 圓盤的半徑
R_circle = 250


# 第3步：定義函數
# 時鐘的小時刻度文字函數
def hours_text():
    for i in range(1, 13):
        x = X0 + (R_circle - 30) * math.sin(2 * math.pi * i / 12)
        y = Y0 + (R_circle - 30) * math.cos(2 * math.pi * i / 12)
        # 在座標點上顯示小時1~12的文字，顏色，字體大小
        arcade.draw_text(f"{i}", x, y, arcade.color.RED, 20)  # 文字輸出的特色函數


# 畫直線函數
def draw_lines(radius, line_width, rad, color):
    x = X0 - radius * math.cos(math.pi / 2 + rad)
    y = Y0 + radius * math.sin(math.pi / 2 + rad)
    # 畫線函數
    line = arcade.draw_line(X0, Y0, x, y, color, line_width)  # 畫直線的特色函數

    return line


# 總的繪畫函數，必須函數
def on_draw(delta_time):
    arcade.start_render()  # 必須
    # 外圓，圓心座標，圓盤半徑，顏色，寬度
    arcade.draw_circle_outline(X0, Y0, R_circle, arcade.color.BABY_BLUE, 1)  # 畫圓的特色函數
    # 數字小時顯示
    hours_text()
    # 獲取當前時間
    tm = time.localtime()
    # 注意X必須大寫，y、m和d大小寫都可以
    cur_time2 = time.strftime('%y-%m-%d %X', time.localtime())
    t_hour = 0
    if tm.tm_hour <= 12:
        t_hour = tm.tm_hour
    else:
        t_hour = tm.tm_hour - 12

    # 時針
    rad1 = 2 * math.pi * (t_hour + tm.tm_min / 60) / 12
    # 分針
    rad2 = 2 * math.pi * (tm.tm_min + tm.tm_sec / 60) / 60
    # 秒針
    rad3 = 2 * math.pi * tm.tm_sec / 60

    # 畫時針
    draw_lines(100, 6, rad1, color=arcade.color.WHITE)
    # 畫分針
    draw_lines(140, 3, rad2, color=arcade.color.GREEN)
    # 畫秒針
    draw_lines(180, 1, rad3, color=arcade.color.YELLOW)
    # 顯示當前時間
    arcade.draw_text(f"{cur_time2}", X0 - 70, 20, arcade.color.GO_GREEN, 20)  # 文字輸出的特色函數


# 第4步：定義主函數
def main():
    # ===必須===
    # 窗口大小和標題名設置
    arcade.open_window(WIDTH, HEIGHT, "Arcade Clock")
    # 窗口背景顏色設置
    arcade.set_background_color(arcade.color.BLACK)
    arcade.schedule(on_draw, 1)
    arcade.run()
    arcade.close_window()
    # ===必須===


# 第5步：調用主函數
if __name__ == '__main__':
    main()