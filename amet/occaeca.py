try:
    # Open a file for reading
    with open('myfile.txt', 'r') as f:
        # Read and process the file contents
except Exception as e:
    # Handle the exception
    print("Error opening the file:", e)
