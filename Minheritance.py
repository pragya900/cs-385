# Base class 1
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass  # Placeholder for subclasses to implement

# Base class 2
class Flying:
    def fly(self):
        print(f"{self.name} can fly.")

# Base class 3
class Swimming:
    def swim(self):
        print(f"{self.name} can swim.")

# Derived class inheriting from Animal and Flying
class Bird(Animal, Flying):
    def speak(self):
        print(f"{self.name} says Chirp!")

# Derived class inheriting from Animal and Swimming
class Fish(Animal, Swimming):
    def speak(self):
        print(f"{self.name} says Bubble!")

# Derived class inheriting from Bird and Fish
class FlyingFish(Bird, Fish):
    def speak(self):
        print(f"{self.name} says Chirp and Bubble!")

# Example usage
if __name__ == "__main__":
    bird = Bird("Sparrow")
    bird.speak()
    bird.fly()

    print("\n")

    fish = Fish("Goldfish")
    fish.speak()
    fish.swim()

    print("\n")

    flying_fish = FlyingFish("Flying Fish")
    flying_fish.speak()
    flying_fish.fly()
    flying_fish.swim()
