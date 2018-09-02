import pyperclip as pc
data = [ i.split('\t') for i in pc.paste().split('\n')]
header = "\\begin{table}[]\n\\centering\n\\begin{tabular}{|" + 'l|'*len(data[0]) + "}\n\\hline\n"
footer = "\\end{tabular}\n\\caption{My caption}\n\\label{my-label}\n\\end{table}"
latex_code = header
for values in data:
	for value in values:
		latex_code += value + " & "
	latex_code = latex_code[:-3] + " \\\\ \\hline\n"
latex_code += footer 
print(latex_code)
pc.copy(latex_code)
print("CODE COPIED TO CLIPBOARD :)")