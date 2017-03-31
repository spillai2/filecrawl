import os

rootDir = '/home/san/Pictures'

for dirName, subdirList, fileList in os.walk(rootDir):
	for fname in fileList:
		filePath = os.path.join(dirName,fname);
		if fname.lower().endswith('.jpg' or '.jpeg' or '.png'):
			print(filePath)
