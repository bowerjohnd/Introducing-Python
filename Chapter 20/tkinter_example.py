import tkinter
from PIL import Image, ImageTk

main = tkinter.Tk()
img = Image.open('oreilly.jpg')
img = img.rotate(-90)
img = img.transpose(Image.FLIP_TOP_BOTTOM)

tkimg = ImageTk.PhotoImage(img)
tkinter.Label(main, image=tkimg).pack()
main.mainloop()