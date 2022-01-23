import cv2
import numpy as np
import matplotlib.pyplot as plt
class user:
    def __init__(self) -> None:
        print("This is a Project of Image Processing Using Open Cv , Numpy (Kernel Matrix) , MatplotLib")
        self.user = input("Enter Your Name :")
        print("Welcome : "+self.user)
        self.main()
    #Main Function :
    def main(self):
        print("Choice : 1 Identity Image 2 Edge Detection 3 Sharpening Image 4 Smoothing Image 5 Auto Sharpning & Smoothing")
        option = input("Enter Your Choice : ").capitalize()
        #If Image is Missing then we are ready to handle error
        try :
            #put Your Image Location Here 
            '''
            Alternate 
            import os
            path = 'C:/Users/Lenovo/AppData/Local/Programs/Python/Python39/opencv'
            cv2.imread(os.path.join(path , 'orange.jpg'), img)
            '''
            img = cv2.imread('C://Users//Lenovo//Downloads//orange.jpg')
            self.realimg = img
            #Coditional Block Start
            if option == "1" or option == "Identity Image":
                print("Your Choice is Identity Image : ")
                opt = input("Would you like to see Brighten Image : 1:Yes | 2:No : ").capitalize()
                #Nesting of if Statement
                if opt == "1" or opt == "Yes":
                    self.bright(img)
                else :
                    k=np.array([[0,0,0],[0,1,0],[0,0,0]])
                    self.image("Identity Image",k,img)
            elif option == "2" or  option =="Edge Detection":
                print("Your Choice is Edge Detection : ")
                self.edge(img)
            elif option == "3" or  option =="Sharpening Image":
                print("Your Choice is Sharpening Image : ")
                self.level(img)
            elif option == "4" or  option =="Smoothing Image":
                print("Your Choice is Smoothing Image : ")
                self.smooth(img)
            elif option == "5" or option == "Auto Sharpening & Smoothing to the same image":
                print("Your Choice is Both Sharpening & Smoothing")
                k=np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])
                k2 =np.array([[1,2,1],[2,4,2],[1,2,1]])/16
                new_img = cv2.filter2D(img,ddepth=-1,kernel=k)
                self.image("Both Sharpening & Smoothing",k2,new_img)
            else :
                print("Wrong Input Please Try Again : ")
                self.main()
            #Conditional Block End
        #Error Handling
        except Exception as err :
            print(err)
    def level(self,img):
        intensity = int(input("Enter Level of Intensity from 1-5 : "))
        if intensity == 1 :
            k=np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
            self.image("Sharpening Image",k,img)
        elif intensity == 2:
            k=np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])
            self.image("Sharpening Image",k,img)
        elif intensity == 3 :
            k=np.array([[-1, -2, -3], [-1, 13, -1], [-2, -1, -1]])
            self.image("Sharpening Image",k,img)
        elif intensity == 4 :
            k=np.array([[0,0,-1,0,0],[0,-1,-2,-1,0],[-1,-2,17,-2,-1],[0,-1,-2,-1,0],[0,0,-1,0,0]])
            self.image("Sharpening Image",k,img)
        elif intensity == 5 :
            k=np.array([[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,25,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1]])
            self.image("Sharpening Image",k,img)
        else :
            print("Wrong Input Please Try Again:")
            #Recurssion
            self.level(img)
    def edge(self,img):
        intensity = input("Enter the Edge Detection level : 1:Low 2:Mid 3:High ").capitalize()
        if intensity == "1" or intensity == "Low":
            k=np.array([[0,-1,0],[0,2,0],[0,-1,0]])
            self.image("Edge Detection",k,img)
        elif intensity == "2" or intensity == "Mid":
            k=np.array([[0,-1,0],[-1,4,-1],[0,-1,0]])
            self.image("Edge Detection",k,img)
        elif intensity == "3" or intensity == "High":
            k=np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])
            self.image("Edge Detection",k,img)
        else :
            print("Wrong Input Please Try Again")
            self.edge(img)
    def bright(self,img):
        intensity = input("Enter Intensity Level : 1:Low 2:Mid 3:High : ").capitalize()
        if intensity == "1" or intensity == "Low":
            k=np.array([[0,0,0],[0,1.25,0],[0,0,0]])
            self.image("Brighten Image",k,img)
        elif intensity == "2" or intensity == "Mid":
            k=np.array([[0,0,0],[0,1.5,0],[0,0,0]])
            self.image("Brighten Image",k,img)
        elif intensity == "3" or intensity == "High":
            k=np.array([[0,0,0],[0,2,0],[0,0,0]])
            self.image("Brighten Image",k,img)
    def smooth(self,img):
        shopt = input("Enter Type of Smoothing : 1 Box | 2 Gaussian Blur :").capitalize()
        if shopt == "Box" or shopt == "1" :
            print("Your Choice is Box Smoothing Image : ")
            k=np.array([[1,1,1],[1,1,1],[1,1,1]])/9
            self.image("Smoothing",k,img)
        elif shopt == "Gaussian Blur" or shopt == "2":
            print("Your Choice is Gaussian Smoothing Image : ")
            self.gaussian(img)
        else :
            print("Wrong Input Please Try Again : ")
            self.smooth(img)
    def gaussian(self,img):
        intensity = input("Enter the Edge Detection level : 1:Low 2:Mid 3:High(Unsharp masking) ").capitalize()
        if intensity == "1" or intensity == "Low":
            k=np.array([[1,2,1],[2,4,2],[1,2,1]])/16
            self.image("Gaussian Smoothing",k,img)
        elif intensity == "2" or intensity == "Mid":
            k=np.array([[1,4,6,4,1],[4,16,24,16,4],[6,24,36,24,6],[4,16,24,16,4],[1,4,6,4,1]])/256
            self.image("Gaussian Smoothing",k,img)
        elif intensity == "3" or intensity == "High":
            k=np.array([[1,4,6,4,1],[4,16,24,16,4],[6,24,-476,24,6],[4,16,24,16,4],[1,4,6,4,1]])/-256
            self.image("Unsharp masking ",k,img)
    #Polymorphism Example
    def image(self,info,k,img):
        new_img = cv2.filter2D(img,ddepth=-1,kernel=k)
        self.show(info,new_img)
    #Showing Images in Pyplot
    def show(self,var,outimg):
        self.realimg = cv2.cvtColor(self.realimg,cv2.COLOR_BGR2RGB)
        new_img = cv2.cvtColor(outimg,cv2.COLOR_BGR2RGB)
        titles = ["Original Image",var]
        images = [self.realimg,new_img]
        for i in range(2):
            plt.subplot(1,2,i+1),plt.imshow(images[i])
            plt.title(titles[i])
        plt.show()
        self.last()
    #Ending Credit
    def last(self):
        last = input("Would you like to try more : Yes | No : ").capitalize()
        if last == "Yes":
            self.main()
        else :
            print("Thanks "+self.user+" for Using My Application please Give Your Feedback")
            try :
                view = input("Please Type Your View : ")
                print("Your View has been Registered Sucessfully "+view)
                print("This Project is Made By Shubham Tiwari")
                print("All Rights Are Reserved By TNE 2021")
                pint = input("Have You Liked My Application : ")
                print(".......See You Soon.......")
            except :
                print("Your Point of View hasn't been Registered")
obj = user
obj()

