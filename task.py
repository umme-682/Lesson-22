def hcf(numberSmallest, numberLargest):
    while(numberSmallest):
        numberStore = numberSmallest
        numberSmallest = numberLargest % numberSmallest
        numberLargest = numberStore
    return numberLargest

# enter 2 numbers
numberLargest = int(input("Enter largest number: "))
numberSmallest = int(input("Enter smallest number: "))

# LCM equals product of numbers divide HCF of the numbers
lcm = int((numberSmallest / hcf(numberSmallest, numberLargest))*numberLargest)
print("LCM is: ", lcm)