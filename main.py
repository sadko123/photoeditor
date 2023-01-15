from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QListWidget, QHBoxLayout, QVBoxLayout, QFileDialog
import os

from PIL import Image

from PIL import ImageFilter

from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class ImageProcessor():
    def __init__(self):
        self.image = None
        self.full_path = None
        self.modified_dir_name = 'Modified'
    def loadImage(self, dir, name):
        self.full_path = os.path.join(dir, name)
        print(self.full_path)
        self.image = Image.open(self.full_path)
        self.current_dir = dir
        self.image_name = name
    def showImage(self):
        lbl_image.hide()
        pixmapimage = QPixmap(self.full_path)
        w, h = lbl_image.width(), lbl_image.height()
        pixmapimage = pixmapimage.scaled(w, h, Qt.KeepAspectRatio)
        lbl_image.setPixmap(pixmapimage)
        lbl_image.show()
    def saveImage(self):
        path = os.path.join(self.current_dir, self.modified_dir_name)
        if not (os.path.exist(path) and os.path.isdir(path)):
            os.mkdir(path)
        self.full_path = os.path.join(path, self.image_name)
        self.image.save(self.full_path)
    def do_bw(self):
        self.image = self.image.convert('L')
        self.saveImage()
        self.showImage()
    def do_blur(self):
        self.image = self.image.filter(ImageFilter.BLUR)
        self.saveImage()
        self.showImage()
    def do_up(self):
        self.image = self.image.transpose(Image.ROTATE_90)
        self.saveImage()
        self.showImage()
    def do_mir(self):
        self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.saveImage()
        self.showImage()
        
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Редактор изображений')
main_win.resize(700, 500)



btn_select_dir = QPushButton('Выбрать папку')
list_widget_images = QListWidget()
lbl_image = QLabel('Картинка')
btn_left = QPushButton('Влево')
btn_right = QPushButton('Вправо')
btn_mirror = QPushButton('Зеркало')
btn_sharpness = QPushButton('Резкость')
btn_bw = QPushButton('Ч/б')

layout_edit_buttons = QHBoxLayout()
layout_edit_buttons.addWidget(btn_left)
layout_edit_buttons.addWidget(btn_right)
layout_edit_buttons.addWidget(btn_mirror)
layout_edit_buttons.addWidget(btn_sharpness)
layout_edit_buttons.addWidget(btn_bw)

layout_image = QVBoxLayout()
layout_image.addWidget(lbl_image, 95)
layout_image.addLayout(layout_edit_buttons, 5)

layout_files = QVBoxLayout()
layout_files.addWidget(btn_select_dir)
layout_files.addWidget(list_widget_images)

layout_main = QHBoxLayout()
layout_main.addLayout(layout_files, 20)
layout_main.addLayout(layout_image, 80)

main_win.setLayout(layout_main)

current_image = ImageProcessor()

current_dir = ''

def showFileNames():
    print('открываем папку')
    global current_dir
    current_dir = QFileDialog.getExistingDirectory()
    print(current_dir)
    all_files = os.listdir(current_dir)
    print(all_files)
    image_files = images_select(all_files)
    print(image_files)
    list_widget_images.clear()
    list_widget_images.addItems(image_files)

def images_select(all_files):
    result = []
    extentions = ['.png', '.jpeg', '.jpg', '.gif']
    
    for file_name in all_files:
        for ext in extentions:
            if file_name.endswith(ext) or file_name.endswith(ext.upper()):
                result.append(file_name)
    return result

def showChoosenImage():
    name_image = list_widget_images.currentItem().text()
    current_image.loadImage(current_dir, name_image)
    current_image.showImage()


btn_select_dir.clicked.connect(showFileNames)
list_widget_images.currentRowChanged.connect(showChoosenImage)

btn_bw.clicked.connect(current_image.do_bw)
btn_left.clicked.connect(current_image.do_up)
btn_mirror.clicked.connect(current_image.do_mir)
btn_sharpness.clicked.connect(current_image.do_blur)
btn_bw.clicked.connect(current_image.do_bw)


main_win.show()
app.exec_()