import os
import PySimpleGUIQt as sg
from PIL import Image

# ファイルを変換する関数
def convert_files(files, format,save_path):
    #　入力されたファイルをforで回して処理
    for file_p in files:
        # 画像ファイルを開いて、指定されたフォーマットで保存する
        
        file_p = file_p.removeprefix(r"file:///")
        print(os.path.abspath(repr(file_p)))
        
        with Image.open(os.path.abspath(file_p)) as im:
            # 画像のファイルネームを取得
            file_p = os.path.splitext(os.path.basename(file_p))[0]
            # 画像を保存する
            im.save(os.path.abspath(os.path.join(save_path,f"{file_p}.{format.lower()}")), format=format,save_all=True)
            sg.popup(f"{file_p} を {format} 形式に変換し、{save_path} に保存しました。")

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

def main():
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
            # ファイルパスを取得
            file_path = values["-file_path-"]
            # 改行でファイルパスを分けてリストで格納
            file_path = file_path.splitlines()
            
            # 保存場所を取得
            save_path = values["-save_path-"]
            format = ""  # 変換するファイル形式を格納する変数

            # ラジオボタンから変換するファイル形式を取得
            if values["-JPEG-"]:
                format = "JPEG"
            elif values["-PNG-"]:
                format = "PNG"
            elif values["-GIF-"]:
                format = "GIF"
            elif values["-WEBP-"]:
                format = "WEBP"
            
            if file_path and format:  # ファイルパスとファイル形式が指定されている場合
                try:
                    convert_files(file_path,format,save_path)
                except:
                    sg.popup("変換に失敗しました。")

    window.close()

if __name__ == "__main__":
    # main実行
    main()