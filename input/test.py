import glob

# set the folder path
folder_path = "/path/to/folder"

# find all the .py files in the folder
py_files = glob.glob(folder_path + "/*.py")

# check if any .py files were found
if not py_files:
    print("No .py files found in the folder.")
else:
    # print the names of the .py files
    print("Please select a .py file:")
    for i, file in enumerate(py_files):
        print(f"{i+1}: {file}")

    # prompt the user to select a file
    selected_file_index = input("Enter the number of the file you want to select: ")

    # validate the user's input
    while not selected_file_index.isdigit() or int(selected_file_index) < 1 or int(selected_file_index) > len(py_files):
        print("Invalid input. Please enter a valid number.")
        selected_file_index = input("Enter the number of the file you want to select: ")

    # get the selected file name
    selected_file_name = py_files[int(selected_file_index) - 1]

    # do something with the selected file
    print(f"You selected file: {selected_file_name}")