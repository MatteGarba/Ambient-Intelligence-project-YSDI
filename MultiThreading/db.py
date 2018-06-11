import time, sqlite3
import TimeManagement as tm
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "YSDIdb")

def ClearAll():
    connection = sqlite3.connect(db_path)
    cur = connection.cursor()
    sql = """SELECT name
            FROM sqlite_master
            WHERE type="table"
          """
    cur.execute(sql)
    tables = cur.fetchall()
    sql = """DELETE FROM {}"""
    for tupla in tables:
        cur.execute(sql.format(tupla[0]))
    connection.commit()
    connection.close()


def MicInsert():
    instant = int(tm.ChromeCurrentInstant(0) / 1e6)
    connection = sqlite3.connect(db_path)
    cur = connection.cursor()
    sql = """INSERT INTO microphone
            VALUES (?)
      """
    cur.execute(sql, (instant,))
    connection.commit()
    connection.close()

def HistoryInsert(visits):
    connection = sqlite3.connect(db_path)
    cur = connection.cursor()
    sql = """INSERT INTO history
              VALUES (?)
            """
    for coppia in visits:
        instant = int(int(coppia[0])/1e6)
        cur.execute(sql, (instant,) )
    connection.commit()
    connection.close()

def ChairInsert(sitting):
    connection = sqlite3.connect(db_path)
    cur = connection.cursor()
    sql = """INSERT INTO chair (ChromeTimestamp, sitting)
          VALUES (?,?);
    """
    instant = tm.ChromeCurrentInstant(0)
    cur.execute(sql, (instant, sitting) )
    connection.commit()
    connection.close()
    return


#The following functions before the # are for the debugging window
def HistoryCount():
    connection = sqlite3.connect(db_path)
    cur = connection.cursor()
    sql = """SELECT COUNT(*)
            FROM history;
                """
    cur.execute(sql)
    tupla = cur.fetchone()
    connection.close()
    return int(tupla[0])
def MicCount():
    connection = sqlite3.connect(db_path)
    cur = connection.cursor()
    sql = """SELECT COUNT(*)
                FROM microphone;
                    """
    cur.execute(sql)
    tupla = cur.fetchone()
    connection.close()
    return int(tupla[0])
def getLastSit():
    connection = sqlite3.connect(db_path)
    cur = connection.cursor()
    sql = """SELECT sitting
             FROM chair
             ORDER BY ChromeTimestamp DESC;
                        """
    cur.execute(sql)
    tupla = cur.fetchone()
    connection.close()
    if tupla is None:
        return 0
    return tupla[0]
#

def getHist(range, now):
    connection = sqlite3.connect(db_path)
    cur = connection.cursor()
    sql = """SELECT *
             FROM history
             WHERE (?-ChromeTimestamp)<= ?;
                        """
    cur.execute(sql, )
    tupla = cur.fetchone()
    connection.close()
    return int(tupla[0])

def getMic(range, now):
    connection = sqlite3.connect(db_path)
    cur = connection.cursor()
    sql = """SELECT *
             FROM microphone
             WHERE (?-ChromeTimestamp)<= ?;
                        """
    cur.execute(sql, now, range)
    tupla = cur.fetchone()
    connection.close()
    return int(tupla[0])
