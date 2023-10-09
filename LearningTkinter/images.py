# from tkinter import *
# from PIL import ImageTk ,Image
# root = Tk()
# root.title("Team DevDuo/DebuggingDuo/Dev-N-Debug")
# # root.iconbitmap("moneyIcon.ico")




# my_img1= ImageTk.PhotoImage(Image.open("LearningTkinter/NyayeSathi_logo_picture.png"))
# my_img2 = ImageTk.PhotoImage(Image.open("LearningTkinter/greenCALC.png"))
# # my_label1 = Label(image = my_img1)
# # my_label1.pack()
# # my_label2 = Label(image = my_img1)
# # my_label2.pack()

# img_list = [my_img1, my_img2,my_img1]

# my_label = Label(image = my_img1)
# my_label.grid(row = 0, column =0 , columnspan =3)

# def forward(image_number):
#     global my_label
#     global button_forward
#     global button_back
    
#     my_label.grid_forget()
#     my_label = Label(image = img_list[image_number -1 ])
#     # my_label = Label(image = my_img2)

# def back():
#     global my_label
#     global button_forward
#     global button_back
    
    
    
# button_back  = Button(root, text = "<<", command = back)
# button_forward  = Button(root, text = ">>")
# button_quit = Button (root, text = "exit program", command = root.quit)

# button_back.grid(row =1, column = 0)
# button_quit.grid(row = 1, column =1)
# button_forward.grid(row =1, column = 2)


# root.mainloop()


a= 3
print (type(a))