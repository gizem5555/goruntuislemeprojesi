import tkinter as tk
from PIL import Image, ImageTk, ImageDraw
import os

def view_profile(master_window, user_name, db_path):
    profile = tk.Toplevel(master_window)
    profile.title("👤 Profil")
    profile.geometry("400x600")
    profile.configure(bg="#f7f7f7")  

  
    label = tk.Label(profile, text=f"🧑 {user_name}", font=("Arial", 24, "bold"), bg="#f7f7f7", fg="#333333")
    label.pack(pady=20)

    
    user_img_path = os.path.join(db_path, f"{user_name}.jpg")
    if os.path.exists(user_img_path):
        user_img = Image.open(user_img_path)
        user_img = user_img.resize((160, 160)) 
        user_img = user_img.convert("RGBA")

        
        circle = Image.new("L", user_img.size, 0)
        draw = ImageDraw.Draw(circle)
        draw.ellipse((0, 0, user_img.size[0], user_img.size[1]), fill=255)
        user_img.putalpha(circle)

        user_img = ImageTk.PhotoImage(user_img)
        img_label = tk.Label(profile, image=user_img, bg="#f7f7f7", bd=0, relief="flat")
        img_label.image = user_img  
        img_label.pack(pady=25)

   
    name_label = tk.Label(profile, text=f"@{user_name}", font=("Arial", 18), bg="#f7f7f7", fg="#333333")
    name_label.pack(pady=10)

 
    edit_button = tk.Button(profile, text="✏️ Profili Düzenle", font=("Arial", 14), bg="#0095F6", fg="white", relief="flat", bd=0,
                            activebackground="#006DB6", activeforeground="white", height=2, width=18, 
                            padx=10, pady=5, command=lambda: edit_profile(user_name, db_path))
    edit_button.pack(pady=20)

   
    logout_button = tk.Button(profile, text="🔒 Çıkış Yap", font=("Arial", 14), bg="#F44336", fg="white", relief="flat", bd=0,
                              activebackground="#D32F2F", activeforeground="white", height=2, width=18, 
                              padx=10, pady=5, command=profile.destroy)
    logout_button.pack(pady=10)

def edit_profile(user_name, db_path):
 
    print(f"{user_name}'ın profilini düzenleme sayfası açılacak.")







