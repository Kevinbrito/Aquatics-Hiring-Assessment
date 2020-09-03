import sqlite3
import functools
from Model.Classes.Applicants import Applicant


def applicant_table():
    connection = sqlite3.connect('Applicant_Data.sqlite')
    cursor = connection.cursor()
    # create applicant_data_table
    create_applicant_table = """ CREATE TABLE IF NOT EXISTS applicant_table (
                                        First_Name TEXT NOT NULL,
                                        Last_Name TEXT NOT NULL,
                                        Email TEXT NOT NULL,
                                        Custom_ID TEXT NOT NULL PRIMARY KEY,
                                        Points INTEGER NOT NULL,
                                        PassFail TEXT,
                                        UNIQUE(Custom_ID)
                                ); """
    cursor.execute(create_applicant_table)
    cursor.close()
    connection.close()


def cert_table():
    connection = sqlite3.connect('Applicant_Data.sqlite')
    cursor = connection.cursor()
    create_certification_table = """ CREATE TABLE IF NOT EXISTS certification_table (
                                        First_Name TEXT NOT NULL,
                                        Last_Name TEXT NOT NULL,
                                        LG TEXT,
                                        LGM TEXT,
                                        LGI TEXT,
                                        WSI TEXT
                                        ); """
    cursor.execute(create_certification_table)
    cursor.close()
    connection.close()


def search_by_email(email_address):
    connection = sqlite3.connect('Applicant_Data.sqlite')
    cursor = connection.cursor()
    if cursor.execute("SELECT Email FROM applicant_table WHERE Email = ?", (email_address,)).fetchone() is not None:
        cursor.close()
        connection.close()
        return True
    else:
        cursor.close()
        connection.close()
        return False


def no_custom_id(custom_id):
    connection = sqlite3.connect('Applicant_Data.sqlite')
    cursor = connection.cursor()
    if cursor.execute("SELECT Custom_ID FROM applicant_table WHERE Custom_ID = ?", (custom_id,)).fetchone() is None:
        cursor.close()
        connection.close()
        return True
    else:
        cursor.close()
        connection.close()
        return False


def match(custom_id, first_name, last_name):
    connection = sqlite3.connect('Applicant_Data.sqlite')
    cursor = connection.cursor()
    if cursor.execute("SELECT First_Name FROM applicant_table WHERE Custom_ID = ?",
                      (custom_id,)).fetchone() is not first_name:
        cursor.close()
        connection.close()
        return False
    elif cursor.execute("SELECT Last_Name FROM applicant_table WHERE Custom_ID = ?",
                        (custom_id,)).fetchone() is not last_name:
        cursor.close()
        connection.close()
        return False
    else:
        cursor.close()
        connection.close()
        return True


def new_applicant(first_name, last_name, email_address):
    connection = sqlite3.connect('Applicant_Data.sqlite')
    cursor = connection.cursor()
    applicant = Applicant(first_name, last_name, email_address)
    fn = applicant.firstName
    ln = applicant.lastName
    ea = applicant.email_address
    custom_id = applicant.custom_id
    points = 0
    cursor.execute(
        "INSERT INTO applicant_Table (First_Name, Last_Name, Email, Custom_ID, Points) VALUES (?,?,?,?,?)",
        (fn, ln, ea, custom_id, points)
    )
    connection.commit()
    cursor.close()
    connection.close()


def lifeguard_instructor(custom_id):
    connection = sqlite3.connect('Applicant_Data.sqlite')
    cursor = connection.cursor()
    if cursor.execute("SELECT Custom_ID FROM LGI_List WHERE Custom_ID = ?", (custom_id,)).fetchone() is not None:
        cursor.close()
        connection.close()
        return True
    else:
        cursor.close()
        connection.close()
        return False


def sectionOne(custom_id, points):
    connection = sqlite3.connect('Applicant_Data.sqlite')
    cursor = connection.cursor()
    if no_custom_id(custom_id):
        cursor.close()
        connection.close()
        return
    else:
        current_points = cursor.execute("SELECT Points FROM applicant_table WHERE Custom_ID = ?",
                                        (custom_id,)).fetchone()
        cursor.execute("UPDATE applicant_table SET Points = ? WHERE Custom_ID =?",
                       (current_points + points, custom_id,))
        cursor.close()
        connection.close()
