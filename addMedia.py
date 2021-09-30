import sys
import os
import mysql.connector
import ftplib
from shutil import copyfile, copy

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def run():
    # Read bdd file config
    with open('config_bdd.txt') as f:
        datas = f.readlines()
    count = -1
    config = []
    for line in datas:
        count += 1
        config.append( "{}".format(line.strip()) )
    
    conn = mysql.connector.connect(host=config[0],user=config[1],password=config[2], database=config[1])
    cursor = conn.cursor()

    #Get the choice
    id_city = choiceMenu(cursor)

    # Read ftp file config
    with open('config_ftp.txt') as f:
        datasFTP = f.readlines()
    countFTP = -1
    configFTP = []
    for line in datasFTP:
        countFTP += 1
        configFTP.append( "{}".format(line.strip()) )
    session = ftplib.FTP("{}".format(configFTP[0]),"{}".format(configFTP[1]),"{}".format(configFTP[2]))

    # Listen folder "medias"
    for media in os.listdir("medias"):
        row = {
            'filename': media,
            'id_city': id_city,
            'folder': configFTP[3]
        }

        # Copy in assets folders
        copy("medias/"+media, 'maps_app/assets')

        # Insert data in bdd
        cursor.execute("""INSERT INTO `medias`(`filename`, `path_directory`, `id_city_reference`) VALUES (%(filename)s, %(folder)s, %(id_city)s)""", row)

        # file to send
        file = open( "medias/{}".format(media) ,'rb')
        # send the file          
        session.storbinary("STOR {}/{}".format(configFTP[3], media), file)     
        # close file and FTP
        file.close()
    
    session.quit()
    conn.commit()
    conn.close()

def choiceMenu(cursor):
    print(15*"-", "MENU", 15*"-")
    cursor.execute("""SELECT  `id`,`name` FROM cities""")
    records = cursor.fetchall()
    for row in records:
        print(bcolors.OKCYAN + row[0] + bcolors.ENDC, " : ", row[1])
    print(37*"-")
    choice = input("Enter your id: ")
    return choice

if __name__ == "__main__":
    run()
