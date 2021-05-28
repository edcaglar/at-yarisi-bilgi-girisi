import sqlite3

class Db_Islemleri():

    def __init__(self):
        self.con = sqlite3.connect("atyarisi_db")
        self.cursor = self.con.cursor()

        self.db_olustur()


    def db_olustur(self):

        self.cursor.execute("CREATE TABLE IF NOT EXISTS atyarisi(at_adi TEXT, at_sahibi TEXT, at_jokeri TEXT, mesafe TEXT, kosu_cinsi TEXT, at_kilosu TEXT, sehir TEXT, derece TEXT, kosma_suresi TEXT ,tarih TEXT)")
        self.con.commit()

    def veri_ekle(self, at_adi, at_sahibi, at_jokeri, mesafe, kosu_cinsi, at_kilosu, sehir, derece, kosma_suresi, tarih):

        self.cursor.execute("INSERT INTO atyarisi VALUES(?,?,?,?,?,?,?,?,?,?)",(at_adi, at_sahibi, at_jokeri, mesafe, kosu_cinsi, at_kilosu, sehir, derece, kosma_suresi, str(tarih),))
        self.con.commit()


    def sorgu_yap(self, at_sahibi):

        self.cursor.execute("SELECT * FROM atyarisi WHERE at_sahibi = ?",(at_sahibi,))
        liste = self.cursor.fetchall()
        return liste