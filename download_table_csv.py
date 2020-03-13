import rpa as r
r.init() #Inicialization
r.url('https://www.w3schools.com/tags/tag_table.asp') # Access URL
r.table('w3-table-all notranslate', 'tablewebsite.csv')
