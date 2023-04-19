import os
import shutil
os.chdir(r'C:\Users\chach\Desktop\Project\2023\overwatchAI\dataset2\images\train')
for i,f in enumerate(os.listdir()):
    print(f)
    if i%5 == 0:
        shutil.move(f, r"C:\Users\chach\Desktop\Project\2023\overwatchAI\dataset2\images\val"+"\\"+f)