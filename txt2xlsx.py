import pandas as pd

# 定义输入和输出文件路径  
txt_file_path = 'Fano5.txt'  # 请将此路径替换为你的txt文件路径  
xlsx_file_path = 'Fano5.xlsx'  # 输出xlsx文件路径  

# 读取txt文件，其中sep='\t'表示以制表符分隔  
data = pd.read_csv(txt_file_path, sep='\t', header=None)  

# 将数据写入xlsx文件  
data.to_excel(xlsx_file_path, index=False, header=False)  

print(f"成功将 {txt_file_path} 转换为 {xlsx_file_path}")

