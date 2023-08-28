import pandas as pd

def main():
    # Open the CSV file
    print("CSV relative path: ")
    inp = input()
    file = open(inp, "r")

    # Convert CSV file to pandas dataframe
    df = pd.read_csv(file)

    # Remove duplicate rows
    df.drop_duplicates(subset=None, inplace=True)

    # Output duplicates removed to new CSV
    df.to_csv("duplicates_removed.csv", index=False)

    # Close the CSV file
    file.close()

if __name__ == "__main__":
    main()