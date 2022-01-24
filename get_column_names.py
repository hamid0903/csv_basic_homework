#Define function,Get coloumn names from a csv file
def get_column_names(data):
    """ 
    Get column names from a csv file
    Parameters:
        data(str): csv file
    Returns:
        column_names: list of column names
    """
    column_name=[]
    txt=data.split('\n')
    column_name=txt[0].split(',')
    return column_name
    
data=open('data.csv').read()
print(get_column_names(data))
# Read the csv file