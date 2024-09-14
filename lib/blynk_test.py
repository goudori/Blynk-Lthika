from machine import Pin  # type: ignore
import time
import network  # type: ignore
import sys
import BlynkLib  # type: ignore


# Wi-Fi接続の設定関数
def wifi_connect(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)

    timeout = 20  # タイムアウト秒数を20秒に延長
    # Wi-Fi接続完了まで待機
    while not wlan.isconnected() and timeout > 0:
        print("Wi-Fi接続中...")
        time.sleep(1)
        timeout -= 1
    # Wi-Fi接続実行
    if wlan.isconnected():
        print("Wi-Fi接続成功!")
        print(wlan.ifconfig())
    # Wi-Fi接続失敗時はステータスコードを表示
    else:
        print("Wi-Fi接続失敗: タイムアウト")
        print("ステータスコード:", wlan.status())  # ステータスコードを表示


# Wi-Fi接続情報
ssid = "SSID"  # Wi-FiのSSID
password = "PassWord"  # Wi-Fiのパスワード

# Wi-Fi接続実行
wifi_connect(ssid, password)

# Wi-Fi接続が成功しているか確認
wlan = network.WLAN(network.STA_IF)
if wlan.isconnected():
    print("Wi-Fi接続成功!")
    print(wlan.ifconfig())
else:
    print("Wi-Fi接続失敗: タイムアウト")
    print("ステータスコード:", wlan.status())  # ステータスコードを表示

# Blynkトークン取得
BLYNK_AUTH = "BLYNK TOKEN"

# Blynkインスタンス作成
blynk = BlynkLib.Blynk(BLYNK_AUTH)

# LED Pin設定
led = Pin("LED", Pin.OUT)


# Blynkの仮想Pin V1からデータを受け取った時の処理
@blynk.on("V1")
def v1_write_handler(value):
    print(value[0])
    if int(value[0]) == 1:
        led.on()
    else:
        led.off()


# Blynkと連携を維持するための無限ループ
while True:
    blynk.run()
