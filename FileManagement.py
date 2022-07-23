import os


class FileManagement:
    path = []
    folderQueue = []

    def __init__(self, p):
        self.folderQueue.append(p)
        while len(self.folderQueue) != 0:
            folder = self.folderQueue.pop()
            for fileOrDirectory in os.listdir(folder):
                f = os.path.join(folder, fileOrDirectory)
                if os.path.isdir(f):
                    self.folderQueue.append(f)
                else:
                    self.path.append(f)

    def getPDFList(self):
        PDFList = []
        for i in range(len(self.path)):
            if self.path[i].endswith(".pdf"):
                PDFList.append(self.path[i])
        return PDFList

    def getDOCXList(self):
        DOCXList = []
        for i in range(len(self.path)):
            if self.path[i].endswith(".docx"):
                DOCXList.append(self.path[i])
        return DOCXList

    def getIMGList(self):
        IMGList = []
        suffixes = (".png", ".jpg", ".jpeg", ".bmp", ".eps", ".raw", ".cr2", ".nef", ".orf", ".sr2")
        for i in range(len(self.path)):
            if self.path[i].endswith(suffixes):
                IMGList.append(self.path[i])
        return IMGList

    def getTXTList(self):
        TXTList = []
        for i in range(len(self.path)):
            if self.path[i].endswith(".txt"):
                TXTList.append(self.path[i])
        return TXTList

    def getVIDEOList(self):
        VIDEOList = []
        suffixes = (".mp4", ".mov", ".wmv", ".avi", ".webm", ".avi", ".flv", ".mkv", ".mpeg4",".gif")
        for i in range(len(self.path)):
            if self.path[i].endswith(suffixes):
                VIDEOList.append(self.path[i])
        return VIDEOList

    def getCSVList(self):
        CSVList = []
        for i in range(len(self.path)):
            if self.path[i].endswith(".csv"):
                CSVList.append(self.path[i])
        return CSVList

    def getXlSXList(self):
        XlSXList = []
        for i in range(len(self.path)):
            if self.path[i].endswith(".xlsx"):
                XlSXList.append(self.path[i])
        return XlSXList




if __name__ == '__main__':
    pathOfBackupFolder = input("Enter the path of the directory that has to be backed up")
    obj = FileManagement(pathOfBackupFolder)
    PDFpath = []
    PDFpath = obj.getPDFList()
    for i in range(len(PDFpath)):
        print(PDFpath[i])
