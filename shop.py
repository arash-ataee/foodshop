from model import *
from tkinter import *
from tkinter import ttk

foods = {}


def add_food(food_id, number):
    co = psycopg2.connect(database='foodshop', user='arash', password='123212', host='127.0.0.1', port='5432')
    cu = co.cursor()
    cu.execute("SELECT name FROM food WHERE ID={}".format(food_id))
    food = cu.fetchall()[0][0]
    a = {food: number}
    foods[food_id] = a
    co.close()


def delete_food(food_id):
    co = psycopg2.connect(database='foodshop', user='arash', password='123212', host='127.0.0.1', port='5432')
    cu = co.cursor()
    cu.execute("DELETE FROM food WHERE ID={}".format(food_id))
    co.commit()
    co.close()


def shop(food_id, customer_id, number):
    co = psycopg2.connect(database='foodshop', user='arash', password='123212', host='127.0.0.1', port='5432')
    cu = co.cursor()
    cu.execute("SELECT name FROM food WHERE ID={}".format(food_id))
    food = cu.fetchall()[0][0]
    print(foods)
    co.close()
    if foods[food_id].get(food) != 0:
        if foods[food_id].get(food) - number > 0:
            Shop(food_id, customer_id, number)
            foods[food_id][food] -= number
        else:
            print('there is not enough')
    else:
        print('food finished')
        del foods[food_id]


def add_customer(name, address):
    Customer(name, address)


def show_menu():
    f_list = []
    for f in foods.keys():
        f_list.append('name: {} - id: {} - number: {}'.format(foods[f], f, foods[f]))
    return f_list


root = Tk()
root.title('food shop')
root.resizable(False, False)


def new_food_win():
    def new_food_add():
        name = new_food_name_var.get()
        category = new_food_category_var.get()
        price = new_food_price_var.get()
        Food(name, category, price)

    new_food_frame = ttk.Frame(root, padding=(150, 50, 0, 62))
    new_food_frame.grid(column=0, row=0, sticky=(N,S,E,W))
    new_food_label = Label(new_food_frame, font=('tahoma', 20), text='add new food')
    new_food_label.grid(column=1, row=1, columnspan=10)
    new_food_name_var = StringVar()
    new_food_category_var = StringVar()
    new_food_price_var = StringVar()
    new_food_label = Label(new_food_frame, font=('tahoma', 15), text='name: ')
    new_food_label.grid(column=1, row=2)
    new_food_name = Entry(new_food_frame, font=('tahoma', 15), width=20, textvariable=new_food_name_var)
    new_food_name.grid(column=2, row=2)
    new_food_label = Label(new_food_frame, font=('tahoma', 15), text='category: ')
    new_food_label.grid(column=1, row=3)
    new_food_name = Entry(new_food_frame, font=('tahoma', 15), width=20, textvariable=new_food_category_var)
    new_food_name.grid(column=2, row=3)
    new_food_label = Label(new_food_frame, font=('tahoma', 15), text='price: ')
    new_food_label.grid(column=1, row=4)
    new_food_name = Entry(new_food_frame, font=('tahoma', 15), width=20, textvariable=new_food_price_var)
    new_food_name.grid(column=2, row=4)
    new_food_btn = Button(new_food_frame, font=('tahoma', 15), text='add new food', command=new_food_add)
    new_food_btn.grid(column=2, row=5)
    back_btn = Button(new_food_frame, font=('tahoma', 15), text='back', command=add_food_win)
    back_btn.grid(column=2, row=6)


def add_food_win():
    def add_food_def():
        food_id = int(add_food_id_var.get())
        number = int(add_food_number_var.get())
        add_food(food_id, number)

    def food_id_show():
        food_id_list = []
        co = psycopg2.connect(database='foodshop', user='arash', password='123212', host='127.0.0.1', port='5432')
        cu = co.cursor()
        cu.execute("SELECT name, ID FROM food")
        food_info = cu.fetchall()
        for i in food_info:
            food_id_list.append('name: {} - id: {}'.format(i[0], i[1]))
        for j in food_id_list:
            food_show_list.insert('end', j)
        co.close()

    add_food_frame = ttk.Frame(root, padding=(150, 50, 0, 62))
    add_food_frame.grid(column=0, row=0, sticky=(N,S,E,W))
    add_food_label = Label(add_food_frame, font=('tahoma', 20), text='add food')
    add_food_label.grid(column=1, row=1, columnspan=10)
    new_food_btn = Button(add_food_frame, font=('tahoma', 15), text='add new food', command=new_food_win)
    new_food_btn.grid(column=1, row=2, columnspan=2)
    food_show_list = Listbox(add_food_frame, width=40, height=10, font=('tahoma', 15))
    food_show_list.grid(column=1, row=3, columnspan=2)
    food_show_btn = Button(add_food_frame, font=('tahoma', 15), text='show foods id', command=food_id_show)
    food_show_btn.grid(column=1, row=4, columnspan=2)
    add_food_number_var = StringVar()
    add_food_id_var = StringVar()
    add_food_label = Label(add_food_frame, font=('tahoma', 15), text='food ID: ')
    add_food_label.grid(column=1, row=5)
    add_food_name = Entry(add_food_frame, font=('tahoma', 15), width=20, textvariable=add_food_id_var)
    add_food_name.grid(column=2, row=5)
    add_food_label = Label(add_food_frame, font=('tahoma', 15), text='number: ')
    add_food_label.grid(column=1, row=6)
    add_food_name = Entry(add_food_frame, font=('tahoma', 15), width=20, textvariable=add_food_number_var)
    add_food_name.grid(column=2, row=6)
    add_food_btn = Button(add_food_frame, font=('tahoma', 15), text='add food to menu', command=add_food_def)
    add_food_btn.grid(column=2, row=7)
    back_btn = Button(add_food_frame, font=('tahoma', 15), text='back', command=food_shop_win)
    back_btn.grid(column=2, row=8)
    
    
def add_customer_win():
    def new_customer_add():
        name = new_customer_name_var.get()
        category = new_customer_address_var.get()
        Customer(name, category)

    new_customer_frame = ttk.Frame(root, padding=(150, 50, 0, 62))
    new_customer_frame.grid(column=0, row=0, sticky=(N,S,E,W))
    new_customer_label = Label(new_customer_frame, font=('tahoma', 20), text='add new customer')
    new_customer_label.grid(column=1, row=1, columnspan=10)
    new_customer_name_var = StringVar()
    new_customer_address_var = StringVar()
    new_customer_label = Label(new_customer_frame, font=('tahoma', 15), text='name: ')
    new_customer_label.grid(column=1, row=2)
    new_customer_name = Entry(new_customer_frame, font=('tahoma', 15), width=20, textvariable=new_customer_name_var)
    new_customer_name.grid(column=2, row=2)
    new_customer_label = Label(new_customer_frame, font=('tahoma', 15), text='address: ')
    new_customer_label.grid(column=1, row=3)
    new_customer_name = Entry(new_customer_frame, font=('tahoma', 15), width=20, textvariable=new_customer_address_var)
    new_customer_name.grid(column=2, row=3)
    new_customer_btn = Button(new_customer_frame, font=('tahoma', 15), text='add new customer', command=new_customer_add)
    new_customer_btn.grid(column=2, row=4)
    back_btn = Button(new_customer_frame, font=('tahoma', 15), text='back', command=food_shop_win)
    back_btn.grid(column=2, row=5)
    
    
def order_win():
    def order_add():
        customer_id = order_customer_var.get()
        food_id = order_food_var.get()
        number = order_number_var.get()
        print(number)
        shop(customer_id=int(customer_id), food_id=int(food_id), number=int(number))

    def order_food_show():
        food_id_list = []
        co = psycopg2.connect(database='foodshop', user='arash', password='123212', host='127.0.0.1', port='5432')
        cu = co.cursor()
        cu.execute("SELECT name, ID FROM food")
        food_info = cu.fetchall()
        for i in food_info:
            food_id_list.append('name: {} - id: {}'.format(i[0], i[1]))
        for j in food_id_list:
            order_food_list.insert('end', j)
        co.close()

    def order_show_list():
        customer_id_list = []
        co = psycopg2.connect(database='foodshop', user='arash', password='123212', host='127.0.0.1', port='5432')
        cu = co.cursor()
        cu.execute("SELECT name, ID FROM customer")
        customer_info = cu.fetchall()
        for i in customer_info:
            customer_id_list.append('name: {} - id: {}'.format(i[0], i[1]))
        for j in customer_id_list:
            order_customer_list.insert('end', j)
        co.close()
        order_food_show()

    order_frame = ttk.Frame(root, padding=(150, 50, 0, 62))
    order_frame.grid(column=0, row=0, sticky=(N,S,E,W))
    order_label = Label(order_frame, font=('tahoma', 20), text='order')
    order_label.grid(column=1, row=1, columnspan=10)
    order_food_list = Listbox(order_frame, height=10, font=('tahoma', 15))
    order_food_list.grid(column=1, row=2)
    order_customer_list = Listbox(order_frame, height=10, font=('tahoma', 15))
    order_customer_list.grid(column=2, row=2)
    order_show_btn = Button(order_frame, font=('tahoma', 15), text='show lists', command=order_show_list)
    order_show_btn.grid(column=1, row=3, columnspan=2)
    order_customer_var = StringVar()
    order_food_var = StringVar()
    order_number_var = StringVar()
    order_label = Label(order_frame, font=('tahoma', 15), text='customer id: ')
    order_label.grid(column=1, row=4)
    order_name = Entry(order_frame, font=('tahoma', 15), width=20, textvariable=order_customer_var)
    order_name.grid(column=2, row=4)
    order_label = Label(order_frame, font=('tahoma', 15), text='food id: ')
    order_label.grid(column=1, row=5)
    order_name = Entry(order_frame, font=('tahoma', 15), width=20, textvariable=order_food_var)
    order_name.grid(column=2, row=5)
    order_label = Label(order_frame, font=('tahoma', 15), text='number: ')
    order_label.grid(column=1, row=6)
    order_name = Entry(order_frame, font=('tahoma', 15), width=20, textvariable=order_number_var)
    order_name.grid(column=2, row=6)
    order_btn = Button(order_frame, font=('tahoma', 15), text='order', command=order_add)
    order_btn.grid(column=2, row=7)
    back_btn = Button(order_frame, font=('tahoma', 15), text='back', command=food_shop_win)
    back_btn.grid(column=2, row=8)


def food_shop_win():
    def show_menu_list():
        for i in show_menu():
            show_list.insert('end', i)

    food_shop_frame = ttk.Frame(root, padding=(150, 150, 162, 162))
    food_shop_frame.grid(column=0, row=0, sticky=(N,S,E,W))
    food_shop_label = Label(food_shop_frame, font=('tahoma', 20), text='arash food shop')
    food_shop_label.grid(column=0, row=0, columnspan=10)
    menu_list_btn = Button(food_shop_frame, font=('tahoma', 15), text='show menu', command=show_menu_list)
    menu_list_btn.grid(column=1, row=4, columnspan=3)
    add_food_btn = Button(food_shop_frame, font=('tahoma', 15), text='add food', command=add_food_win)
    add_food_btn.grid(column=1, row=1)
    add_food_btn = Button(food_shop_frame, font=('tahoma', 15), text='add customer', command=add_customer_win)
    add_food_btn.grid(column=2, row=1)
    add_food_btn = Button(food_shop_frame, font=('tahoma', 15), text='order', command=order_win)
    add_food_btn.grid(column=3, row=1)
    show_list = Listbox(food_shop_frame, width=40, height=10, font=('tahoma', 15))
    show_list.grid(column=1, row=3, columnspan=3)


food_shop_win()
root.mainloop()
