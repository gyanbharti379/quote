import tkinter
import requests
from PIL import Image,ImageTk

class Quotes:
    def __init__(self):

        self.count = 1

# ----------------------------Area for creating window --------------------------------------------#

        self.master = tkinter.Tk()
        self.master.title("Quotes App")
        self.master.geometry("1470x750+10+10")
        self.master.resizable(False, False)

# ----------------------------Area for creating window -------------------END-------------------------#

# -------------------Area for widget to display on the window----------------------------------------#

# ---------------Area for Left Frame ---------------------------#

        self.left_frame = tkinter.Frame(self.master, width=400, height=740, background="#a84fdb")
        self.left_frame.place(x=10, y=0)

        self.title_Label = tkinter.Label(self.left_frame, text="." * 22 + "Quotes Book" + "." * 23, bg="#a84fdb",
                                         font=("bookman old style", 15), fg="black")
        self.title_Label.place(x=10, y=20)

        self.canvas = tkinter.Canvas(self.left_frame, width=375, height=290)
        self.canvas.place(x=10,y=70)

        self.img = Image.open("Image/before_img.jpg").resize((380, 290), Image.BOX)
        self.img_now = ImageTk.PhotoImage(self.img)

        self.canvas.create_image(190,147,image=self.img_now)

        self.Date_Label = tkinter.Label(self.left_frame, text="Date:", font=("bookman old style", 15),
                                                 bg="#a84fdb")
        self.Date_Label.place(x=10, y=380)

        self.author_Name_Label = tkinter.Label(self.left_frame, text="Author Name:", bg="#a84fdb",
                                             font=("bookman old style", 15))
        self.author_Name_Label.place(x=10, y=420)

# ---------------Area for Left Frame ------------END---------------#

# ---------------Area for Right Frame ----------------------------------------#

        self.right_frame = tkinter.Frame(self.master, width=1050, height=740, background="#f4a3e1")
        self.right_frame.place(x=410, y=0)

        self.title_Label = tkinter.Label(self.right_frame, text="-" * 21 + "Daily Quotes" + "-" * 22, bg="#f4a3e1",
                                         fg="#6d3e3c", font=("bookman old style", 30))
        self.title_Label.place(x=10, y=20)

        self.textArea = tkinter.Text(self.right_frame, font=("bookman old style",15), width=85, height=26)
        self.textArea.place(x=10, y=70)

        self.nextbtn = tkinter.Button(self.right_frame, text="Next",
                                      font=("bookman old style",15),
                                      width=50, command=self.insertdata
                                      )
        self.nextbtn.place(x=200, y=685)

# ---------------Area for Right Frame --------------------END------------------#

        self.master.mainloop()

# -------------------Area for widget to display on the window-----------------------END-----------------#

# --------------------------Area for all Methods used in the requirements ---------------------------------#

    def fetch_random_quate_freeapi(self):
        url = "https://api.freeapi.app/api/v1/public/quotes?page=1&limit=10&query=human"
        response = requests.get(url)
        all_data = response.json()

        if all_data["success"] and "data" in all_data:
            data = all_data["data"]["data"]

            return data


    def insertdata(self):

        lines = []
        lines.clear()

        data = self.fetch_random_quate_freeapi()

        self.img = Image.open("Image/after_img.jpg").resize((430, 290), Image.BOX)
        self.img_now = ImageTk.PhotoImage(self.img)
        self.canvas.create_image(190, 147, image=self.img_now)

        for i in range(0, len(data)):

            author_name = data[i]["author"]
            self.author_Name_Label.config(text="Author Name: "+author_name)

            content = data[i]["content"]
            lines.append(data[i]["content"])
            dataAdded = data[i]["dateAdded"]
            self.Date_Label.config(text="Date: "+dataAdded)

            message = f"{self.count}. Author Name: {author_name}\nContent: {content}\nDate: {dataAdded}\n\n"

            self.textArea.insert(tkinter.END,message)
            self.count +=1

# --------------------take last line of code and display in the image in the left frame ----------------------#
        len1 = lines[4]
        length = 30
        y = 120
        line = [len1[i:i + length] for i in range(0, len(len1), length)]

        for i in range(0, len(line)):
            self.canvas.create_text(185, y, text=""+line[i]+"\n", font=("bookman old style", 15))
            y += 40
# --------------------take last line of code and display in the image in the left frame ------------End-----------#

if __name__=="__main__":
      Quotes()