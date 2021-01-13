from tkinter import *
from tkinter import messagebox

from ttkthemes import themed_tk as tk
from tkinter import ttk

import sqlite3


root = tk.ThemedTk()
root.get_themes()
root.set_theme("adapta")



#Database
conn = sqlite3.connect('enrollment_database.db')

#cursor
c = conn.cursor()
c.execute("""SELECT rowid FROM Student""")
retrieved_rowid = c.fetchall()
c.execute("""SELECT Student_pass FROM Student""")
retrieved_password = c.fetchall()
c.execute("SELECT rowid FROM Student ORDER BY rowid DESC LIMIT 1")
generated_id = c.fetchone()

		#self.retrieved_password = self.conn.fetchall()
		#if self.Studid.get() == self.retrieved_rowid and self.Studpass.get() == self.retrieved_password:
			#self.Welcome = ttk.Label(self.Portal, text="Welcome!").grid(row=9, column=0)
			#self.Studid.delete(0, END)
			#self.Studpass.delete(0, END)
			#New window subject selection
			#success = Process()
			#success.selection()

test = LabelFrame(root)
text = Label(test, text=retrieved_rowid)
text1 = Label(test, text=retrieved_password)
text2 = Label(test, text=generated_id)
test.pack()
text.pack()
text1.pack()
text2.pack()

root.mainloop()
