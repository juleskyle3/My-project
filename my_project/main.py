 
from helpers import greet
from src.processor import process_data

def main():
    greet("Ghee Supreme")
    result = process_data("data/sample.txt")
    print("Processed Data:", result)

if __name__ == "__main__":
    main()
