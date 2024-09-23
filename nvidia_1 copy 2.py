class Animal:
    def shoutall(self):
        self.shoutit()

    def shoutit(self):
        print("sss")

class Bird(Animal):

    def shoutit(self):
        print("xxx")

a = Animal()
b = Bird
c = Bird()

def E(i):
	if (i < 1):
		return 1
	else:
		return E(i - 1) + E(i - 2) + E(i - 3)
print(E(10))