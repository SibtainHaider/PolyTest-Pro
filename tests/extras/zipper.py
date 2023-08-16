import os
import zipfile


def zipdir(path, ziph):
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file),
                       os.path.relpath(os.path.join(root, file),
                                       os.path.join(path, '../..')))


def zipit(dir1, dir2, zip_name):
    zipf = zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED)
    zipdir(dir1, zipf)
    zipdir(dir2, zipf)
    zipf.close()


zipit('allure-results', 'allure-report', 'allure.zip')