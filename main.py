# Necro(ネクロ)
# sidmishra94540@gmail.com

from PyQt5 import QtWidgets
try:
    app = QtWidgets.QApplication([])
    model = QtWidgets.QFileSystemModel()
    path = input('Enter the path of file or folder: ')
    save = input('Enter save location: ')
    print('Working...')
    icon = model.fileIcon(model.index(path))
    sizes = icon.availableSizes()
    list(map(lambda x: icon.pixmap(x[1]).toImage().save(save+'/'+str(x[0])+'.png', quality=100), list(enumerate(sizes))))
    list(map(lambda x: icon.pixmap(x[1]).toImage().save(save+'/'+str(x[0])+'.ico', quality=100), list(enumerate(sizes))))
    print('Done!')
except:
    print('Error')