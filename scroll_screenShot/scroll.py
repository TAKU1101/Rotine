from screeninfo import get_monitors
from PIL import ImageGrab
import time
import pyautogui

# full screen

print(*[str(i) + "\n" for i in range(100)], end="")

print("表示されている一番上の数字: ", end="")

size = input()

try:
    size = int(size)
except:
    print("ERROR")
    exit(1)

print("スクリーンショットをするデータの行数: ", end="")

data_size = input()

try:
    data_size = int(data_size)
except:
    print("ERROR")
    exit(1)

for i in range(10, 0, -1):
    print(i, "秒後に処理が始まります。スクリーンショットを行いたいウィンドウに変更しマウスとキーボードから手を話してください。")
    time.sleep(1)

ImageGrab.grab().save("PIL_capture_{}.png".format(0))
time.sleep(0.1)

for i in range(1, (data_size // size) + 1):
    for _ in range(100 - size):
        pyautogui.press("enter")
    ImageGrab.grab().save("PIL_capture_{}.png".format(i))
    time.sleep(0.1)

ImageGrab.grab().save("PIL_capture.png")
m = get_monitors()

# print(m[0].width)