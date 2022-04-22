import os

path = "C:/Users/Hamidreza/Desktop/test"

dir_list = os.listdir(path)

print("-----------------------------------------")

print("Files and directories in '", path, "' :")

print(dir_list)

for i in range(0, 107):

     f = open(dir_list[i] , "r")
     print(f)
     firstline = f.readline()
     abnew = firstline.replace('-1' , '0' , 1)
     with open(dir_list[i] , "w") as f:
         f.write(abnew)