__author__ = 'r.lukaszewski'

from gi.repository import Gtk
from datetime import datetime
import sqlite3

class App():
    def __init__(self):

        self.open_db()
        self.init_ui()

    def init_ui(self):
        builder = Gtk.Builder()
        builder.add_from_file("kontakty.glade")

        handlers = {
            "onDeleteWindow": self.quit,
            "on_btnAdd_clicked": self.add,
            "on_btnShow_clicked": self.show_contacts,
            "on_btnSearch_clicked": self.search,
            "on_btnDelete_clicked": self.delete,
            "on_btnUpdate_clicked": self.update
        }
        builder.connect_signals(handlers)

        self.window = builder.get_object("window1")
        self.window.show_all()

        self.lbxContacts = builder.get_object("lbxContacts")
        self.contactsViewModel = Gtk.ListStore(str, str, str, str)
        self.lbxContacts.set_model(self.contactsViewModel)
        renderer = Gtk.CellRendererText()
        self.lbxContacts.append_column(Gtk.TreeViewColumn("Nazwa", renderer, text=0))
        self.lbxContacts.append_column(Gtk.TreeViewColumn("Nr Tel", renderer, text=1))
        self.lbxContacts.append_column(Gtk.TreeViewColumn("Email", renderer, text=2))
        self.lbxContacts.append_column(Gtk.TreeViewColumn("Timestamp", renderer, text=3))

        self.tbxName = builder.get_object("tbxName")
        self.tbxTel = builder.get_object("tbxTel")
        self.tbxEmail = builder.get_object("tbxEmail")

    def add(self, button):
        """Dodajemy nowy "rekord" """
        rec = [self.tbxName.get_text(),self.tbxTel.get_text(),self.tbxEmail.get_text(), datetime.now()]
        self.cursor.execute("""insert into Kontakty values (?,?,?,?) """,rec)
        self.clear_form()
        self.show_contacts()

    def clear_form(self):
        self.tbxName.set_text("")
        self.tbxTel.set_text("")
        self.tbxEmail.set_text("")

    def update(self, btn=None):
        """Aktualizacja rekordu """
        urec = [self.tbxName.get_text(),self.tbxTel.get_text(),self.tbxEmail.get_text(), datetime.now(), self.tbxName.get_text()]
        self.cursor.execute("""update or abort Kontakty set Nazwa=?, Nr_Tel=?, Email=?, Timestamp=? where Nazwa=?""",urec)
        self.show_contacts()

    def save(self):
        """Zapisujemy baze"""
        self.db.commit()

    def delete(self, btn):
        """Usuniecie rekordu"""
        nrec = [self.tbxName.get_text(),self.tbxTel.get_text(),self.tbxEmail.get_text()]
        self.cursor.execute("""delete from Kontakty where Nazwa=? or Nr_Tel=? or Email=? """,nrec)
        self.show_contacts(None)

    def search(self, btn):
        """Wyswietlenie konkretnego rekordu wedlug nazwy"""
        srec = [self.tbxName.get_text(),self.tbxTel.get_text(),self.tbxEmail.get_text()]
        self.cursor.execute("""select * from Kontakty where Nazwa=? or Nr_Tel=? or Email=? """,srec)
        wynik = self.cursor.fetchone()
        if wynik is not None:
            print(wynik)
            self.tbxName.set_text(wynik[0])
            self.tbxTel.set_text(wynik[1])
            self.tbxEmail.set_text(wynik[2])
            self.update()
            self.show_contacts()

    def show_contacts(self, btn = None):
        """Wiadomo co"""
        self.contactsViewModel.clear()

        self.cursor.execute("select * from Kontakty")
        for row in self.cursor:
            lstRow = list(row)
            lstRow[3] = str(lstRow[3])
            self.contactsViewModel.append(row)

    def open_db(self):
        """Otwieranie bazy z pliku"""

        self.db = sqlite3.connect("kontakty.db")
        self.cursor = self.db.cursor()

        self.cursor.execute("""create table if not exists Kontakty (
                    Nazwa text,
                    Nr_Tel text,
                    Email text,
                    Timestamp date,
                    PRIMARY KEY (Nazwa ASC)) """)

    def quit(self, *args):
        self.save()
        self.db.close()
        Gtk.main_quit(*args)


app = App()
Gtk.main()

