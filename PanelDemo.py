
from breezypythongui import EasyFrame
from tkinter import PhotoImage 

class PanelDemo(EasyFrame):
	def __init__(self):

		#create the main frame
		def __init__(self):
		"""sets up the window and widgets"""
		EasyFrame.__init__(self, title = "Image Viewer 1.0", width = 300, height = 100)
		self.label = self.addLabel(text = "Now you see me", row = 0, column = 0, sticky = "NSEW")
		self.label = self.addLabel(text = "", row = 0, column = 0, columnspan = 2, sticky = "NSEW")
		self.addButton(text = "click", row = 1, column = 0, command = self.click)

	def click(self):
		self.label = self.addLabel(text = "", row = 0, column = 0, columnspan = 2, sticky = "NSEW")
		self.label = self.addLabel(text = "now you don't", row = 0, column = 0, columnspan = 2, sticky = "NSEW")
		self.addButton(text = "click", row = 1, column = 0, command = self.clickRestore)

		


		

		#create the nested frame for the data panel
		dataPanel = self.addPanel(row = 0, column = 0, background = "white")

		
		#create the nested frame for the button panel
		buttonPanel = self.addPanel(row = 1, column = 0, background = "blue")

		# Create and add buttons to the button pannel
		buttonPanel.addButton(text = "Click", row = 0, column = 0)
		buttonPanel.addButton(text = "Click", row = 0, column = 1)
		buttonPanel.addButton(text = "Click", row = 0, column = 2)

def main():
	PanelDemo().mainloop()

main()












d