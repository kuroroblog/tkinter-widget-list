import tkinter as tk
from tkinter import scrolledtext
from tkinter import ttk

class Application(tk.Frame):
    # scrolledtext Widgetを取得する関数
    def getScrolledText(self):
        # Windowを親要素として、frame Widget(Frame)を作成する。
        # Frameについて : https://kuroro.blog/python/P20XOidA5nh583fYRvxf/
        frame = tk.Frame(self.master)
        # Windowを親要素として、frame Widget(Frame)をどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        frame.pack()

        # frame Widget(Frame)を親要素として、scrolledtext Widgetを作成する。
        # ScrolledTextについて : https://kuroro.blog/python/r3HUUg7yh60zwYuwnmm2/
        scrolledText = scrolledtext.ScrolledText(frame)

        # frame Widget(Frame)を親要素とした場合に、scrolledtext Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        scrolledText.pack()

    # combobox Widgetを取得する関数
    def getCombobox(self):
        # Windowを親要素として、frame Widget(Frame)を作成する。
        # Frameについて : https://kuroro.blog/python/P20XOidA5nh583fYRvxf/
        frame = tk.Frame(self.master)
        # Windowを親要素として、frame Widget(Frame)をどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        frame.pack()

        # frame Widget(Frame)を親要素として、combobox Widgetを作成する。
        # values : comboboxを選択すると、表示される様々な選択肢(バイキンマン, 食パンまんとする)の設定
        # Comboboxについて : https://kuroro.blog/python/3ZzPkezBOeTN7lletMyG/
        combobox = ttk.Combobox(frame, values=('バイキンマン', '食パンまん'))

        # frame Widget(Frame)を親要素とした場合に、combobox Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        combobox.pack()

    # optionmenu Widgetを取得する関数
    def getOptionMenu(self):
        # Windowを親要素として、frame Widget(Frame)を作成する。
        # Frameについて : https://kuroro.blog/python/P20XOidA5nh583fYRvxf/
        frame = tk.Frame(self.master)
        # Windowを親要素として、frame Widget(Frame)をどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        frame.pack()

        # 現在選択されているoptionmenu Widget内の選択肢の値を、文字列変数として扱う。
        # StringVarについて : https://kuroro.blog/python/K53voPjJuKFfYrjmP8FP/
        var = tk.StringVar()
        # set() : 初期値としてaaaの選択肢を設定する。
        var.set('aaa')

        # frame Widget(Frame)を親要素として、optionmenu Widgetを作成する。
        # var : 現在選択されている選択肢の値。文字列変数(var)として値を持たせることで、可変として扱う。
        # 'aaa', 'bbb' : 選択肢1, 選択肢2
        # OptionMenuについて : https://kuroro.blog/python/LA789mm56rcPTvU3gfdW/
        optionmenu = tk.OptionMenu(frame, var, 'aaa', 'bbb')

        # frame Widget(Frame)を親要素とした場合に、optionmenu Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        optionmenu.pack()

    # canvas Widgetを取得する関数
    def getCanvas(self):
        # Windowを親要素として、frame Widget(Frame)を作成する。
        # Frameについて : https://kuroro.blog/python/P20XOidA5nh583fYRvxf/
        frame = tk.Frame(self.master)
        # Windowを親要素として、frame Widget(Frame)をどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        frame.pack()

        # frame Widget(Frame)を親要素として、canvas Widgetを作成する。
        # width : 幅の設定
        # height : 高さの設定
        # background : 背景色の設定
        # 色について : https://kuroro.blog/python/YcZ6Yh4PswqUzaQXwnG2/
        # Canvasについて : https://kuroro.blog/python/V63iINoXI8iwMeRMEJPK/
        canvas = tk.Canvas(frame, width=250, height=500, background="white")

        # canvas Widgetへ線を描画する。
        # x1座標 : 200, y1座標 : 200, x2座標 : 10, y2座標 : 20, x3座標 : 60, y3座標 : 100, x4座標 : 40, y4座標 : 30
        # fill : 線の色を設定
        # Canvasについて : https://kuroro.blog/python/ANyM9WLpd0LSXRQAELOj/
        canvas.create_line(200, 200, 10, 20, 60, 100, 40, 30, fill='black')

        # frame Widget(Frame)を親要素とした場合に、canvas Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        canvas.pack()

    # scrollbar Widgetを取得する関数
    def getScrollBar(self):
        # Windowを親要素として、frame Widget(Frame)を作成する。
        # Frameについて : https://kuroro.blog/python/P20XOidA5nh583fYRvxf/
        frame = tk.Frame(self.master)
        # Windowを親要素として、frame Widget(Frame)をどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        frame.pack()

        # frame Widget(Frame)を親要素として、text Widgetを作成する。
        # height : 高さを設定
        # Textについて : https://kuroro.blog/python/bK6fWsP9LMqmER1CBz9E/
        text = tk.Text(frame, height=4)

        # frame Widget(Frame)を親要素として、scrollbar Widgetを作成する。
        # orient option : 垂直scrollbarを作成するため、tk.VERTICALを設定。水平scrollbarの場合は、tk.HORIZONTALを設定する。
        # command option : scrollbar Widgetを動かした場合に、連動して表示する内容を設定。今回は、text Widgetをy軸方向へ動かした内容を表示する。
        # Scrollbarについて : https://kuroro.blog/python/vgx53M7D1d6C0R8ejp0V/
        scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=text.yview)

        # scrollbar Widgetをtext Widgetに反映する
        # scrollbar Widgetの設定内容をtext Widgetと紐付ける。
        # yscrollcommand : text Widget内で上下移動した場合に、scrollbarが追従するように設定する。
        text["yscrollcommand"] = scrollbar.set

        # frame Widget(Frame)を親要素とした場合に、text Widgetをどのように配置するのか?
        # gridについて : https://kuroro.blog/python/JoaowDiUdLAOj3cSBxiX/
        text.grid(row=0, column=0)
        # frame Widget(Frame)を親要素とした場合に、scrollbar Widgetをどのように配置するのか?
        # gridについて : https://kuroro.blog/python/JoaowDiUdLAOj3cSBxiX/
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))

    # text Widgetを取得する関数
    def getText(self):
        # Windowを親要素として、frame Widget(Frame)を作成する。
        # Frameについて : https://kuroro.blog/python/P20XOidA5nh583fYRvxf/
        frame = tk.Frame(self.master)
        # Windowを親要素として、frame Widget(Frame)をどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        frame.pack()

        # frame Widget(Frame)を親要素として、text Widgetを作成する。
        # Textについて : https://kuroro.blog/python/bK6fWsP9LMqmER1CBz9E/
        text = tk.Text(frame)
        # frame Widget(Frame)を親要素として、text Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        text.pack()

    # entry Widgetを取得する関数
    def getEntry(self):
        # Windowを親要素として、frame Widget(Frame)を作成する。
        # Frameについて : https://kuroro.blog/python/P20XOidA5nh583fYRvxf/
        frame = tk.Frame(self.master)
        # Windowを親要素として、frame Widget(Frame)をどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        frame.pack()

        # frame Widget(Frame)を親要素として、entry Widgetを作成する。
        # Entryについて : https://kuroro.blog/python/PUZp77YFxrXvMCjpZbUg/
        entry = tk.Entry(frame)
        # frame Widget(Frame)を親要素として、entry Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        entry.pack()

    # listbox Widgetを取得する関数
    def getListbox(self):
        # Windowを親要素として、frame Widget(Frame)を作成する。
        # Frameについて : https://kuroro.blog/python/P20XOidA5nh583fYRvxf/
        frame = tk.Frame(self.master)
        # Windowを親要素として、frame Widget(Frame)をどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        frame.pack()

        # frame Widget(Frame)を親要素として、listbox Widgetを作成する。
        # Listboxについて : https://kuroro.blog/python/XMWVRR2MEZAe4bpPDDXE/
        listbox = tk.Listbox(frame)
        for month in ("1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月"):
            # listboxへ選択肢を格納する。
            # insert : listbox内の指定箇所(index(位置番号))へ、選択肢を格納する。
            # tk.END : 末尾を表す。
            listbox.insert(tk.END, month)
        # frame Widget(Frame)を親要素として、listbox Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        listbox.pack()

    # spinbox Widgetを取得する関数
    def getSpinbox(self):
        # Windowを親要素として、frame Widget(Frame)を作成する。
        # Frameについて : https://kuroro.blog/python/P20XOidA5nh583fYRvxf/
        frame = tk.Frame(self.master)
        # Windowを親要素として、frame Widget(Frame)をどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        frame.pack()

        # frame Widget(Frame)を親要素として、spinbox Widgetを作成する。
        # Spinboxについて : https://kuroro.blog/python/CQZWZZXhhyD3B1TWP3FN/
        spinbox = tk.Spinbox(frame)
        # frame Widget(Frame)を親要素として、spinbox Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        spinbox.pack()

    # scale Widgetを取得する関数
    def getScale(self):
        # Windowを親要素として、frame Widget(Frame)を作成する。
        # Frameについて : https://kuroro.blog/python/P20XOidA5nh583fYRvxf/
        frame = tk.Frame(self.master)
        # Windowを親要素として、frame Widget(Frame)をどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        frame.pack()

        # frame Widget(Frame)を親要素として、scale Widgetを作成する。
        # Scaleについて : https://kuroro.blog/python/DUvG7YaE2i6jLwCxdPXJ/
        scale = tk.Scale(frame)
        # frame Widget(Frame)を親要素として、scale Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        scale.pack()

    # menubutton Widgetを取得する関数
    def getMenubutton(self):
        # Windowを親要素として、frame Widget(Frame)を作成する。
        # Frameについて : https://kuroro.blog/python/P20XOidA5nh583fYRvxf/
        frame = tk.Frame(self.master)
        # Windowを親要素として、frame Widget(Frame)をどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        frame.pack()

        # frame Widget(Frame)を親要素として、menubutton Widgetを作成する。
        # text : テキスト情報
        # Menubuttonについて : https://kuroro.blog/python/Dfq4VCJ7OiEfYJv6ySge/
        menubutton = tk.Menubutton(frame, text="test")
        # frame Widget(Frame)を親要素として、menubutton Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        menubutton.pack()

    # menu Widgetを取得する関数
    def getMenu(self):
        # menubarを作成して、menubarをWindow内のmenubarとする。
        # Menuを作成する。menuBarとする。
        # Menuについて : https://kuroro.blog/python/ZITZ7dM4nundAhMbChXs/
        menuBar = tk.Menu()
        # Window内のmenubarを、先ほど作成したmenuBarとする。
        self.master.config(menu=menuBar)

        # サブメニューを作成する。
        # サブメニューとは? : https://kotobank.jp/word/%E3%82%B5%E3%83%96%E3%83%A1%E3%83%8B%E3%83%A5%E3%83%BC-3747#:~:text=%E9%9A%8E%E5%B1%A4%E7%9A%84%E3%81%AB%E8%A1%A8%E7%A4%BA%E3%81%95%E3%82%8C,%E3%82%B3%E3%83%9E%E3%83%B3%E3%83%89%E6%93%8D%E4%BD%9C%E3%81%A7%E8%A1%A8%E7%A4%BA%E3%81%A7%E3%81%8D%E3%82%8B%E3%80%82
        # Menuを作成する。fileMenuとする。
        # Menuについて : https://kuroro.blog/python/ZITZ7dM4nundAhMbChXs/
        fileMenu = tk.Menu()
        # label : サブメニュー名の設定
        fileMenu.add_command(label="Exit")

        # menubarへ、Fileと名付けられたメインメニューを追加する。そしてFileと名付けられたメインメニュー内に、サブメニューを追加する。
        # メインメニューとは? : https://kotobank.jp/word/%E3%83%A1%E3%82%A4%E3%83%B3%E3%83%A1%E3%83%8B%E3%83%A5%E3%83%BC-9213
        # label : メインメニュー名の設定
        # menu : メインメニュー内に含む、サブメニューを設定
        menuBar.add_cascade(label="File", menu=fileMenu)

    # radiobutton Widgetを取得する関数
    def getRadiobutton(self):
        # Windowを親要素として、frame Widget(Frame)を作成する。
        # Frameについて : https://kuroro.blog/python/P20XOidA5nh583fYRvxf/
        frame = tk.Frame(self.master)
        # Windowを親要素として、frame Widget(Frame)をどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        frame.pack()

        # frame Widget(Frame)を親要素として、radiobutton Widgetを作成する。
        # text : テキスト情報
        # Radiobuttonについて : https://kuroro.blog/python/ztJbt5uabbTBMCGcljHc/
        radiobutton = tk.Radiobutton(frame, text="test")
        # frame Widget(Frame)を親要素として、radiobutton Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        radiobutton.pack()

    # checkbutton Widgetを取得する関数
    def getCheckbutton(self):
        # Windowを親要素として、frame Widget(Frame)を作成する。
        # Frameについて : https://kuroro.blog/python/P20XOidA5nh583fYRvxf/
        frame = tk.Frame(self.master)
        # Windowを親要素として、frame Widget(Frame)をどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        frame.pack()

        # frame Widget(Frame)を親要素として、checkbutton Widgetを作成する。
        # text : テキスト情報
        # Checkbuttonについて : https://kuroro.blog/python/gspi4F2pMIkzHN7l0f1F/
        checkbutton = tk.Checkbutton(frame, text="test")
        # frame Widget(Frame)を親要素として、checkbutton Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        checkbutton.pack()

    # button Widgetを取得する関数
    def getButton(self):
        # Windowを親要素として、frame Widget(Frame)を作成する。
        # Frameについて : https://kuroro.blog/python/P20XOidA5nh583fYRvxf/
        frame = tk.Frame(self.master)
        # Windowを親要素として、frame Widget(Frame)をどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        frame.pack()

        # frame Widget(Frame)を親要素として、button Widgetを作成する。
        # text : テキスト情報
        # width : 幅の設定
        # Buttonについて : https://kuroro.blog/python/oFju6EngDtcYtIiMIDf1/
        button = tk.Button(frame, text="test", width=10)
        # frame Widget(Frame)を親要素として、button Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        button.pack()

    # label Widgetを取得する関数
    def getLabel(self):
        # Windowを親要素として、frame Widget(Frame)を作成する。
        # Frameについて : https://kuroro.blog/python/P20XOidA5nh583fYRvxf/
        frame = tk.Frame(self.master)
        # Windowを親要素として、frame Widget(Frame)をどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        frame.pack()

        # frame Widget(Frame)を親要素として、label Widgetを作成する。
        # text : テキスト情報
        # width : 幅の設定
        # bg : 背景色の設定
        # 色について : https://kuroro.blog/python/YcZ6Yh4PswqUzaQXwnG2/
        # Labelについて : https://kuroro.blog/python/Pj4Z7JBNRvcHZvtFqiKD/
        label = tk.Label(frame, text="test", width=10, bg="#008000")
        # frame Widget(Frame)を親要素として、label Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        label.pack()

    def __init__(self, master=None):
        # Windowの初期設定を行う。
        super().__init__(master)
        # Windowの画面サイズを設定する。
        # geometryについて : https://kuroro.blog/python/rozH3S2CYE0a0nB3s2QL/
        self.master.geometry("300x200")
        # self.getLabel()
        # self.getButton()
        # self.getCheckbutton()
        # self.getRadiobutton()
        # self.getMenu()
        # self.getMenubutton()
        # self.getScale()
        # self.getSpinbox()
        # self.getListbox()
        # self.getEntry()
        # self.getText()
        # self.getScrollBar()
        # self.getCanvas()
        # self.getOptionMenu()
        # self.getCombobox()
        # self.getScrolledText()


# Tkinter初学者参考 : https://docs.python.org/ja/3/library/tkinter.html#a-simple-hello-world-program
if __name__ == "__main__":
    # Windowを生成する。
    # Windowについて : https://kuroro.blog/python/116yLvTkzH2AUJj8FHLx/
    root = tk.Tk()
    app = Application(master=root)

    # Windowをループさせて、継続的にWindow表示させる。
    # mainloopについて : https://kuroro.blog/python/DmJdUb50oAhmBteRa4fi/
    app.mainloop()
