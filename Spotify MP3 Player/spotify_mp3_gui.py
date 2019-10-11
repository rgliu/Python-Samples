from Tkinter import *
import Tkinter as tk
import tkFont
import ttk
from spotify_mp3 import *

class Application(Frame):
	
	sp = Spotify_MP3("BQBROx1LwM0Q_CtudkGxUf021qcJjwkpkjIrtGVvJPmRaIza_h_D9BRcuP8mowhN292WoZ83H1vXO48eZ3mL3awj6S7a8Aqu0I-pvf5GOnme6XRo7iTEwDxDRhT66H-Chmqoj_sFYtfYZId97E_KpwiBLvVIxJY")
	
	def create_GUI(self):
		default_font = tkFont.nametofont("TkDefaultFont")
		default_font.configure(size=12)
		self.option_add("*Font", default_font)

		self.master.title("Spotify Player")
		
		mainframe = ttk.Frame(self, padding="3 3 12 12")
		mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
		mainframe.columnconfigure(0, weight=1)
		mainframe.rowconfigure(0, weight=1)
		
		search_frame = ttk.Frame(mainframe, padding="3 3 12 0")
		search_frame.grid(column=0, row=0, sticky=(N, W, E, S))
		search_frame.columnconfigure(0, weight=1)
		search_frame.rowconfigure(0, weight=1)
		
		search_entry_frame = ttk.Frame(search_frame, padding="3 3 12 0")
		search_entry_frame.grid(column=0, row=0, sticky=(N, W, E, S))
		search_entry_frame.columnconfigure(0, weight=1)
		search_entry_frame.rowconfigure(0, weight=1)
		
		search_button_frame = ttk.Frame(search_frame, padding="3 3 12 0")
		search_button_frame.grid(column=0, row=1, sticky=(N, W, E, S))
		search_button_frame.columnconfigure(0, weight=1)
		search_button_frame.rowconfigure(0, weight=1)
		
		results_frame = ttk.Frame(mainframe, padding="3 3 12 0")
		results_frame.grid(column=0, row=1, sticky=(N, W, E, S))
		results_frame.columnconfigure(0, weight=1)
		results_frame.rowconfigure(0, weight=1)

		######################################################################################
		####
		#### Track and Artist Search Entries
		####
		#### Search Button
		####
		######################################################################################

		track_search_name = StringVar(None, "")
		artist_search_name = StringVar(None, "")

		track_search_label = ttk.Label(search_entry_frame, text="Track Name")
		track_search_label.grid(column=0, row=0)

		track_search_entry = ttk.Entry(search_entry_frame, width=20, textvariable=track_search_name)
		track_search_entry.grid(column=1, row=0)

		artist_search_label = ttk.Label(search_entry_frame, text="Artist Name")
		artist_search_label.grid(column=0, row=1)

		artist_search_entry = ttk.Entry(search_entry_frame, width=20, textvariable=artist_search_name)
		artist_search_entry.grid(column=1, row=1)	
		
		search_button = tk.Button(search_button_frame, text="Search", background = "DarkSeaGreen1", command=lambda: self.sp.search_music_library(track_search_name.get(), artist_search_name.get()))
		search_button.grid(column=0, row=0, sticky=(N, W, E, S)) 
		
		
		# Pad all frames within the mainframe
		for child in search_entry_frame.winfo_children(): child.grid_configure(padx=5, pady=5)
		for child in search_button_frame.winfo_children(): child.grid_configure(padx=5, pady=5)
		
		self.mainloop()
		 
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.pack()
		self.create_GUI()

		
