from AbstractiveSummary import AbstractiveSummarizer
from FileManagement import FileManagement
from CodeConverter import FileConverter
from ImageClassification import ImageClassifier
from KeybertExtractor import KWE
from PIIData import PiiData
from VideoClassification import VC


# takes the file path and returns all the data ML in a list in the format,[<path of file>,<Abstactive Summary>,<keywords>,<PII data>,< img/video tags>,]
class MLData:
    path = ""
    tessaractFilePath = ""
    piiDataTagsFilePath = ""
    objectClassificationConfigPath=""
    frozenModelPath=""

    def __init__(self, p, tessaract,pii,classification,frozen):
        self.path = p
        self.tessaractFileLocation = tessaract
        self.piiDataTagsFilePath = pii
        self.imageClassificationConfigPath=classification
        self.frozenModelPath=frozen

    def getMlData(self):
        list = []
        list.append(self.path)
        cc = FileConverter(self.Path, self.tessaractFileLocation)
        txtableSuffixes = (
        ".pdf", ".docx", "xlsx", ".csv", ".pdf", ".jpg", ".png", ".gif", ".jpeg", ".raw", ".cr2", ".nef", ".orf",
        ".sr2")
        imgSuffixes = (".jpg", ".png", ".gif", ".jpeg", ".raw", ".cr2", ".nef", ".orf", ".sr2")
        vidSuffixes = (".mp4", ".mov", ".wmv", ".avi", ".webm", ".avi", ".flv", ".mkv", ".mpeg4", ".gif")
        if self.path.endswith(txtableSuffixes):
            txtstr = cc.convert_tostr()
            asry = AbstractiveSummarizer(txtstr)  # abstractive summary
            list.append(asry.getSummary())
            kwrd = KWE(txtstr)
            list.append(kwrd.keywordExtract())  # keywords
            pdta = PiiData(txtstr, self.piiDataTagsFilePath)
            list.append(pdta.match_query_21())  # PII data result , can be low,medium, high or very high

        elif self.path.endswith(imgSuffixes):
            imgc = ImageClassifier(self.path,self.objectClassificationConfigPath,self.frozenModelPath )
            list.append(imgc.classify())

        elif self.path.endswith(vidSuffixes):
            vidc=VC(self.path,self.objectClassificationConfigPath,self.frozenModelPath )
            list.append((vidc.classify()))
        return list




if __name__ == '__main__':
    backupPath = input("Enter the path of the directory that has to backed up")
    tessaractFilePath = input("Enter the location of the tesseract executable")
    piiDataTagsFilePath=input("Enter the location of the PII data tags file")
    objectClassificationConfigFilePath=input("Enter the path of image classification config file")
    frozenModelFilePath=input("Enter the path of the frozen model")
    fm = FileManagement(backupPath)
    filePaths=fm.getPathList()
    metadata=[]        #list of list that contain
    for i in range(len(filePaths)):
        metaobj=MLData(filePaths[i],tessaractFilePath,piiDataTagsFilePath,objectClassificationConfigFilePath,frozenModelFilePath)
        metadata.append(metaobj.getMlData())

