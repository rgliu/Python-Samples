from Tkinter import *
import Tkinter as tk
import tkFont
import ttk
from spotify_mp3 import *
#import webbrowser

class Application(Frame):
	
	sp = Spotify_MP3("BQAlMfd0t-3fpyJ3FZmtQod8t6aM2a-GZRH7KW7wsPnSQOBTW9ZNzifl_IEV2YuH9wZMliN-_hK2Q-PGs0FeKhe_mXZaa_tyjsOCkKBwPJ0zG-lH2bqBnNSi-xWotFAqNJ8P4o54cKLaniL2TYlskN6EQs27J-o")
	
	def create_GUI(self):
		default_font = tkFont.nametofont("TkDefaultFont")
		default_font.configure(size=12)
		self.option_add("*Font", default_font)

		self.master.title("Spotify Player")
		
		global mainframe
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
		
		global results_frame
		results_frame = ttk.Frame(mainframe, padding="3 3 12 0")
		
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
		
		search_button = tk.Button(search_button_frame, text="Search", background = "DarkSeaGreen1", command=lambda:self.search_and_display_results(track_search_name.get(), artist_search_name.get()) )
		search_button.grid(column=0, row=0, sticky=(N, W, E, S)) 
		
		# Pad all frames within the mainframe
		for child in search_entry_frame.winfo_children(): child.grid_configure(padx=5, pady=5)
		for child in search_button_frame.winfo_children(): child.grid_configure(padx=5, pady=5)
		
		self.mainloop()
		
	
	def del_results(self):
		global results_frame
		global mainframe
		global result_label
		global play_button
		global track_uris # A separate list of uris is easier to read/implement
		results_frame.destroy()
		results_frame = ttk.Frame(mainframe, padding="3 3 12 0")
		results_frame.grid(column=1, row=0, sticky=(N, W, E, S))
		results_frame.columnconfigure(0, weight=1)
		results_frame.rowconfigure(0, weight=1)
		results_header = ttk.Label(results_frame, text="Top Result(s)")
		results_header.grid(column=1, row=0, sticky=(N))
		result_label = []
		play_button = []
		track_uris = []
		
	
	def search_and_display_results(self, track, artist):
		global result_label
		global play_button
		global track_uris
		self.sp.clear_search_results()
		self.del_results()
		self.sp.search_music_library(track, artist)
		for i,result in enumerate(self.sp.search_results):
			play_button.append(tk.Button(results_frame, text=" ", command=lambda:self.play_track(i)))
			play_button[i].grid(column=0, row=i+1, sticky=(N,W))
			result_label.append(ttk.Label(results_frame, text=result[0]))
			result_label[i].grid(column=1, row=i+1, sticky=(W))
			track_uris.append(result[1])
			
	def play_track(self, button_index):
		#global track_uris
		#self.sp.play_track(track_uris[button_index])
		#webbrowser.open("index.html").read().format(uri="spotify:track:1BuZAIO8WZpavWVbbq3Lci")
		print "Play feature not implemented yet"
		


	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.pack()
		self.create_GUI()

		
