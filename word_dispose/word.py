#coding :utf8
from docx import Document
import pandas as pd
from openpyxl import load_workbook

# docx库不支持doc格式
#  QT_DataModel.doc
def read_table(docpath: str):
    '''docpath->word文件路径    n->要读取文件中的第几个表格。从0开始    返回表格数据的列表    '''

    doc = Document(docpath)
    res = []
    for n in range(0,201):
        print(n)
        tb = doc.tables[n]
        print("table rows :%s"%len(tb.rows))
        for i in range(0, len(tb.rows)):
            data = []
            row_cells = tb.rows[i].cells
            for cell in row_cells:
                data.append(cell.text)
            res.append(data)
    df = pd.DataFrame(res)
    df.to_excel("d:\\tt10.xls",'sheet',index=None)
        #excel_writer = pd.ExcelWriter('d:\\tt3.xlsx', engine='openpyxl')
        #excelAddSheet(df,excel_writer ,'sheet%s'%n)

def excelAddSheet(dataframe,excelWriter,sheet_name):

   book = load_workbook(excelWriter.path)
   excelWriter.book = book
   dataframe.to_excel(excel_writer=excelWriter,sheet_name=sheet_name,index=None)
   excelWriter.close()


read_table('d://qt.docx')



