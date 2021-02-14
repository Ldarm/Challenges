import datetime
import zipfile
import os
import glob
# -*- coding: utf-8 -*-
#
# LDT Fev 2021
#
# Script Python2.7 Ok
# lecture info Zip file et decompression en boucle apres recup du passwd
#


# dir_name = 'E:\\03-Challenges\A-Epreuves-Challenges\HackTheBox\Misc\Eternal_Loop\My_test_archive_Python'
dir_name = '/home/ldarm/Challenges/HackTheBox/Misc/Eternal_Loop/My_test_archive_Python'
extension = ".zip"
os.chdir(dir_name) # change directory from working dir to dir with files
Content_filename = ""

# Fonction pour identifier le dernier fichier cree
def newest(dir_name):
    files = os.listdir(dir_name)
    paths = [os.path.join(dir_name, basename) for basename in files]
    return max(paths, key=os.path.getctime)


# item = ""
def print_info(item):
    global Motpass
    global Content_filename
    zf = zipfile.ZipFile(item)
    for info in zf.infolist():
        print ''
        print 'Nom du fichier: ', item
        print 'Contenu: ', info.filename
        print '\tComment:\t', info.comment
        print '\tModified:\t', datetime.datetime(*info.date_time)
        print '\tSystem:\t\t', info.create_system, '(0 = Windows, 3 = Unix)'
        print '\tZIP version:\t', info.create_version
        print '\tCompressed:\t', info.compress_size, 'bytes'
        print '\tUncompressed:\t', info.file_size, 'bytes'
        Content_filename = info.filename
        Motpass = Content_filename.split('.')[0]
        print 'File name :', Content_filename
        print 'Mot de passe:', Motpass
        print 'OS path item:', (os.path.splitext(item))
        zip_ref = zipfile.ZipFile(item)
        for file in zip_ref.infolist():
            print ""
            print " Ok Extract..."
            print "Zip file :", zip_ref.filename
            print "Mot de passe : ", Motpass
            if Motpass != "DoNotTouch":
                zip_ref.extractall(pwd=Motpass)
            else:
                print "ok boucle terminee :", Motpass
                break




if __name__ == '__main__':
    while 1:
        print newest(dir_name)
        item = "".join(newest(dir_name).split("/")[-1])
        print "Fonction newest:", item

        # print "Fichier a traiter:", item
        print_info(item)

        if item != "37366.zip":
            os.remove(dir_name + "/" + item)
            print "On efface:", item
        else:
            print " Ok fin de la boucle..."
            print "script termine"
            break

            # os.system(rm zip_ref.filename)
    # extract_files(item != 'DoNotTouch')
    # extract_files(item)
# Script OK decompression en boucle des fichiers zip
