from tkinter import *
root = Tk()
root.title("Fibonacci")
root.geometry("400x400")
 label_series = Label(root, text="fibonacci series: ")
label_flower = Label(root)
label_spiral = Label(root)

def fibonacci():
 num =10
first_num = 0
second_num = 1
sum = 0
counter = 1
while(counter <= num):
 label_series["text"] += str(sum)+" "
counter = counter +1 
first_num = second_num 
second_num = sum 
sum = first_num + second_num
label_flower['text'] ="flower is fully bloomed"
label_spiral["text"] ="Spirals in right direction are"+ str(first_num)+"Spirals in the left direction are "+str(second_num)+"\n. Total spiral are "+str(sum)
btn = Button(root, text = "show fibonacci series", command = fibonacci)
btn.pack()
label_series.pack()
label_flower.pack()
label_spiral.pack()
root.mainloop()
