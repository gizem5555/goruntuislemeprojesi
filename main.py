import tkinter as tk
from tkinter import messagebox, simpledialog
import cv2
from deepface import DeepFace
import os
from PIL import Image, ImageTk
from profile_view import view_profile  

# Veritabanı klasörü
DB_PATH = "faces_db"

# Ana pencere
window = tk.Tk()
window.title("🧠 Yüz Tanıma ile Giriş")
window.geometry("400x650")
window.configure(bg="#2c3e50")

title = tk.Label(window, text="🧠 Yüz Tanıma Sistemi", font=("Helvetica", 22, "bold"), bg="#2c3e50", fg="white")
title.pack(pady=20)

description = tk.Label(window, text="📷 Kameranızı açarak giriş yapın veya kayıt olun", font=("Helvetica", 12), bg="#2c3e50", fg="white")
description.pack(pady=10)

# Kamera ön izleme alanı
camera_label = tk.Label(window, bg="#ecf0f1", width=300, height=300, bd=10, relief="sunken")
camera_label.pack(pady=10)

def update_camera_preview():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame)
        img = img.resize((300, 300))
        imgtk = ImageTk.PhotoImage(image=img)
        camera_label.imgtk = imgtk
        camera_label.configure(image=imgtk)
    window.after(1000, update_camera_preview)

def register_user():
    name = simpledialog.askstring("📝 Kayıt", "Adınızı girin:")
    if name:
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        cap.release()
        if ret:
            os.makedirs(DB_PATH, exist_ok=True)
            save_path = os.path.join(DB_PATH, f"{name}.jpg")
            cv2.imwrite(save_path, frame)
            messagebox.showinfo("✔️ Kayıt Başarılı", f"{name} sisteme kaydedildi.")
        else:
            messagebox.showerror("❌ Hata", "Kayıt için görüntü alınamadı.")
    else:
        messagebox.showwarning("İptal", "Kayıt işlemi iptal edildi.")

def capture_and_verify():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()
    if not ret:
        messagebox.showerror("❌ Hata", "Kameradan görüntü alınamadı.")
        return

    img_path = "temp.jpg"
    cv2.imwrite(img_path, frame)

    try:
        if not any(fname.endswith('.jpg') or fname.endswith('.png') for fname in os.listdir(DB_PATH)):
            messagebox.showinfo("📁 Bilgi", "Veritabanı boş. Önce kayıt olun.")
            register_user()
            return

        results = DeepFace.find(img_path, db_path=DB_PATH, enforce_detection=False)

        if results and len(results[0]) > 0:
            best_match = results[0].iloc[0]
            user_name = os.path.basename(best_match["identity"]).split(".")[0]
            distance = best_match["distance"]

            if distance < 0.4:
                messagebox.showinfo("🎉 Giriş Başarılı", f"Hoşgeldin, {user_name}!")
                show_dashboard(user_name)
            else:
                messagebox.showwarning("🛑 Giriş Reddedildi", "Bu yüz tanınamadı. Kayıt olmayı deneyin.")
        else:
            messagebox.showinfo("❓ Bilinmeyen", "Hiçbir eşleşme bulunamadı.")
            register_user()
    except Exception as e:
        messagebox.showerror("⚠️ Hata", f"Tanıma sırasında bir hata oluştu:\n{e}")

def show_dashboard(user_name):
    dash = tk.Toplevel(window)
    dash.title("📋 Giriş Paneli")
    dash.geometry("400x400")
    dash.configure(bg="#f5f5f5")

    msg = tk.Label(dash, text=f"👋 Hoşgeldin, {user_name}!", font=("Helvetica", 18, "bold"), bg="#f5f5f5", fg="#2c3e50")
    msg.pack(pady=30)

    profile_btn = tk.Button(dash, text="👤 Profilim", font=("Helvetica", 14), bg="#2980b9", fg="white",
                            command=lambda: view_profile(window, user_name, DB_PATH), relief="raised", bd=4)
    profile_btn.pack(pady=10, fill="x", padx=40)

    logout_btn = tk.Button(dash, text="🔓 Çıkış Yap", font=("Helvetica", 14), bg="#e74c3c", fg="white", command=dash.destroy, relief="raised", bd=4)
    logout_btn.pack(pady=10, fill="x", padx=40)

# Ana ekrandaki butonlar
tk.Button(window, text="🔐 GİRİŞ YAP", font=("Helvetica", 14), bg="#27ae60", fg="white", command=capture_and_verify, relief="raised", bd=4).pack(pady=10, fill="x", padx=40)
tk.Button(window, text="📝 KAYIT OL", font=("Helvetica", 14), bg="#f39c12", fg="white", command=register_user, relief="raised", bd=4).pack(pady=10, fill="x", padx=40)
tk.Button(window, text="🚪 ÇIKIŞ", font=("Helvetica", 12), bg="#7f8c8d", fg="white", command=window.quit, relief="raised", bd=2).pack(pady=10, fill="x", padx=40)

update_camera_preview()
window.mainloop()






