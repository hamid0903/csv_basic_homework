def get_first_column(data):
    """
    Get the first column from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First column.
    """
    columns=[]
    txt=data.split('\n')
    idx=0
    while idx<len(txt):
        columns.append(txt[idx].split(','))
        idx+=1
    first_column=[]
    idx=0
    while idx<len(columns):
        first_column.append(columns[idx][0])
        idx+=1
    return first_column
data=open('data.csv').read()
print(get_first_column(data))
    
# Read the csv file