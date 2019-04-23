import sys
import os
import io
import json
from google.cloud import vision
from google.cloud import translate
from google.cloud.vision import types
from PyQt4 import QtGui, QtCore, Qt

credential_path = '/home/dwill148/cs340/image_translator/cs340-86384d000595.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

def translation(texts, target_ln):
    client = translate.Client()
    data = json.dumps(texts)
    data = data.replace('\\n', '\n').replace('"', '')
    print('Detected Text:')
    print(data)

    translation = client.translate(data, target_language=target_ln)
    f_translation = translation['translatedText'].replace('\ n', '\n').replace('\ N', '\n')
    print("Translation:")
    print(f_translation)
    return f_translation

def detect_text(path, lang='Chinese(Simplified) zh-CN'):
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image:
        content = image.read()

    image = types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    string = ''
    for text in texts:
        string += text.description
        break

    return(translation(string, str(lang).split()[1]))

class TestListView(QtGui.QListWidget):
    def __init__(self, type, parent=None):
        super(TestListView, self).__init__(parent)
        self.setAcceptDrops(True)
        self.setIconSize(QtCore.QSize(72, 72))

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls:
            event.setDropAction(QtCore.Qt.CopyAction)
            event.accept()
        else:
            event.ignore()
    
    def dropEvent(self, event):
        if event.mimeData().hasUrls:
            event.setDropAction(QtCore.Qt.CopyAction)
            event.accept()
            links = []
            for url in event.mimeData().urls():
                links.append(str(url.toLocalFile()))
            self.emit(QtCore.SIGNAL("dropped"), links)
        else:
            event.ignore()

def output(text, listWidget, counter):
  listWidget.addItem(str(counter) + ': ' + text)

class MainForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MainForm, self).__init__(parent)

        self.view = TestListView(self)
        self.connect(self.view, QtCore.SIGNAL("dropped"), self.pictureDropped)
        self.setCentralWidget(self.view)
        self.setWindowTitle('Drag and Drop Window')
        self.resize(600, 500)
        
        self.language = QtGui.QComboBox(self)
        self.language.move(500, 0)

        self.listWidget = QtGui.QListWidget()
        self.listWidget.addItem("Translation:")
  
        self.items = QtGui.QDockWidget("Result",self)
        self.items.setWidget(self.listWidget)
        self.counter = 0

        #compile error
        #self.addDockWidget(Qt.BottomDockWidgetArea,self.items)

        with open('languages.txt') as fin:
            self.language.addItems([i.split()[1] + ' ' + i.split()[0] for i in fin.readlines()])

    def pictureDropped(self, l):
        for url in l:
            self.counter += 1
            if os.path.exists(url):
                translation = detect_text(url, self.language.currentText())
                output(translation, self.listWidget, self.counter)
                icon = QtGui.QIcon(url)
                pixmap = icon.pixmap(72, 72)                
                icon = QtGui.QIcon(pixmap)
                item = QtGui.QListWidgetItem(url, self.view)
                item.setIcon(icon)        
                item.setStatusTip(url)        

def main():
    app = QtGui.QApplication(sys.argv)

    # This is the main window that the entire app runs in
    form = MainForm()
    form.show()

    app.exec_()

if __name__ == '__main__':
    main()
