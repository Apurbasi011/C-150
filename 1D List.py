from tkinter import * 
import random

root = Tk()
root.title("Luck Friend Wheel")
root.geometry("400x400")

enter_name = Entry(root)
enter_name.place(relx = 0.5, rely = 0.2, anchor = CENTER)

friend_list = Label(root)
random_number_label = Label(root)
lucky_friend = Label(root)

list1 = []
def addfriend():
    
    friend_name = enter_name.get()
    list1.append(friend_name)
    friend_list ["text"] = "Your Friend List : " + str(list1)
    
def random_number():
    length = len(list1)
    random_number = random.randint(0, length - 1)
    random_number_label ["text"] = str(random_number)
    generated_random_number = list1[random_number]
    lucky_friend ["text"] = "Your Lucky Friend Is : " + str(generated_random_number)
    
btn = Button(root, text = "Add A Friend To The Friend List", command = addfriend)
btn.place(relx = 0.5, rely = 0.3, anchor = CENTER)

friend_list.place(relx = 0.5, rely = 0.4, anchor = CENTER)

btn1 = Button(root, text = "Who Is Your Lucky Friend?", command = random_number)
btn1.place(relx = 0.5, rely = 0.5, anchor = CENTER)

random_number_label.place(relx =0.5, rely = 0.6, anchor = CENTER)
lucky_friend.place(relx = 0.5, rely = 0.7, anchor = CENTER)

root.mainloop()

