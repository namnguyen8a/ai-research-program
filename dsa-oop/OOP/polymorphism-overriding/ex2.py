class Document:
    def open(self):
        print("Not Implemented Error")

class PdfDocument(Document):
    def open(self):
        print("Opening PDF document")

class WordDocument(Document):
    def open(self):
        print("Opening Word document")

docs = [PdfDocument(), WordDocument()]
for doc in docs:
    doc.open()