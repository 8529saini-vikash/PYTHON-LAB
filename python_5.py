import os
import sys

print("Current Directory:", os.getcwd())

if len(sys.argv) > 1:
    target_directory = sys.argv[1]
else:
    target_directory = input("Enter directory path: ")

if os.path.exists(target_directory):
    print("\nDirectory Contents:")

    for item in os.listdir(target_directory):
        print(item)

    os.chdir(target_directory)

    print("\nChanged Directory:", os.getcwd())

    workspace = "workspace"

    if not os.path.exists(workspace):
        os.mkdir(workspace)
        print("\nWorkspace folder created.")

    print("\nText Files:")
    for item in os.listdir():
        if item.endswith(".txt"):
            print(item)

    log_file = os.path.join(workspace, "activity.log")

    with open(log_file, "w") as file:
        file.write("Directory inspected successfully.")

    print("\nLog file created:", log_file)

    with open(log_file, "r") as file:
        content = file.read()

    print("\nLog Content:")
    print(content)

else:
    print("Directory does not exist.")