from sys import executable, base_prefix, prefix
import site
import os


if __name__ == "__main__":
    in_venv = base_prefix != prefix
    print("\nMATRIX STATUS: ", end="")
    print("Welcome to the construct" if in_venv else "You're still plugged in")

    print("\nCurrent Python: ", end="")
    print(executable)
    print("Virtual Environment: ", end="")
    name = os.path.basename(prefix)
    print(name if in_venv else "None detected")
    if in_venv:
        print("Environment Path: ", end="")
        print(prefix)

        print("\nSUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.")

        print("\nPackage installation path:")
        if current_path_packages := site.getsitepackages():
            print(current_path_packages[0])
    else:
        print("\nWARNING: You're in the global environment!")
        print("The machines can see everything you install.")

        print("\nTo enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\\Scripts\\activate # On Windows")

        print("\nThen run this program again.")
