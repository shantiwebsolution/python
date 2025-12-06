
user_input = input("Enter text to write to file: ")
with open("output.txt", "w") as file:
    file.write(user_input + "\n")

print("Data sucessfully written to output.txt")

# Step 2: Append additional data to the file
append_input = input("Enter data to append to file: ")
with open("output.txt", "a") as file:
    file.write(append_input + "\n")

print("Data sucessfully appended to output.txt")

# Step 3: Read and display the final content
print("\nFinal Content of output.txt:")
with open("output.txt", "r") as file:
    content = file.read()
    print(content)