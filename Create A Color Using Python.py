from PIL import Image as I #importing libraries
a = int(input("Enter the first RGB value. "))
b = int(input("Enter the second RGB value. "))
c = int(input("Enter the last RGB value. "))
color = (a, b, c) #What color u want to use in RGB format
width, height = 500, 500 #Defining the images structure
image = I.new("RGB", (width, height), color) #Creating the image
image.save("colored_image.png") #Saving the image as "colored_image.png"
image.show() #Opens a window to show the image *OPTIONAL* add a "#" behind image if u dont want it to appear 
Image_path = r"C:\Users\hp\AppData\Local\Temp\wct1E64.tmp" #To show where the image is stored

#46, 0, 253 for the good blue color