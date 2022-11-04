from tkinter import *
import autopy

program = Tk()
# Centering Window
window_width = 300
window_height = 400
xx = int((program.winfo_screenwidth()-window_width)/2)
yy = int((program.winfo_screenheight()-window_height)/2)

# Then, you will define the size of the window in width(312) 
# and height(324) using the 'geometry' method
program.geometry(f"{window_width}x{window_height}+{xx}+{yy}")

program.title("Selfy Camera V1.2")

titlle = Label(program, text="Selfy Camera", bg="Black", fg="White", font=('arial', 18, 'bold'))
titlle.pack(fill=X)

photo = PhotoImage(file=r"F:\WEB-Devolopment\Python\Projects\Holding-Programs\Taking-Screen-shoot\download.jpg")
imago = Label(program, image=photo)
imago.place(x=50, y=50, width=200, height=200)

def takingphoto():
    photoimg = autopy.bitmap.capture_screen()
    photoimg.save(r"F:\WEB-Devolopment\Python\Projects\Holding-Programs\Taking-Screen-shoot\photo-1.png")

takephoto = Button(program, text="Take Photo", bg="Black", fg="White", font=('arial', 10, 'bold'), command=takingphoto)
takephoto.place(x=100, y=325, width=100, height=20)

quitButton = Button(program, text="Close", bg="Black", fg="White", font=('arial', 10, 'bold'), command=program.quit)
quitButton.place(x=100, y=350, width=100, height=20)

program.mainloop()