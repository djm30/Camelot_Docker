import PyPDF2
import pandas as pd
import camelot

def parse_pdf(filename):
    with open(filename, "rb") as f:
        reader = PyPDF2.PdfFileReader(f)
        content = ""
        for page in reader.pages:
            content += page.extractText()

        dataframes = []
        tables = camelot.read_pdf(f.name, pages="1-end")
        for table in tables:
            dataframes.append(table.df)
        
        return content, dataframes
    

if __name__ == "__main__":
    content, tables = parse_pdf("app/Sample2.pdf")
    print(content)
    print(len(tables))
