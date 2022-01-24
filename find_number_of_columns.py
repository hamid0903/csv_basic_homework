def find_number_of_columns(data):
    """
    Find the number of columns in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of columns.
    """
    txt=data.split('\n')
    print(txt)
    numb_column=txt[0].split(',')
    print(numb_column)
    return len(numb_column)
data=open('data.csv').read()
print(find_number_of_columns(data))

# Read the csv file