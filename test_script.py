import os

def check_files():
    required_files = ["Lab 5-Spring 2025.ipynb", "README.md"]
    missing_files = [file for file in required_files if not os.path.exists(file)]

    if missing_files:
        print(f"Missing files: {missing_files}")
        exit(1)  # Exit with error
    else:
        print("All required files are present.")

if __name__ == "__main__":
    check_files()
