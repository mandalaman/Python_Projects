import os

def createIfNotExist(folder):
    if not os.path.exists("others"):
        os.makedirs("others")

def move(foldername, files):
    for file in files:
        os.replace(file, f"{foldername}/{file}")

files = os.listdir()
files.remove("main.py")
print(files)
createIfNotExist("Images")
createIfNotExist("Docs")
createIfNotExist("Media")
createIfNotExist("others")

imaExts = [".png", ".jpge"]
images = [file for file in files if os.path.splitext(file)[1].lower() in imaExts]

docExts = [".txt", ".pdf"]
docs = [file for file in files if os.path.splitext(file)[1].lower() in docExts]

mediaExts = [".mp4", ".mp3"]
medias = [file for file in files if os.path.splitext(file)[1].lower() in mediaExts]

others = []
for file in files:
    ext = os.path.splitext(file)[1].lower()
    if (ext not in mediaExts) and (ext not in docExts) and (ext not in imaExts):
        others.append(file)


move("Images", images)
move("Docs", docs)
move("Media", medias)
move("Others", others)