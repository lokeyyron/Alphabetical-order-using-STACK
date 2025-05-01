#Luke Aaron T. Velasquez
#Grade 12 CS Neird

from Stack import Stack  # Import the Stack class from Stack.py

def sort_string_with_stack(input_string):
    #Initialize the main stack
    stack = Stack(len(input_string))  #Max size equals the length of the input string
    temp_stack = Stack(len(input_string))  #Make a temporary stack

    #Push all characters into the main stack
    for char in input_string:
        stack.push(char)
    
     #Sort characters using stacks
    while not stack.isEmpty():
        current = stack.pop()  #Pop from main stack
        #Move from temp_stack to stack until the correct position is found
        while not temp_stack.isEmpty() and temp_stack.peek() > current:
            stack.push(temp_stack.pop())
        temp_stack.push(current)  #Push current character to temp_stack

    #Transfer sorted characters back to the main stack
    while not temp_stack.isEmpty():
        stack.push(temp_stack.pop())

     #Reconstruct the sorted string from the main stack
    sorted_string = ""
    while not stack.isEmpty():
        sorted_string += stack.pop()
    
    return sorted_string

def main():
    user_input = input("Enter a string to sort alphabetically: ")
    sorted_result = sort_string_with_stack(user_input)
    print(f"Sorted string: {sorted_result}")

if __name__ == "__main__":
    main()
