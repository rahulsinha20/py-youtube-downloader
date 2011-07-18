from distutils.core import setup
import py2exe
import os
#IMP - Place YouTubeDownloaderApp.py in the same directory as this file (FOR CURRENT BUILD, Place it above <youtube> package)
#This is added to support tree import: http://www.py2exe.org/index.cgi/data_files, http://www.py2exe.org/old/, http://objectmix.com/python/115674-py2exe-distutils-how-include-tree-files.html
#Add more resources in the line below as added, these are data files which
# are put in the dist folder, also notice we create an empty Log folder as shown below

#Include configuration.xml - for test
#Mydata_files = [('Resources',['./youtube/Resources/configuration.xml']),('Resources',['./youtube/Resources/DefaultWebKitImage.png']),('Resources',['./youtube/Resources/splash.jpg']),('Logs',[]),('Resources',['./youtube/Resources/app.ico','./youtube/Resources/youtube.jpg','./youtube/Resources/AboutLogo.png','./youtube/Resources/console.gif','./youtube/Resources/directVideoLink.gif','./youtube/Resources/folder.gif','./youtube/Resources/root.gif','./youtube/Resources/song.gif','./youtube/Resources/wait.gif'])]
#Exclude configuration.xml - for build
Mydata_files = [('Resources', ['./youtube/Resources/DefaultWebKitImage.png']), ('Resources', ['./youtube/Resources/splash.jpg']), ('Logs', []), ('Resources', ['./youtube/Resources/app.ico', './youtube/Resources/youtube.jpg', './youtube/Resources/AboutLogo.png', './youtube/Resources/console.gif', './youtube/Resources/directVideoLink.gif', './youtube/Resources/folder.gif', './youtube/Resources/root.gif', './youtube/Resources/song.gif', './youtube/Resources/wait.gif'])]

setup(windows=[{"script" : "YouTubeDownloaderApp.py"}], data_files=Mydata_files, options={"py2exe" : {"includes" : ["sip", "PyQt4", "PyQt4.QtNetwork"], "dll_excludes":["MSVCP90.dll"]}})
# Problems with PyQt 4.7 and Python 27
# Refer to http://old.nabble.com/Problems-using-PyQt-4.7-and-py2exe-td27451823.html
# Override the function in py2exe to determine if a dll should be included
dllList = ('mfc90.dll', 'msvcp90.dll', 'qtnetwork.pyd', 'qtxmlpatterns4.dll', 'qtsvg4.dll')
origIsSystemDLL = py2exe.build_exe.isSystemDLL
def isSystemDLL(pathname):
    if os.path.basename(pathname).lower() in dllList:
        return 0
    return origIsSystemDLL(pathname)
py2exe.build_exe.isSystemDLL = isSystemDLL
