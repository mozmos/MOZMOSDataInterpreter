from tkinter import *
from tkinter import filedialog, messagebox
from settings import *

class FileImport:
    def importfile():
        importedFile = str(filedialog.askopenfilename(filetypes = [("Text Files","*.txt")]))
        check = FileImport.checkImportedFile(importedFile)
        if check == "success":
            return importedFile
        else:
            return "failed"
    
    def checkImportedFile(file):
        if file == "" or file == "None":
            print("No file was selected")
            messagebox.showwarning("No File Loaded", "No file was selected!")
            return "nofile"
        else:
            return 'success'
        