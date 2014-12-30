from distutils.core import setup 

import py2exe 

setup(windows=["login.pyw"],
      data_files=[("img",
                   [r"G:\main match\about.png",
                    r"G:\main match\count.png",
                    r"G:\main match\count1.png",
                    r"G:\main match\del.png",
                    r"G:\main match\help.png",
                    r"G:\main match\login.bmp",
                    r"G:\main match\open.png",
                    r"G:\main match\out.png",
                    r"G:\main match\save.png",
                    r"G:\main match\static.png",
                    r"G:\main match\title3.png",
                    r"G:\main match\two.jpg",
                    r"G:\main match\del_local.png"]),
                  ("bat",
                   [r"G:\main match\del.bat",
                    r"G:\main match\del_local.bat",
                    r"G:\main match\read.bat",
                    r"G:\main match\start.bat"]),]) 
 

 

 

 

 



