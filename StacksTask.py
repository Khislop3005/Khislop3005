numStack = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
top = -1
maxSize = 10

#In this program x == x has be input in numerous places. Change this code to get the stack working.
#Note that this implementation of a stack has been completed using an array based implementation.


def isFull():
    #Should retun True if the stack is already full and False if it is not full
    if top == maxSize - 1:
        return True
    else:
        return False


def isEmpty():
    #Should return True if stack is empty and False if it is not empty
    if top == -1:
        return True
    else:
        return False


def push(numStack, itemToAdd, top):
    if isFull() == True:
      print("Stack is full.")
    else:
      top = top + 1
      numStack[top] = itemToAdd
      return top


def pop(numStack, top):
    if isEmpty() == False:
        itemToReturn = numStack[top]
        print(numStack[top])
        top = top - 1
        return itemToReturn
    else:
        print("Unable to return an item from the stack")


def peek(numStack, top):
    if isEmpty() == False:
        itemToReturn = numStack[top]
        return itemToReturn
    else:
        print("Unable to return an item from the stack")


def main():
    print("""Select: \n1 to enter a value onto a stack \n2 to retrieve and remove the value from the top of the stack \n3 to view the item at the top of the stack \n4 to exit the menu.""")
    choice = int(input("Enter choice: "))
    if choice == 1:
      itemToAdd = int(input("Please enter the number you would like to add: "))
      print("Adding to stack")
      push(numStack, itemToAdd, top)
      print(numStack)
    elif choice == 2:
      print("Popping from stack")
      item = pop(numStack, top)
      print(item)
    elif choice == 3:
      print("Peeking top of stack")
      item = peek(numStack, top)
      print(item)
    else:
      print("Please make sure choice is between 1 and 3")
      main()

main()
again = input("Would you like to go again(Yes/No)? ")
while again.lower() == "yes":
    main()
    again = input("Would you like to go again(Yes/No)? ")
