def get_first_row(data):   
   """
   Get the first row from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First row.
   """
   txt=[]
   txt2=data.split('\n')
   txt=txt2[1].split(',')   
   return txt
data=open('data.csv').read()
print(get_first_row(data))

# Read the csv file