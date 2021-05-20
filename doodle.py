from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Scale
from PIL import ImageTk, Image

root = Tk()
root.attributes("-fullscreen", False)
root.title("DOODLE")
Icon = PhotoImage(file="doodle.png")
root.iconphoto(False, Icon)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


class Paint:
    font = StringVar()
    text = IntVar()
    bold = IntVar()
    italic = IntVar()
    x_pos, y_pos = None, None
    x_start, y_start, x_final, y_final = None, None, None, None
    control = "up"

    @staticmethod
    def quit():
        root.quit()

    @staticmethod
    def about():
        messagebox.showinfo('DOODLE', 'Go to the help in the main window')

    def menu_bar(self):
        menu = Menu(root)

        # FILE MENU
        file_menu = Menu(menu, tearoff=0)
        file_menu.add_command(label="📂 Open")
        file_menu.add_command(label="📥 Save")
        file_submenu = Menu(file_menu)
        file_submenu.add_radiobutton(label="📊 Png")
        file_submenu.add_radiobutton(label="💷 Jpeg")
        file_submenu.add_radiobutton(label="🧧 Gif")
        file_menu.add_cascade(label="💾 Save as", menu=file_submenu)
        file_menu.add_separator()
        file_menu.add_command(label="❌ Quit", command=self.quit)
        menu.add_cascade(label="🗂 File", menu=file_menu)

        # FONT MENU:
        font_menu = Menu(menu, tearoff=0)
        type_submenu = Menu(font_menu)
        type_submenu.add_radiobutton(label="Times", variable=self.font)
        type_submenu.add_radiobutton(label="Courier", variable=self.font)
        type_submenu.add_radiobutton(label="Ariel", variable=self.font)
        font_menu.add_cascade(label="Font style", menu=type_submenu)

        size_submenu = Menu(font_menu)
        size_submenu.add_radiobutton(label="🛑 10", variable=self.text)
        size_submenu.add_radiobutton(label="🛑 15", variable=self.text)
        size_submenu.add_radiobutton(label="🛑 20", variable=self.text)
        size_submenu.add_radiobutton(label="🛑 25", variable=self.text)
        font_menu.add_cascade(label="Font size", menu=size_submenu)
        font_menu.add_checkbutton(label="Bold", variable=self.bold, onvalue=1, offvalue=0)
        menu.add_cascade(label="✏ Font", menu=font_menu)

        # EDIT MENU
        edit_menu = Menu(menu, tearoff=0)
        edit_menu.add_command(label="Undo")
        edit_menu.add_separator()
        edit_menu.add_command(label="Cut")
        edit_menu.add_command(label="Copy")
        edit_menu.add_command(label="Paste")
        menu.add_cascade(label="✒ Edit", menu=edit_menu)

        # HELP MENU
        help_menu = Menu(menu, tearoff=0)
        help_menu.add_command(label="⁉ About", command=self.about)
        menu.add_cascade(label="❓ Help", menu=help_menu)

        root.config(menu=menu)

    def __init__(self):

        self.menu_bar()
        self.pen_color = "black"
        self.color_fill = LabelFrame(root, text="Color", font=("Times", 15, "bold"), bd=5, relief=RIDGE, bg="white")
        self.color_fill.place(x=0, y=0, width=70, height=185)
        colors = ["#000000", "#FFFFFF", "#FF0000", "#00FF00", "#0000FF", "#FFFF00", "#FFD700", "#FF00FF", "#FFC0CB",
                  "#800080", "#00ffd9", "#808080"]
        i = j = 0
        for color in colors:
            Button(self.color_fill, bg=color, bd=2, relief=RIDGE, width=3,
                   command=lambda col=color: self.select_color(col)).grid(row=i, column=j)
            i = i + 1
            if i == 6:
                i = 0
                j = 1
        # CREATING BUTTONS:
        self.eraser_img = ImageTk.PhotoImage(
            Image.open("Pictures/eraser.png").resize((28, 20), Image.ANTIALIAS))
        self.eraser_btn = Button(root, image=self.eraser_img, fg="red", bg="white", font=("Arial", 10, "bold"),
                                 relief=RAISED, bd=3, command=self.eraser)
        self.eraser_btn.place(x=0, y=187)
        self.colorbox_img = ImageTk.PhotoImage(
            Image.open("Pictures/bucket.jpg").resize((25, 20), Image.ANTIALIAS))
        self.colorbox_btn = Button(root, image=self.colorbox_img, fg="red", bg="white", font=("Arial", 10, "bold"),
                                   relief=RAISED, bd=3, command=None)
        self.colorbox_btn.place(x=37, y=187)
        self.clear = Button(root, text="Clear", bd=4, bg="white", width=8, relief=RIDGE,
                            command=lambda: self.canvas.delete("all"))
        self.clear.place(x=0, y=217)
        self.canvas = Button(root, text="Canvas", bd=4, bg="white", width=8, relief=RIDGE, command=None)
        self.canvas.place(x=0, y=247)
        # CREATING SIZE FOR PENCIL AND ERASER
        self.pen_size = LabelFrame(root, text="Size", bd=5, bg="white", font=("Times", 15, "bold"), relief=RIDGE)
        self.pen_size.place(x=0, y=280, height=150, width=70)
        self.pen_size1 = Scale(self.pen_size, orient=VERTICAL, from_=50, to=0, length=120)
        self.pen_size1.set(1)
        self.pen_size1.grid(row=0, column=1, padx=15)
        self.canvas = Canvas(root, bd=6, bg="white", relief=GROOVE, height=600, width=1000)
        self.canvas.place(x=80, y=0)
        self.shapes = Label(root, text="Shapes", bd=4, bg="white", width=8, relief=RIDGE, command=None)
        self.shapes.place(x=0, y=430)
        self.rectangle_img = ImageTk.PhotoImage(Image.open("Pictures/rectangle.jpg").resize((20, 20), Image.ANTIALIAS))
        self.rec = Button(root, image=self.rectangle_img, fg="red", bg="white",
                          font=("Arial", 10, "bold"), relief=RAISED, bd=3, command=None)
        self.rec.place(x=0, y=455)

        self.circle_img = ImageTk.PhotoImage(
            Image.open("Pictures/circle.png").resize((20, 20), Image.ANTIALIAS))
        self.circle_btn = Button(root, image=self.circle_img, fg="red", bg="white", font=("Arial", 10, "bold"),
                                 relief=RAISED, bd=3, command=None)
        self.circle_btn.place(x=0, y=485)

        assert isinstance(Image.open("Pictures/triangle.jpg").resize, object)
        self.triangle_img = ImageTk.PhotoImage(Image.open("Pictures/triangle.jpg").resize((20, 20), Image.ANTIALIAS))
        self.triangle_btn = Button(root, image=self.triangle_img, fg="red", bg="white",
                                   font=("Arial", 10, "bold"), relief=RAISED, bd=3, command=None)
        self.triangle_btn.place(x=37, y=455)

        self.pentagon_img = ImageTk.PhotoImage(Image.open("Pictures/pentagon.png").resize((20, 20), Image.ANTIALIAS))
        self.pentagon_btn = Button(root, image=self.pentagon_img, fg="red", bg="white",
                                   font=("Arial", 10, "bold"), relief=RAISED, bd=3, command=None)
        self.pentagon_btn.place(x=37, y=485)

        # mouse drag
        self.canvas.bind("<B1-Motion>", self.paint_app)
        self.canvas.bind("<Motion>", self.coordinates)

        # status bar
        self.status = Label(relief=RIDGE, font='Times 17 bold', bg='white', fg='black', anchor=W)
        self.status.pack(side=BOTTOM, fill=X)

    def paint_app(self, event):
        x_start, y_start = (event.x - 2), (event.y - 2)
        x_final, y_final = (event.x + 2), (event.y + 2)

        self.canvas.create_oval(x_start, y_start, x_final, y_final, fill=self.pen_color, outline=self.pen_color,
                                width=self.pen_size1.get())

    def select_color(self, col):
        self.pen_color = col

    def eraser(self):
        self.pen_color = "white"

    def coordinates(self, event):
        self.status['text'] = f'Cursor coordinates : ({event.x},{event.y})'


paint = Paint()
root.mainloop()
