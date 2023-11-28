class Mobile():
    def phone (self):
        print("Print the phone:")
    def photo(self):
        print("pshow the photo: ")
class Samsang(Mobile):
    def gallery(self):
        print("Open the gallery: ")

p = Samsang()
p.photo()
p.phone()