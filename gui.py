import tkinter as tk

from PIL import Image,ImageTk

from deezer_api import get_albums


root = tk.Tk()
root.geometry('700x500')
root.resizable(0,0)
#search_label = Label(root,text="Izvodjac")

#frm_search =  tk.Frame(root,width=300,height=32)
#frm_search.pack_propagate(0)
#frm_search.pack(side=tk.LEFT)

frm_search = tk.Frame(root)
frm_search.pack()

#frm_albums = tk.Frame(root)
#frm_albums.pack()


lbl_izvodjac = tk.Label(master=frm_search,text="Izvodjac:",bg='orange')
lbl_izvodjac.pack(side=tk.LEFT)

ent_search = tk.Entry(master=frm_search,width=50,fg='white',bg='black')
ent_search.pack(side=tk.LEFT)

#txt_albums = tk.Text(master=frm_albums,width=62,bg='orange')
#txt_albums.pack()


frm_albums2 = tk.Frame(root)
frm_albums2.pack()

lbl_loading = tk.Label(master=frm_albums2,text="Loading...")

#event listeners
def show_albums():
	lbl_loading.pack()
	artist_name = ent_search.get()
	dct_albums = get_albums(artist_name)

	r = 0
	for album in dct_albums:
		#txt_albums.insert(tk.END,album+'\n')
		tk.Label(text=f'{album}').grid(row=r,column=0)
		tk.Button(text='Vidi pesme').grid(row=r,column=1)
		r += 1


	lbl_loading.pack_forget()
#--------------------------
size = 20,17
im = Image.open('icons/search.png')
im.thumbnail(size,Image.ANTIALIAS)
ph = ImageTk.PhotoImage(im)
btn_search = tk.Button(master=frm_search,image=ph,bg='orange',command=show_albums)
btn_search.image = ph
btn_search.pack(side=tk.LEFT)

#-----------------------------



root.mainloop()