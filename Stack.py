class Stack:
    def __init__(self, max_size):
        # Creates a new stack that is empty with a maximum size.
        self.stack = []  # Use a list to store stack elements
        self.max_size = max_size

    def __str__(self):
        # Returns a string representation of the stack.
        if self.isEmpty():
            return "Stack is empty"
        return "->".join(map(str, reversed(self.stack)))

    def getSize(self):
        # Returns the current size of the stack.
        return len(self.stack)

    def isEmpty(self):
        # Checks if the stack is empty.
        return len(self.stack) == 0

    def peek(self):
        # Returns the top item from the stack without removing it.
        if self.isEmpty():
            return "Stack is empty, nothing to peek."
        return self.stack[-1]

    def push(self, item):
        # Adds a new item to the top of the stack.
        if len(self.stack) >= self.max_size:
            return "Stack is full. Cannot push more elements."
        self.stack.append(item)
        return f"Pushed {item} onto the stack."

    def pop(self):
        # Removes and returns the top item from the stack.
        if self.isEmpty():
            return "Stack is empty. Nothing to pop."
        return self.stack.pop()


def main():
    #Ask the user for the maximum size of the stack
    max_size = int(input("Enter the maximum size of the stack: "))
    stack = Stack(max_size)

    while True:
        print("\nStack Operations:")
        print("1. Push - adds a new item to the top of the stack")
        print("2. Pop - removes the top item from the stack.")
        print("3. Peek - returns the top item from the stack but does not remove it. ")
        print("4. Check if Empty")
        print("5. Show Stack")
        print("6. Quit")
        
        choice = input("Choose an operation (1-6): ")

        if choice == "1":  #Push
            item = input("Enter a string to push: ")
            result = stack.push(item)
            print(result)

        elif choice == "2":  #Pop
            result = stack.pop()
            print(result)

        elif choice == "3":  #Peek
            result = stack.peek()
            print(f"Top item: {result}")

        elif choice == "4":  #isEmpty
            print(f"Stack is empty: {stack.isEmpty()}")

        elif choice == "5":  #Show Stack
            print(f"Current stack: {stack}")

        elif choice == "6":  #Quit
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid operation.")


if __name__ == "__main__":
    main()
