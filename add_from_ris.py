# Run this script to add citations to README from .ris files
# Current version adds all to the "Unsorted Papers" at the end, no tags
#%%
# import statements
import os
from glob import glob

# Filepath organization: default adds to unsorted papers
# Current list of categories (IN PROGRESS):
#
# 0 Condensates
#   0 
#   1 Reviews
#   2 Structural studies
#   3 Cellular studies
#   4 Simulation
#
# 1 RNA Structural Ensembles
#   0
#   1
#
# 2 Riboswitches
# 
# 3 RNA structural ensembles
# 
# 4 RNA Regulation
#
# 5 RNA Therapeutics
#
# 6 Structural methods
#   0
#   1
#   2
# 
# 7 RNA Bioinformatics
#   0
#   1
#   2
# 
# 8 Broad bio computation
#
# 9 Protein structure function
#   0   
#   
# 10 Unsorted papers
#   0

# Month reference:
months = ['', 'January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']

section_num = 10 # Unsorted papers
sub_num = 0 # Default subsection
ris_dir = '' # Default: look in current directory
readme = 'README.md' # readme of references
ris_files = glob(ris_dir + '*.ris')
ris_start = 6 # RIS colunm after label

# Loop through and add one by one
new_reflines = []
for ris in ris_files:
    # Get Title, Author_list, Journal, Month, Year, doi
    with open(ris, 'r') as rfile:
        rlines = rfile.readlines()

    title = ''
    authors = ''
    journal = ''
    month = ''
    yr = ''
    doi = '' 
    url = '' 

    for line in rlines:
        if line.startswith('T1') or line.startswith('TI'):
            title = line[ris_start:-1]
        elif line.startswith('AU'):
            asplit = line[ris_start:-1].split(', ')
            if len(asplit) < 3:
                authors = authors + asplit[0] + ', '
            else: 
                authors = authors + asplit[1] + ' ' + asplit[0] + ', '
        elif line.startswith('DO'):
            doi = line[ris_start:-1] 
        elif line.startswith('T2') or line.startswith('JO'):
            journal = line[ris_start:-1]
        elif line.startswith('Y1') or line.startswith('DA'): 
            date = line[ris_start:-1]
            dnums = date.split('/')
            yr = dnums[0]
            month = months[int(dnums[1])]
        elif line.startswith('UR'):
            url = line[ris_start:-1]

    # Format fudging
     

    # Append to end of file
    new_reflines.append('\n')
    new_reflines.append('**' + title + '**  \n')
    new_reflines.append(authors[:-2] + '  \n')
    new_reflines.append('*' + journal + ', ' + month + ' ' + yr + '.*  \n')
    new_reflines.append('[[' + doi + '](' + url + ')]  \n')
    new_reflines.append('\\___\\_  \n')
    
    print('Added ' + ris)

with open(readme, 'a') as reffile:
    reffile.writelines(new_reflines)

