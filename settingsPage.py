from settings import *
import settings
from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox

class settingsPage:
    def startup(root):
        window = Toplevel(root)
        window.title(SETTINGS_TITLE)
        window.geometry(f"{SETTINGS_WIDTH}x{SETTINGS_HEIGHT}")
        settingsPage.settingsRender(Main_Settings, window)

    def settingsRender(settings, window):
        for setting in settings:
            if settings[0] == setting:
                button = Button(window, text=setting)
                button.config(command = lambda: nestedSettings.settingsIdentify(button['text'], window))
                button.pack(pady = 30)
            if settings[1] == setting:
                button1 = Button(window, text=setting)
                button1.config(command = lambda: nestedSettings.settingsIdentify(button1['text'], window))
                button1.pack(pady = 30)
            if settings[2] == setting:
                button2 = Button(window, text=setting)
                button2.config(command = lambda: nestedSettings.settingsIdentify(button2['text'], window))
                button2.pack(pady = 30)
            if settings[3] == setting:
                button3 = Button(window, text=setting)
                button3.config(command = lambda: nestedSettings.settingsIdentify(button3['text'], window))
                button3.pack(pady = 30)


def updateTheme(option, window):
    settings.CURRENT_THEME = option
    CURRENT_THEME = option
    print(option)
    print(settings.CURRENT_THEME)
    window.destroy()

class nestedSettings:
    def settingsIdentify(settingMenu, window):
        if settingMenu == "Themes":
            nestedSettings.clearScreen(window)
            nestedSettings.themes(window)
        elif settingMenu == "Graph":
            messagebox.showinfo("Content unavailable", "This content has not been released yet!")
        elif settingMenu == "Accessibility":
            messagebox.showinfo("Content unavailable", "This content has not been released yet!")
        elif settingMenu == "Language":
            messagebox.showinfo("Content unavailable", "This content has not been released yet!")
    
    def themes(window):
        themeLabel = Label(window, text = "Themes")
        themeLabel.place(x = 30, y = 30)

        themesVar = StringVar(window)
        themesVar.set(settings.CURRENT_THEME)
        themeSelect = OptionMenu(window, themesVar, *THEMES)
        themeSelect.place(x = 300,y = 25)

        save = Button(window, text = "Save Settings", command = lambda: updateTheme(themesVar.get(), window))
        save.place(x = 280, y = 360)
    
    def graph(window):
        return

    def graph2(window):
        #Labels
        outlineColorText = Label(window, text = "Outline Colour:")
        outlineColorText.place(x = 30, y = 100)

        backgroundColorText = Label(window, text = "Background Colour:")
        backgroundColorText.place(x = 30, y = 170)

        ##Options
        outlineVar = StringVar(window)
        outlineVar.set(COLOURS[7])
        outlineMenu = OptionMenu(window, outlineVar, *COLOURS)
        outlineMenu.place(x = 300, y = 95)
        outlineVar.trace("w", callback)

        backgroundVar = StringVar(window)
        backgroundVar.set(COLOURS[7])
        backgroundMenu = OptionMenu(window, backgroundVar, *COLOURS)
        backgroundMenu.place(x = 300, y = 165)


    def language():
        return
    
    def accessibility():
        return
    
    def clearScreen(window):
        _list = window.winfo_children()

        for item in _list :
            if item.winfo_children() :
                _list.extend(item.winfo_children())
        
        for item in _list:
            item.pack_forget()