from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QListWidget, QHBoxLayout, QVBoxLayout
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Редактор изображений')

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


main_win.show()
app.exec_()