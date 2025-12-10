from helpers import greet

def main():
    """Main entry point of the application."""
    try:
        greet("Ghee Supreme")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
