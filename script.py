if __name__ == "__main__":

    # pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu117
    # pip install matplotlib
    # pip install seaborn
    # pip install tqdm
    # pip install pyyaml
    # python -m PyInstaller script.py

    import torch
    import numpy as np
    import cv2
    from PIL import Image
    from PIL import ImageTk
    import threading
    import tkinter as tk
    from tkinter import PhotoImage
    import pandas as pd
    import random

    model = torch.hub.load('ultralytics/yolov5', 'custom', path='..//gesture_recognition/yolov5/runs/train/exp56/weights/best.pt', force_reload=True)


letter = ""
def random_letter():
    global letter
    letter = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    rand_label.config(text=letter)

def start_button_clicked(videoloop_stop):
    threading.Thread(target=videoLoop, args=(videoloop_stop,)).start()

def stop_button_clicked(videoloop_stop):
    videoloop_stop[0] = True

def show_image():
    popup = tk.Toplevel()
    popup.title("Letter Reference")

    image = PhotoImage(file="../gesture_recognition/images/letters.gif")
    label = tk.Label(popup, image=image)
    label.image = image
    label.pack()

def show_CS():
    desc = tk.Toplevel()
    desc.title("Sign Descriptions")
    label_6 = tk.Label(desc, text="Remember you're signing for the person in front of you, not for yoursel!")
    label_6.config(bg="#ca7ff2", font=("", 20))
    label_6.pack()
    label_1 = tk.Label(desc, text="All vowels correspond to each finger on your hand, starting with 'A' at the thumb and ending with 'U' at the pinky!")
    label_1.config(bg="#a9ebf4", font=("", 20))
    label_1.pack()
    label_2 = tk.Label(desc, text="'L', 'M', 'N', and 'V' all look similar and use the palm of your hand!")
    label_2.config(bg="#2acee3", font=("", 20))
    label_2.pack()
    label_3 = tk.Label(desc, text="The letter 'S' uses depth. Try different positions if you're struggling with this one!")
    label_3.config(bg="#a9ebf4", font=("", 20))
    label_3.pack()
    label_4 = tk.Label(desc, text="Interlace all of your fingers for 'W' while only crossing your two index fingures for 'X'!")
    label_4.config(bg="#2acee3", font=("", 20))
    label_4.pack()
    label_5 = tk.Label(desc, text="Some letters like 'P', 'C', and 'D' are meant to look like the way they're written!")
    label_5.config(bg="#a9ebf4", font=("", 20))
    label_5.pack()
    desc.config(bg = "#8d9ee9")
    desc.geometry("1500x200+0+0")

    
def videoLoop(mirror=False):
    cap = cv2.VideoCapture(2)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 700)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 450)

    while True:
        ret, frame = cap.read()
        results = model(frame)

        for i, row in results.pandas().xyxy[0].iterrows():
            name = (row['name']).upper()
            conf = (row['confidence'])
            if name == letter:
                if conf >= 0.5:
                    label1 = tk.Label(root, text=(name, "Well Done!"), bg="#63ca7b", font=("", 20))
                    label1.place(x=50, y=600, width=400, height=150)
                elif conf >= 0.3 and conf < 0.5:
                    label2 = tk.Label(root, text=(name, "Very Close"), bg="#95e576", font=("", 20))
                    label2.place(x=50, y=600, width=400, height=150)
                elif conf >= 0.1 and conf < 0.3:
                    label3 = tk.Label(root, text=(name, "Getting There"), bg = "#dee066", font=("", 20))
                    label3.place(x=50, y=600, width=400, height=150)
                elif conf < 0.1:
                    label4 = tk.Label(root, text=(name, "Needs Improvement!"), bg = "#fb5e54", font=("", 20))
                    label4.place(x=50, y=600, width=400, height=150)
            
        if mirror is True:
            frame = frame[:, ::-1]
            
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(image)
        image = ImageTk.PhotoImage(image)
        panel = tk.Label(image=image)
        panel.image = image
        panel.place(x=50, y=120)

        if videoloop_stop[0]:
            videoloop_stop[0] = False
            panel.destroy()
            cap.release()
            break


videoloop_stop = [False]

root = tk.Tk()
root.title("BSL Learning Tool")
root.config(bg = "#f3fecb")
root.geometry("1900x1080+0+0")

# display prompt for which letter to sign
rand_label = tk.Label(root, text=("A"), font=("", 40))
rand_label.config(bg="#f3fecb")
rand_label.pack()

# button to change the prompt letter 
letter_button = tk.Button(root, text="New Letter", command=random_letter)
letter_button.pack()

# button to display the image
img_button = tk.Button(root, text="Reference Image", bg="#fff", font=("", 15), command=show_image)
img_button.config(bg="#e2fc84")
img_button.place(x=1225, y=0, width=300, height=75)

# button to show how to do the signs
img_button = tk.Button(root, text="Cheat Sheet", bg="#fff", font=("", 15), command=show_CS)
img_button.config(bg="#e2fc84")
img_button.place(x=1225, y=90, width=300, height=75)

# button to start the camera
start_button = tk.Button(root, text="Start Camera", bg="#fff", font=("", 25),command=lambda: start_button_clicked(videoloop_stop))
start_button.place(x=1200, y=500, width=300, height=75)
start_button.config(bg="#fc3532")

# button to stop the camera (at that frame)
stop_button = tk.Button(root, text="Freeze Frame", bg="#fff", font=("", 25),command=lambda: stop_button_clicked(videoloop_stop))
stop_button.place(x=1200, y=650, width=300, height=75)
stop_button.config(bg="#3b95c4")


root.mainloop()