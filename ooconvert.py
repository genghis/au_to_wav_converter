import os
import soundfile as sf
from tkinter import (Tk, BOTH, RIGHT, LEFT, Text, E, W, S, N, Y, END, NORMAL,
                     DISABLED, StringVar, Scrollbar, Listbox)
import tkinter.filedialog as fdialog
from tkinter.ttk import Frame, Label, Button, Progressbar
from functools import partial
from threading import Thread

class Convert(Frame):

	def __init__(self, parent):
		Frame.__init__(self, parent)

		self.parent = parent
		self.initUI()

	def initUI(self):

		self.parent.title('AU to WAV Converter')
		self.pack(fill=BOTH, expand=True)

		self.to_convert = Button(
		    master=self, text="Select Folder", command=lambda: self.get_dir())
		self.to_convert.pack()

		self.target_dir = Label(master=self, text="None Selected")
		self.target_dir.pack()

		self.number_of_files = Label(master=self, text='')
		self.number_of_files.pack()

		self.btn_convert = Button(
		    master=self, text="CONVERT", command=self.dispatch)
		self.btn_convert.pack()

		self.pbar = Progressbar(self, orient="horizontal", length=400, mode='determinate')
		self.pbar.pack()

		self.scrollbar = Scrollbar(self)
		self.scrollbar.pack(side=RIGHT, fill=Y)

		self.converted = Listbox(self, height=30, width=80)
		self.converted.pack()
		self.converted.config(yscrollcommand=self.scrollbar.set)

		self.converted_count = Label(master=self, text='')
		self.converted_count.pack()

	def get_dir(self):
		directory = fdialog.askdirectory()
		self.target_dir['text'] = directory
		file_count = 0
		for file in [f for f in os.listdir(directory) if f.endswith('.au')]:
			file_count += 1
		self.number_of_files['text'] = f'{file_count} files will be converted'
		self.pbar['maximum'] = file_count

	def dispatch(self):
		self.btn_convert.config(state = DISABLED)
		self.au_to_wav_count = 0
		directory = self.target_dir['text']
		self.iterator = [(directory, f) for f in os.listdir(directory) if f.endswith('.au')]
		Thread(target=self.conversion).start()

	def conversion(self):
		for filetuple in self.iterator:
			directory = filetuple[0]
			file = filetuple[1]
			file_name = file.split('.')[0]
			export_name = f'{directory}/{file_name}.wav'
			get_file = f'{directory}/{file}'
			data, samplerate = sf.read(get_file)
			sf.write(export_name, data, samplerate)
			self.au_to_wav_count += 1
			self.converted_count['text'] = f'{self.au_to_wav_count} Files Converted'
			self.converted.insert(END, f'{file_name}.wav')
			self.pbar['value'] += 1

def main():

	root = Tk()
	root.geometry("750x750+750+750")
	app = Convert(root)
	root.mainloop()

if __name__ == '__main__':
	main()


