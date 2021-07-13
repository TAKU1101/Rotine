from PIL import ImageGrab
import time
import pyautogui

def my_screen_shot(i):
    ImageGrab.grab().save("auto_SS{}.png".format(i))
    time.sleep(0.1)

def int_input(msg):
    print(msg, end="")
    n = input()
    try:
        n = int(n)
    except:
        print("ERROR")
        exit(1)
    return n

def data_input():
    print(*[str(i) + "\n" for i in range(100)], end="")
    size = int_input("表示されている一番上の数字: ")
    data_size = int_input("スクリーンショットをするデータの行数: ")
    return size, data_size

def before():
    for i in range(10, 0, -1):
        print(i, "秒後に処理が始まります。スクリーンショットを行いたいウィンドウに変更しマウスとキーボードから手を話してください。")
        time.sleep(1)

def routine(size, data_size):
    my_screen_shot(0)
    for i in range(1, (data_size // size) + 1):
        for _ in range(100 - size):
            pyautogui.press("enter")
        my_screen_shot(i)

if __name__ == '__main__':
    size, data_size = data_input()
    before()
    routine(size, data_size)