from src.client import IOLClient
from src.config import GET_OPERATIONS_START_DATE, GET_OPERATIONS_END_DATE, OPERATIONS_CSV_PATH

def main():
    client = IOLClient()
    client.create_operations_dataframe(GET_OPERATIONS_START_DATE, GET_OPERATIONS_END_DATE, OPERATIONS_CSV_PATH)

if __name__ == "__main__":
    main()
