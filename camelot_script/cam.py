import camelot
import os


directory = os.path.dirname(os.path.realpath(__file__))
input_path = os.path.join(directory,'Input')
output_path = os.path.join(directory,'Output')
tables = camelot.read_pdf('{}/Direct Bill Commission Statement.pdf'.format(input_path),pages='all',flavor='stream')
data = tables[0]
filename='output.csv'
file_path = os.path.join(directory, filename)
data.to_csv(file_path,index=False)



