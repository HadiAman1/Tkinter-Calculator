from sqlite3 import *
from tkinter import *
from tkinter.messagebox import *
from tkinter.colorchooser import *
######################################################

conn = connect('config.db')
c = conn.cursor()
try:
    c.execute('select * from config;')
except:
    query1 = 'create table config(id int(5), apptitle varchar(15), bg_color varchar(15), ebgcolor varchar(15),' \
            ' bg_color_btn varchar(15), fg_color_btn varchar(15), activebackground_color varchar(15),' \
            ' activeforeground_color varchar(15));'
    c.execute(query1)

    query2 = "insert into config(id, apptitle, bg_color, ebgcolor, bg_color_btn, fg_color_btn, activebackground_color," \
             " activeforeground_color) values(1, 'Calculator', 'black', '#ffffff', '#566573', '#ffffff', '#46535f'," \
             " '#ffffff');"
    c.execute(query2)
    conn.commit()


def set_app_title():
    app = Tk()
    app.maxsize(width='153', height='80')
    app.minsize(width='153', height='80')
    E = Entry(app)
    E.grid(column=0, row=0)

    def set_title():
        if E.get() == '':
            pass
        else:
            try:
                query = "update config set apptitle='%s'" % E.get()
                c.execute(query)
                showwarning('WARNING', 'To apply changes restart the app')
                conn.commit()
            except:
                pass
    Button(app, text='Set', command=set_title).grid(column=0, row=1)
    app.mainloop()


def set_bg_color():
    color_code = askcolor(title="Choose color")[1]
    if color_code is None:
        pass
    else:
        query = "update config set bg_color='%s'" % color_code
        c.execute(query)
        conn.commit()
        showwarning('WARNING', 'To apply changes restart the app')


def set_ebgcolor():
    color_code = askcolor(title="Choose color")[1]
    if color_code is None:
        pass
    else:
        query = "update config set ebgcolor='%s'" % color_code
        c.execute(query)
        conn.commit()
        showwarning('WARNING', 'To apply changes restart the app')


def set_bg_color_btn():
    color_code = askcolor(title="Choose color")[1]
    if color_code is None:
        pass
    else:
        query = "update config set bg_color_btn='%s'" % color_code
        c.execute(query)
        conn.commit()
        showwarning('WARNING', 'To apply changes restart the app')


def set_fg_color_btn():
    color_code = askcolor(title="Choose color")[1]
    if color_code is None:
        pass
    else:
        query = "update config set fg_color_btn='%s'" % color_code
        c.execute(query)
        conn.commit()
        showwarning('WARNING', 'To apply changes restart the app')


def set_activebackground_color():
    color_code = askcolor(title="Choose color")[1]
    if color_code is None:
        pass
    else:
        query = "update config set activebackground_color='%s'" % color_code
        c.execute(query)
        conn.commit()
        showwarning('WARNING', 'To apply changes restart the app')


def set_activeforeground_color():
    color_code = askcolor(title="Choose color")[1]
    if color_code is None:
        pass
    else:
        query = "update config set activeforeground_color='%s'" % color_code
        c.execute(query)
        conn.commit()
        showwarning('WARNING', 'To apply changes restart the app')


#################################################


def get_app_title():
    query = 'select apptitle from config'
    c.execute(query)
    x = c.fetchall()[0][0]
    return x

def get_bg_color():
    query = 'select bg_color from config'
    c.execute(query)
    x = c.fetchall()[0][0]
    return x


def get_ebgcolor():
    query = 'select ebgcolor from config'
    c.execute(query)
    x = c.fetchall()[0][0]
    return x


def get_bg_color_btn():
    query = 'select bg_color_btn from config'
    c.execute(query)
    x = c.fetchall()[0][0]
    return x


def get_fg_color_btn():
    query = 'select fg_color_btn from config'
    c.execute(query)
    x = c.fetchall()[0][0]
    return x


def get_activebackground_color():
    query = 'select activebackground_color from config'
    c.execute(query)
    x = c.fetchall()[0][0]
    return x


def get_activeforeground_color():
    query = 'select activeforeground_color from config'
    c.execute(query)
    x = c.fetchall()[0][0]
    return x
