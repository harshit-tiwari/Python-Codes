# Python-Codes

A Python module to copy files

Save this as copyModule.py
Then import the module copyModule in python shell
Then type copyModule.copyFile()  and the rest will follow

def copyFile():
    import os
    sourceFileName = input("Enter the source file name: ")
    targetFileName = input("Enter the target file name: ")

    print("Does source file exists : %s"% os.path.isfile(sourceFileName))
    print("Does target file exists : %s"% os.path.isfile(targetFileName))

    openSource = open(sourceFileName)
    print("The length of the source file is : %s"% len(sourceFileName))
    sourceContents = openSource.read()
    openSource.close()

    openTarget = open(targetFileName, 'w')
    openTarget.write(sourceContents)
    openTarget.close()
    print("=========File Coying in progress==========")
    if os.path.isfile(targetFileName) == False:
       print("The target file was not created in the directory")
    else:
       sourceLength = len(sourceFileName)
       targetLength = len(targetFileName)
       if sourceLength == targetLength:
          print("The file copy was successful ")
       else:
          print("The length of the source file is : %s"% sourceLength)
          print("The length of the target file is : %s"% targetLength)
          print("The target file was created but contents are not properly copied") 


