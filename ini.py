import subprocess
import os
subprocess.run(["git","init"])
with open(os.getcwd() + "\README.md","w+") as file:
    file.write("### Title"+"\n"+"---")    
subprocess.run(["git","add","."])
subprocess.run(["git","commit","-m","Initial commit"])
subprocess.run(["git","remote","add","origin",input("Give Your GitHub Link")])
subprocess.run(["git","push","-u","origin","master"])