import sys
import os
import mysql.connector
import ftplib

def run(id_city):
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
            'id_city': id_city
        }

        # Insert data in bdd
        cursor.execute("""INSERT INTO `medias`(`filename`, `path_directory`, `id_city_reference`) VALUES (%(filename)s, '/httpdocs/travels/medias', %(id_city)s)""", row)

        # file to send
        file = open( "medias/{}".format(media) ,'rb')
        # send the file          
        session.storbinary("STOR /httpdocs/travels/medias/{}".format(media), file)     
        # close file and FTP
        file.close()
    
    session.quit()
    conn.commit()
    conn.close()

if __name__ == "__main__":
    id_city = sys.argv[1]
    run(id_city)
