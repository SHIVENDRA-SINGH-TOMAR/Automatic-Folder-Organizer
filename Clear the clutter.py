import os

def createIfNotExist(folder):
    if folder not in files:
        os.makedirs(folder)

def move(foldername, files):
    for file in files:
        os.replace(file, f"{foldername}/{file}")

files = os.listdir()
files.remove("main.py")

createIfNotExist("Apps")
createIfNotExist("Audios")
createIfNotExist("Compressed files")
createIfNotExist("C++ files")
createIfNotExist("Documents")
createIfNotExist("Images")
createIfNotExist("pdfs")
createIfNotExist("Python files")
createIfNotExist("Web Pages")
createIfNotExist("Videos")
createIfNotExist("Others")

imgExt = [".jpg", ".png", ".jpeg", ".jfif", ".gif"]
images = [file for file in files if os.path.splitext(file)[1].lower() in imgExt]

docsExt = [".doc", ".docx", ".txt", ".dotx", ".odt"]
docs = [file for file in files if os.path.splitext(file)[1].lower() in docsExt]

audExt = [".mp3", ".wav", ".wma", ".aac", ".ogg"]
audios = [file for file in files if os.path.splitext(file)[1].lower() in audExt]

vidExt = [".mp4", ".wma", ".webm", ".avi", ".mkv", ".mpeg"]
videos = [file for file in files if os.path.splitext(file)[1].lower() in vidExt]

pdfExt = [".pdf"]
pdfs = [file for file in files if os.path.splitext(file)[1].lower() in pdfExt]

webExt = [".html", ".xml", ".htm", ".mht", ".mhtml"]
webs = [file for file in files if os.path.splitext(file)[1].lower() in webExt]

pyExt = [".py"]
pythons = [file for file in files if os.path.splitext(file)[1].lower() in pyExt]

cppExt = [".cpp"]
cpps = [file for file in files if os.path.splitext(file)[1].lower() in cppExt]

comExt = [".zip", ".rar", ".7z", ".arj"]
comps = [file for file in files if os.path.splitext(file)[1].lower() in comExt]

exeExt = [".exe"]
exes = [file for file in files if os.path.splitext(file)[1].lower() in exeExt]

others = []
for file in files:
    ext = os.path.splitext(file)[1].lower()
    if (ext not in imgExt)  and (ext not in audExt) and (ext not in vidExt) and (ext not in docsExt) and (ext not in pdfExt) and (ext not in webExt) and (ext not in pyExt) and (ext not in cppExt)  and os.path.isfile(file):
        others.append(file) 

move("Images", images)
move("Audios", audios)
move("Videos", videos)
move("Documents", docs)
move("pdfs", pdfs)
move("Web pages", webs)
move("Python files", pythons)
move("C++ files", cpps)
move("Compressed files", comps)
move("Apps", exes)
move("Others", others)

