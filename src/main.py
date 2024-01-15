import os
import shutil


def remove_git_directories(start_path):
    for root, dirs, files in os.walk(start_path):
        if '.git' in dirs:
            git_dir = os.path.join(root, '.git')
            print(f"Removing .git directory at: {git_dir}")
            shutil.rmtree(git_dir)


# Replace 'start_directory' with the path of your starting directory.
start_directory = input('Enter directory where all git repos should be deleted: ')
remove_git_directories(start_directory)

print("Completed removing .git directories.")
