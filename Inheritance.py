class Phone:
    def call(self):
        print("You can Call")
    def message(self):
        print("You can Message")

class Samsang(Phone):
    def photo(self):
        print("You can take picture")

s = Samsang()
s.call()
s.message()
s.photo()
print(issubclass(Samsang,Phone))