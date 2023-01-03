from car import Car

def main():
    """ Try out the Car class. """
    c = Car()
    c.turn('l')
    c.drive(10)
    c.turn('l')
    c.drive(9)
    c.status()

if __name__ == "__main__":
    main()