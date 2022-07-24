import os
import time
import csv
import socket
import csv
from datetime import date
import hashlib
from numpy import true_divide

from pip import main


class FileTransfer:
    hostName = None
    server = None
    fileSize = None
    chunkSize = None
    filePath = None
    originalCheckSum = None  # stores the hash that verfires if the file has been sent correctly or not
    summary = ""
    keywords = ""
    piiData = ""
    tags = ""

    def __init__(self, hN, fP, cS, s, k, p, t):
        self.hostName = hN
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.summary = s
        self.keywords = k
        self.piiData = p
        self.tags = t
        self.filePath = fP
        self.chunkSize = cS
        self.fileSize = os.path.getsize(filePath)

        with open(filePath,
                  'rb') as file_to_check:  # Open,close, read file and calculate MD5 on its contents
            data = file_to_check.read()
        self.originalChecksum = hashlib.md5(data).hexdigest()

    # establishes a connection with the server
    def establishConnection(self):
        # To connect to server socket.
        try:
            self.server.connect((self.hostName, 22223))
            print("Successfully connected to Host")
        except:
            print("Unable to connect")
            exit(0)

    # def isEmptySpaceAvailable(self):
    #     flag=False
    #     if emptySize>=self.fileSize:
    #         flag=True
    #     return flag

    # sends the essential details like the file name, extension, etc
    def sendFilesDetails(self):
        self.server.send(self.file_name.encode())
        self.server.send(str(self.fileSize).encode())
        self.server.send(str(self.chunkSize).encode('unicode_escape'))
        self.server.send(self.originalChecksum.encode())

    def sendFileChunks(self):
        with open(f"{self.filePath}/{self.fileName}") as file:
            count = 0
            # Running loop while count != file_size.
            while count <= self.fileSize:
                data = file.read(1024 * int(self.chunkSize))
                if not (data):
                    break
                self.server.sendall(data)
                count += len(data)
            print("File is transffered successfully")

            # Closing the sender (client) socket.
            self.server.close()

    def sendMlDatails(self):
        self.server.send(self.summary)
        self.server.send(self.keywords)
        self.server.send(self.piiData)
        self.server.send(self.tags)



# if __name__ == "__main__":
#     hostName = input("Host Name: ")
#     filePath = input("Enter the folder path in which the file is present")
#     fileName = input("Enter the name of the file")
#     chunkSize = input("Enter the chunk size")
#     ftobj = FileTransfer(hostName, filePath, fileName, chunkSize)
#     ftobj.establishConnection()
#     ftobj.sendFilesDetails()
#     ftobj.sendFileChunks()
