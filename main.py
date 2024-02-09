from tkinter import *
from tkinter import messagebox


class Calc:
    def __init__(self):
        self.button: list = []
        self.expression: str = ""

        ''' Window Creation '''
        self.root = Tk()
        self.root.title('Calculator')
        self.root.geometry('353x540')
        self.root.resizable(False, False)
        self.root.configure(bg='black')
        self.root.bind('<Return>', lambda event: self.calculate())

        ''' Header '''
        label = Label(self.root, text='Calculator', fg='white', font=('courier', 25, 'bold'), bg='black')
        label.grid(row=0, column=0, ipady=2)

        ''' Display Frame '''
        self.display_frame = Frame(self.root, width=404, height=50, bg='black', borderwidth=3)
        self.display_frame.grid(row=1, column=0, ipadx=2)

        self.text_area = Entry(self.display_frame, bg='#f2dda4', width=20, font=('courier', 20, 'bold'), bd=0)
        self.text_area.focus_set()
        self.text_area.pack(padx=5, pady=3, ipadx=6)

        self.answer_area = Entry(self.display_frame, bg='#f2dda4', width=20, font=('courier', 20, 'bold'), bd=0)
        self.answer_area.configure(state=DISABLED)
        self.answer_area.pack(padx=5, pady=5, ipadx=6)

        ''' Buttons Frame '''
        self.button_frame = Frame(self.root, width=400, height=460, bg='yellow', borderwidth=3)
        self.button_frame.grid(row=2, column=0)

        ''' Button creation '''
        for i in range(6):
            self.button.append([])
            for j in range(4):
                if i == 5:
                    self.button[i].append(None)
                    self.button[i][j] = Button(self.button_frame, text=f'{i},{j}', bd=0, bg='black', borderwidth=2)
                    self.button[i][j].configure(fg='white', font=('arial', 19), border=4, width=4, height=1)
                    self.button[i][j].grid(row=i, column=0, pady=1, padx=1, columnspan=1, ipadx=3, ipady=5)

                    self.button[i].append(None)
                    self.button[i][j+1] = Button(self.button_frame, text=f'{i},{j}', bd=0, bg='black', borderwidth=2)
                    self.button[i][j+1].configure(fg='white', font=('arial', 19), border=4, width=4, height=1)
                    self.button[i][j+1].grid(row=i, column=1, pady=1, padx=1, columnspan=1, ipadx=3, ipady=5)

                    self.button[i].append(None)
                    self.button[i][j+2] = Button(self.button_frame, text=f'{i},{j}', bd=0, bg='#ff4929', borderwidth=2)
                    self.button[i][j+2].configure(fg='white', font=('arial', 19), border=4, height=1)
                    self.button[i][j+2].grid(row=i, column=2, pady=1, padx=1, columnspan=2, ipadx=60, ipady=5)
                    break

                else:
                    self.button[i].append(None)
                    self.button[i][j] = Button(self.button_frame, text=f'{i},{j}', bd=0, bg='black', borderwidth=2)
                    self.button[i][j].configure(fg='white', font=('arial', 19), border=4, width=4, height=1)
                    self.button[i][j].grid(row=i, column=j, pady=1, padx=1, ipadx=3, ipady=5)

        ''' Row 1 '''
        self.button[0][0].configure(text='C', command=self.clear)
        self.button[0][1].configure(text='**', command=lambda: self.add_char('**'))
        self.button[0][2].configure(text=u'\u2190', command=self.backspace)
        self.button[0][3].configure(text='/', command=lambda: self.add_char('/'))

        ''' Row 2 '''
        self.button[1][0].configure(text='7', command=lambda: self.add_char('7'))
        self.button[1][1].configure(text='8', command=lambda: self.add_char('8'))
        self.button[1][2].configure(text='9', command=lambda: self.add_char('9'))
        self.button[1][3].configure(text='*', command=lambda: self.add_char('*'))

        ''' Row 3 '''
        self.button[2][0].configure(text='4', command=lambda: self.add_char('4'))
        self.button[2][1].configure(text='5', command=lambda: self.add_char('5'))
        self.button[2][2].configure(text='6', command=lambda: self.add_char('6'))
        self.button[2][3].configure(text='-', command=lambda: self.add_char('-'))

        ''' Row 4 '''
        self.button[3][0].configure(text='1', command=lambda: self.add_char('1'))
        self.button[3][1].configure(text='2', command=lambda: self.add_char('2'))
        self.button[3][2].configure(text='3', command=lambda: self.add_char('3'))
        self.button[3][3].configure(text='+', command=lambda: self.add_char('+'))

        ''' Row 5 '''
        self.button[4][0].configure(text='00', command=lambda: self.add_char('00'))
        self.button[4][1].configure(text='0', command=lambda: self.add_char('0'))
        self.button[4][2].configure(text='(', command=lambda: self.add_char('('))
        self.button[4][3].configure(text=')', command=lambda: self.add_char(')'))

        ''' Row 6'''
        self.button[5][0].configure(text='i', command=self.show_info)
        self.button[5][1].configure(text='.', command=lambda: self.add_char('.'))
        self.button[5][2].configure(text='=', command=self.calculate)

        ''' Loop '''
        self.root.mainloop()

    def add_char(self, char: str):
        text = StringVar()
        self.expression = self.text_area.get()
        if char is not None:
            self.expression += char

        text.set(self.expression)
        self.text_area.configure(textvariable=text)
        self.text_area.icursor(len(self.text_area.get()))

    def calculate(self):
        if self.text_area.get() == '':
            return
        text = StringVar()
        self.expression = self.text_area.get()

        try:
            text.set("Ans : " + str(eval(self.expression)))
            self.answer_area.configure(state=NORMAL)
            self.answer_area.configure(textvariable=text)
            self.answer_area.configure(state=DISABLED)

        except ZeroDivisionError:
            temp = StringVar()
            temp.set("Zero Division Error")
            self.answer_area.configure(state=NORMAL)
            self.answer_area.configure(textvariable=temp)
            self.answer_area.configure(state=DISABLED)

        except Exception as e:
            temp = StringVar()
            temp.set("Invalid Exception")
            self.answer_area.configure(state=NORMAL)
            self.answer_area.configure(textvariable=temp)
            self.answer_area.configure(state=DISABLED)
            print("Exception : ", e)

    def clear(self):
        self.expression = ''
        text = StringVar()
        text.set(self.expression)
        self.text_area.configure(textvariable=text)
        self.answer_area.configure(state=NORMAL, textvariable=text)
        self.answer_area.configure(state=DISABLED)

    def backspace(self):
        backspace = StringVar()
        text = self.text_area.get()
        temp = text[0:len(text)-1:1]
        backspace.set(temp)
        self.expression = temp
        self.text_area.configure(textvariable=backspace)

    @staticmethod
    def show_info():
        info = f'''        Application \t:    Calculator   
        Designed by \t:    V. Pranitej   
        Created on   \t:    15-01-2023   
        '''
        messagebox.showinfo('Info', info)


if __name__ == '__main__':
    clac_obj: Calc = Calc()
