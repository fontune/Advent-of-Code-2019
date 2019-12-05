def main():
    print("Total required fuel: " + str(calculateFuel(readValues("input.txt"))))

def readValues(fileName):
    with open(fileName) as f:
        moduleValues = [value.rstrip('\n') for value in f]
    return moduleValues    
    
def calculateFuel(values):
    fuelRequired = 0
    for value in values:
        fuelRequired = fuelRequired + ((int(int(value)/3) - 2))
    return fuelRequired

main()