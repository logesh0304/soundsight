from tkinter import *
from tkinter import filedialog as fd
from PIL import ImageTk, Image
import cv2
import pyttsx3
import objectdetector
import threading

engine=pyttsx3.init()
img_path='dog.jpg'

def upload():
    global img_path
    img_path=fd.askopenfile().name
    setImage(img_path)

def setImage(path):
    img=Image.open(path)
    img=img.resize((400,300))
    img_data=ImageTk.PhotoImage(img)
    imgscr.config(image=img_data)
    imgscr.image=img_data    

def speak(text):
    engine.say(text)
    engine.runAndWait()

def updatePrompt(text):
    prompt.delete('1.0', 'end')
    prompt.insert('end', text)
    threading.Thread(target=speak, args=(text,)).start()

def generateText():
    updatePrompt(objectdetector.detectandgenerate(img_path))

root=Tk()
root.title("Sound sight")
root.geometry("600x600")

btn_upload=Button(root, text="Upload", command=upload)
btn_startcam=Button(root, text="Start camera")
btn_capture=Button(root, text="Capture")
btn_gentext=Button(root, text="Generate", command=generateText)

btn_upload.place(x=450,y=10)
btn_startcam.place(x=450,y=50)
btn_capture.place(x=450,y=90)
btn_gentext.place(x=450,y=130)

imgscr=Label(root, width=400, height=300)
imgscr.place(x=10, y=10)

prompt=Text(root, width=80, height=5)
prompt.config(padx=10, pady=10)
#prompt.config(state=DISABLED)
prompt.place(x=10, y=320)

#updatePrompt("Hello world")
setImage(img_path)

#btn_upload.place(x=400, y=40)
#cap= cv2.VideoCapture(0)


# Define function to show frame
'''
def show_frames():
   # Get the latest frame and convert into Image
   cv2image= cv2.cvtColor(cap.read()[1],cv2.COLOR_BGR2RGB)
   img = Image.fromarray(cv2image)
   # Convert image to PhotoImage
   imgtk = ImageTk.PhotoImage(image = img)
   label.imgtk = imgtk
   label.configure(image=imgtk)
'''

#show_frames()
root.mainloop()
