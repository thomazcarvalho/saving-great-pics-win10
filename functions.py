def transfer_archives(from_folder, to_folder):
    from time import sleep
    from distutils.dir_util import copy_tree
    print('Copiando arquivos para pasta destino...')
    sleep(3)
    copy_tree(from_folder, to_folder)
    print('Arquivos copiados!')


def rename_all_archives(folder):
    from time import sleep
    import os
    print('Renomeando extensão dos arquivos...')
    sleep(3)
    for filename in os.listdir(folder):
        old_name = folder + '\\' + filename
        filename = filename[:-4]
        new_name = folder + '\\' + filename + '.jpg'
        os.rename(old_name, new_name)
    print('Pronto!')


def delete_small_files(folder):
    from time import sleep
    import os
    print('Removendo arquivos desnecessários...')
    sleep(3)
    for filename in os.listdir(folder):
        full_file_name = folder + '\\' + filename
        size = os.path.getsize(full_file_name)
        if size < 200000:
            os.remove(full_file_name)
    print('Finalizado!')


def save_pictures(u):
    user = u
    from_folder = 'C:/Users/' + user + \
        '/AppData/Local/Packages/Microsoft.Windows.' \
        'ContentDeliveryManager_cw5n1h2txyewy/LocalState/Assets'
    to_folder = 'C:/Users/' + user + '/Desktop/Fotos Windows 10'
    print()
    transfer_archives(from_folder, to_folder)
    print()
    rename_all_archives(to_folder)
    print()
    delete_small_files(to_folder)


def __main__():
    user = 'thoma'
    from_folder = 'C:/Users/' + user + \
        '/AppData/Local/Packages/Microsoft.Windows.' \
        'ContentDeliveryManager_cw5n1h2txyewy/LocalState/Assets'
    to_folder = 'C:/Users/' + user + '/Pictures/Destaques/Novos'
    print()
    transfer_archives(from_folder, to_folder)
    print()
    rename_all_archives(to_folder)
    print()
    delete_small_files(to_folder)


if __name__ == "__main__":
    __main__()
