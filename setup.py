from tkinter import messagebox
from distutils.core import setup

def popup():
    messagebox.showinfo("Information", "Thanks for downloading.\nVisit https://github.com/Forhad95000 for more items")

setup (
	name = "Python-GPU_benchmark",
	version = "1.0",
	packages = ["GPU_benchmark"],
	license = "MIT",
	long_description = open("README.md").read()
)

popup()
