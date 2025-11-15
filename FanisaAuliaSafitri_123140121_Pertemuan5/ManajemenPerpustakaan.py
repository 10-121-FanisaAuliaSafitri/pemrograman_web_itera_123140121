import sys
from abc import ABC, abstractmethod

class LibraryItem(ABC):
    def __init__(self, item_id, title):
        self._item_id = item_id
        self._title = title
        self._is_available = True

    @property
    def item_id(self):
        return self._item_id

    @property
    def title(self):
        return self._title

    @property
    def is_available(self):
        return self._is_available

    @is_available.setter
    def is_available(self, status):
        if isinstance(status, bool):
            self._is_available = status
        else:
            print("Error: Status harus berupa boolean (True/False).", file=sys.stderr)

    @abstractmethod
    def display_details(self):
        pass

class Book(LibraryItem):
    def __init__(self, item_id, title, author, isbn):
        super().__init__(item_id, title)
        self._author = author
        self._isbn = isbn

    def display_details(self):
        status = "Tersedia" if self.is_available else "Dipinjam"
        print(f"--- Detail Buku ---")
        print(f"  ID    : {self.item_id}")
        print(f"  Judul : {self.title}")
        print(f"  Penulis: {self._author}")
        print(f"  ISBN  : {self._isbn}")
        print(f"  Status: {status}")

class Magazine(LibraryItem):
    def __init__(self, item_id, title, issue_number, publisher):
        super().__init__(item_id, title)
        self._issue_number = issue_number
        self._publisher = publisher

    def display_details(self):
        status = "Tersedia" if self.is_available else "Dipinjam"
        print(f"--- Detail Majalah ---")
        print(f"  ID       : {self.item_id}")
        print(f"  Judul    : {self.title}")
        print(f"  Edisi    : {self._issue_number}")
        print(f"  Penerbit : {self._publisher}")
        print(f"  Status   : {status}")

class Library:
    def __init__(self):
        self.__items = []

    def add_item(self, item):
        if isinstance(item, LibraryItem):
            self.__items.append(item)
            print(f"INFO: Item '{item.title}' berhasil ditambahkan.")
        else:
            print("Error: Hanya objek dari turunan LibraryItem yang bisa ditambahkan.", file=sys.stderr)

    def display_available_items(self):
        print("\n" + "=" * 30)
        print("  DAFTAR ITEM YANG TERSEDIA")
        print("=" * 30)
        
        found_available = False
        for item in self.__items:
            if item.is_available:
                item.display_details()
                print("-" * 20)
                found_available = True
        
        if not found_available:
            print("Tidak ada item yang tersedia saat ini.")

    def search_item(self, query):
        print(f"\n--- Hasil Pencarian untuk '{query}' ---")
        found = False
        query_lower = query.lower()
        
        for item in self.__items:
            if item.item_id == query or query_lower in item.title.lower():
                item.display_details()
                print("-" * 20)
                found = True
        
        if not found:
            print("Item tidak ditemukan.")

    def _find_item_by_id(self, item_id):
        for item in self.__items:
            if item.item_id == item_id:
                return item
        return None
    
    def check_out_item(self, item_id):
        item = self._find_item_by_id(item_id)
        if item:
            if item.is_available:
                item.is_available = False
                print(f"PEMINJAMAN: '{item.title}' telah berhasil dipinjam.")
            else:
                print(f"INFO: Maaf, '{item.title}' sedang dipinjam.")
        else:
            print(f"Error: Item dengan ID '{item_id}' tidak ditemukan.", file=sys.stderr)

    def check_in_item(self, item_id):
        item = self._find_item_by_id(item_id)
        if item:
            if not item.is_available:
                item.is_available = True
                print(f"PENGEMBALIAN: '{item.title}' telah berhasil dikembalikan.")
            else:
                print(f"INFO: '{item.title}' sudah ada di perpustakaan.")
        else:
            print(f"Error: Item dengan ID '{item_id}' tidak ditemukan.", file=sys.stderr)

if __name__ == "__main__":
    my_library = Library()

    book1 = Book("B001", "Filosofi Teras", "Henry Manampiring", "978-6024246179")
    book2 = Book("B002", "Dune", "Frank Herbert", "978-0441172719")
    mag1 = Magazine("M001", "National Geographic", "Edisi November 2025", "NatGeo Society")

    my_library.add_item(book1)
    my_library.add_item(book2)
    my_library.add_item(mag1)

    my_library.display_available_items()

    print("\n" + "*" * 30)
    my_library.check_out_item("B002") 
    my_library.check_out_item("B999")
    my_library.check_out_item("B002") 
    print("*" * 30)

    my_library.display_available_items()

    print("\n" + "*" * 30)
    my_library.check_in_item("B002") 
    print("*" * 30)

    my_library.search_item("filosofi")
    my_library.search_item("M001") 
    my_library.search_item("Laskar Pelangi")