import os
import PySimpleGUIQt as sg
from PIL import Image


# GUIのレイアウト
layout = [
    # 上部のフレーム
    [sg.Frame(title="ファイルパスを入力してください",
              layout=[
                  [sg.Multiline(key="-file_path-", enable_events=True),
                   sg.FileBrowse("開く", key="-browse-")],
                  [sg.Text("保存場所を選択"),
                   sg.Input(key="-save_path-"),
                   sg.FolderBrowse("開く", key="-folder_browse-")]
              ])],
    # 中央のフレーム
    [sg.Frame(title="変換するファイル形式を選択してください",
                layout=[
                    [sg.Radio("JPEG", "RADIO1", default=True, key="-JPEG-"),
                    sg.Radio("PNG", "RADIO1", key="-PNG-"),
                    sg.Radio("GIF", "RADIO1", key="-GIF-"),
                    sg.Radio("WEBP", "RADIO1", key="-WEBP-")]
                ])],
    # 下部のフレーム
    [sg.Frame(title="",
              layout=[
                  [sg.Button("変換", key="-convert-")]
              ])]
]

# ウィンドウを作成
window = sg.Window("Image Converter", layout, size=(500, 200))

# イベントループ
while True:
    event, values = window.read()  # イベントを取得

    # ウィンドウを閉じたら終了
    if event == sg.WINDOW_CLOSED:
        break

    # ファイルを選択したら、テキストボックスにパスを表示
    if event == "-browse-":
        window["-file_path-"].update(value=values["-browse-"])

    # 変換ボタンが押されたら
    if event == "-convert-":
        pass

        # ラジオボタンから変換するファイル形式を取得
        if values["-JPEG-"]:
            format = "JPEG"
        elif values["-PNG-"]:
            format = "PNG"
        elif values["-GIF-"]:
            format = "GIF"
        elif values["-WEBP-"]:
            format = "WEBP"

window.close()