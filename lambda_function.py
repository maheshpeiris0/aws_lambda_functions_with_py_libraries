import pandas as pd

def lambda_handler(event, context):
    # Create a dictionary of lists
    data = {
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago']
    }

    # Create DataFrame
    df = pd.DataFrame(data)

    # Convert DataFrame to a string to print it in Lambda's logs
    print(df.to_string())

    # Optionally return something
    return {
        'statusCode': 200,
        'body': df.to_json(orient='records')
    }
