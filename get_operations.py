from src.client import IOLClient
from pathlib import Path

def main():

    client = IOLClient()
    client.create_operations_dataframe("2024-01-01", "2024-08-01", "data/iol_operations.csv")

if __name__ == "__main__":
    main()
