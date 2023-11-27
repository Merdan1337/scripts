import customtkinter as ctk
import tkinter

ctk.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

# Mainwindow Settings
window = ctk.CTk()
window.geometry("350x660")
window.title("CONFIG")
window.resizable(False, False)

# Variables for Radiobuttons and different Font-Styles
var_Winfull = tkinter.IntVar(value=1)
var_Fontname = tkinter.IntVar(value=1)
var_Fontsize = tkinter.IntVar(value=1)
fnt_Font_small = ctk.CTkFont(family="Leelawadee", size=13)
fnt_Font_medium = ctk.CTkFont(family="Leelawadee", size=15, weight="bold")
fnt_Font_big = ctk.CTkFont(family="Leelawadee UI", size=25, weight="bold")

# Func get user input "Custom Resolution"
def open_input_dialog_event():
    dialog = ctk.CTkInputDialog(text="Type in your custom resolution: ", title="CUSTOM RESOLUTION")
    print("CTkInputDialog:", dialog.get_input())

# Packing three frames below each other
fre_Display = ctk.CTkFrame(master=window)
fre_Display.pack(pady=(15, 10))
fre_Sound = ctk.CTkFrame(master=window)
fre_Sound.pack(pady=(10, 5))
fre_Okcancel = ctk.CTkLabel(master=window, width=130)
fre_Okcancel.pack(pady=15)

# 1
#
# First Frame "Display"
lbl_Display = ctk.CTkLabel(fre_Display, text="Display", text_color="white")
lbl_Display.grid(row=0, column=0, pady=10, sticky="nsew", columnspan=2, padx=110)
lbl_Display.configure(font=fnt_Font_big)

lbl_Resolution = ctk.CTkLabel(fre_Display, text="Resolution")
lbl_Resolution.grid(row=1, column=0, pady=(5, 0), sticky="news")
lbl_Resolution.configure(font=fnt_Font_small)

opm_Resolution = ctk.CTkOptionMenu(fre_Display, values=["800x500", "720x1280", "1920x1080", "2180x3980", "..."], width=140)
opm_Resolution.grid(row=1, column=1, pady=(10, 5), padx=(0, 10), sticky="w")
opm_Resolution.set("1920x1080")
opm_Resolution.configure(font=fnt_Font_small)

# Labeled Radiobuttons
lbl_Border = ctk.CTkLabel(fre_Display, text="Window Mode")
lbl_Border.grid(row=2, column=0, sticky="news", columnspan=2, pady=(15, 0))
lbl_Border.configure(font=fnt_Font_medium)

rtn_Windowed = ctk.CTkRadioButton(fre_Display, variable=var_Winfull, value=1, text="Windowed")
rtn_Windowed.grid(row=3, column=0, sticky="news", padx=(40, 0), pady=(0, 15))
rtn_Windowed.configure(font=fnt_Font_small)

rtn_Fullscreen = ctk.CTkRadioButton(fre_Display, variable=var_Winfull, value=2, text="Fullscreen")
rtn_Fullscreen.grid(row=3, column=1, sticky="nes", padx=(0, 50), pady=(0, 15))
rtn_Fullscreen.configure(font=fnt_Font_small)

lbl_Fontname = ctk.CTkLabel(fre_Display, text="Font Name")
lbl_Fontname.grid(row=4, column=0, sticky="news", columnspan=2, pady=(15, 0))
lbl_Fontname.configure(font=fnt_Font_medium)

rtn_Fontname_default = ctk.CTkRadioButton(fre_Display, variable=var_Fontname, value=1, text="Default")
rtn_Fontname_default.grid(row=5, column=0, sticky="news", padx=(40, 0), pady=(0, 15))
rtn_Fontname_default.configure(font=fnt_Font_small)

rtn_Fontname_alternative = ctk.CTkRadioButton(fre_Display, variable=var_Fontname, value=2, text="Alternative")
rtn_Fontname_alternative.grid(row=5, column=1, sticky="nes", padx=(0, 50), pady=(0, 15))
rtn_Fontname_alternative.configure(font=fnt_Font_small)

lbl_Fontsize = ctk.CTkLabel(fre_Display, text="Font Size")
lbl_Fontsize.grid(row=6, column=0, sticky="news", columnspan=2, pady=(15, 0))
lbl_Fontsize.configure(font=fnt_Font_medium)

rtn_Fontsize_default = ctk.CTkRadioButton(fre_Display, variable=var_Fontsize, value=1, text="Default")
rtn_Fontsize_default.grid(row=7, column=0, sticky="news", padx=(40, 0), pady=(0, 15))
rtn_Fontsize_default.configure(font=fnt_Font_small)

rtn_Fontsize_big = ctk.CTkRadioButton(fre_Display, variable=var_Fontsize, value=2, text="Big")
rtn_Fontsize_big.grid(row=7, column=1, sticky="nes", padx=(0, 50), pady=(0, 15))
rtn_Fontsize_big.configure(font=fnt_Font_small)

# Vsync Switch
swt_Vsync = ctk.CTkSwitch(fre_Display, text="VSync")
swt_Vsync.grid(row=8, column=0, columnspan=2, sticky="news", padx=(100, 0), pady=(15, 25))

# 2
#
# Second Frame "Sound"
lbl_Sound = ctk.CTkLabel(fre_Sound, text="Sound", text_color="white")
lbl_Sound.grid(row=0, column=0, columnspan=2, pady=10, sticky="nsew", padx=115)
lbl_Sound.configure(font=fnt_Font_big)

lbl_Music = ctk.CTkLabel(fre_Sound, text="Music", width=70)
lbl_Music.grid(row=1, column=0, pady=5, padx=(15, 0))
lbl_Music.configure(font=fnt_Font_small)

lbl_Effects = ctk.CTkLabel(fre_Sound, text="Effects", width=70)
lbl_Effects.grid(row=2, column=0, pady=(0, 20), padx=(18, 0))
lbl_Effects.configure(font=fnt_Font_small)

sld_Music = ctk.CTkSlider(fre_Sound, from_=0, to=100, width=140)
sld_Music.grid(row=1, column=1, pady=10, padx=(10, 15))

sld_Effects = ctk.CTkSlider(fre_Sound, from_=0, to=100, width=140)
sld_Effects.grid(row=2, column=1, pady=(0, 20), padx=(10, 15))

# 3
#
# Third Frame "OK / CANCEL"
btn_Okay = ctk.CTkButton(fre_Okcancel, text="OK", width=110)
btn_Okay.grid(row=0, column=0, padx=(0, 15))

btn_Cancel = ctk.CTkButton(fre_Okcancel, text="CANCEL", width=110, command=quit)
btn_Cancel.grid(row=0, column=1, padx=(15, 0))


# Start Mainloop
window.mainloop()
