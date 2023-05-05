import os
import PySimpleGUIQt as sg
from PIL import Image

class ImageManager:
    """画像を操作するクラス"""
    #　コンストラクタ　初期値を""に設定
    def __init__(self,file_path="",save_path=""):
        self.file_path = file_path
        self.save_path = save_path
    # ファイルを変換する関数
    def convert_files(self,files, format,save_path):
        #　入力されたファイルをforで回して処理
        for file_p in files:
            # 画像ファイルを開いて、指定されたフォーマットで保存する
            
            file_p = file_p.removeprefix(r"file:///")
            print(os.path.abspath(repr(file_p)))
            
            with Image.open(os.path.abspath(file_p)) as im:
                if format == "JPEG":
                    # JPEGの場合は開き直してRGB形式に変換
                    im = Image.open(os.path.abspath(file_p)).convert("RGB")
                # 画像のファイルネームを取得
                file_p = os.path.splitext(os.path.basename(file_p))[0]
                # 画像を保存する
                im.save(os.path.abspath(os.path.join(save_path,f"{file_p}.{format.lower()}")), format=format,save_all=True)
                sg.popup(f"{file_p} を {format} 形式に変換し、{save_path} に保存しました。")

class GUIView:
    """GUIに関係するクラス"""
    def __init__(self):
        # GUIのレイアウト
        self.layout = [
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
        self.window = sg.Window("Image Converter", self.layout, size=(500, 200))

    def main(self):    
        # イベントループ
        while True:
            event, values = self.window.read()  # イベントを取得

            # ウィンドウを閉じたら終了
            if event == sg.WINDOW_CLOSED:
                break

            # ファイルを選択したら、テキストボックスにパスを表示
            if event == "-browse-":
                self.window["-file_path-"].update(value=values["-browse-"])

            # 変換ボタンが押されたら
            if event == "-convert-":
                # ファイルパスを取得
                image_manager.file_path = values["-file_path-"]
                # 改行でファイルパスを分けてリストで格納
                image_manager.file_path = image_manager.file_path.splitlines()
                
                # 保存場所を取得
                image_manager.save_path = values["-save_path-"]
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

                if image_manager.file_path and format:  # ファイルパスとファイル形式が指定されている場合
                    try:
                        image_manager.convert_files(image_manager.file_path,format,image_manager.save_path)
                    except:
                        sg.popup("変換に失敗しました。")
        self.window.close()

if __name__ == "__main__":
    # イメージ処理用のクラスをインスタンス化
    image_manager = ImageManager()
    # GUIをインスタンス化
    image_converter = GUIView()
    # main実行
    image_converter.main()