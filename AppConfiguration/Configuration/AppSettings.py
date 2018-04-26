from enum import Enum

class AppSettings(Enum):
    # Absolut paths
    Option_File = 'C:/DropBox/sql/mysql.cnf'
    SQL_Select_Annonce = "C:/DropBox/sql/mysql_script_annonce.sql"
    SQL_Select_kompetence = 'C:/DropBox/sql/mysql_script_kompetence.sql'
    SQL_Insert_annonce_kompetence = 'C:/DropBox/sql/mysql_script_insert_annonce_kompetence.sql'
    SQL_Select_Annonce_Kompetence = 'C:/DropBox/sql/mysql_script_annonce_kompetence.sql'
    Option_groups = 'CloudDB'
    #
    # define for alternativ handler
    # hint: files are stored in relativ path
