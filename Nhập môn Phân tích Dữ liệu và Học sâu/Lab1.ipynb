# Ngô Minh Khôi - 197CT09794
import pandas as pd
import numpy as np

df = pd.read_csv("dulieuxettuyendaihoc.txt",sep= ',')




# 3. Sử dụng Python để tải dữ liệu lên chương trình và in ra màn hình 10 dòng đầu tiên và 10 dòng cuối cùng.
print(df.head(10))
print(df.tail(10))

# 4. Thống kê dữ liệu thiếu cho cột "dân tộc" và hiệu chỉnh dữ liệu thiếu như sau: Mặc định thiếu thì điền giá trị 0.
df["DT"].fillna(0,inplace=True)


# 5. Thống kê dữ liệu thiếu cho biến "T1" và hiệu chỉnh dữ liệu, lưu ý việc thay thế dữ liệu thiếu sử dụng phương pháp Mean.
df["T1"].fillna(df["T1"].mean(),inplace=True)

#print(df.dtypes)
#is_float64 = df.dtypes == float
#df_columns_list = df.columns[is_float64].tolist()
#print(df_columns_list)



# 7. Tạo các biến "TBM1", "TBM2", "TBM3" tương ứng với trung bình môn của các năm lớp 10, 11 và 12 => Công thức tính: TBM = (T*2 + L + H + S + V*2 + X + D + N) / 10
for i in ["1","2","3"]:
    df["TBM"+i] = (df["T"+i]*2 + df["L"+i] + df["H"+i] + df["S"+i] + df["V"+i]*2 + df["X"+i] + df["D"+i] + df["N"+i]) / 10



# 8. Tạo các biến xếp loại XL1, XL2 và XL3 dựa trên TBM1,TBM2 và TBM3 cho từng năm lớp 10, 11, 12 như sau:
# Nhỏ hơn 5.0 xếp loại: yếu (kí hiệu là Y)
# Từ 5.0 đến dưới 6.5: trung bình (kí hiệu là TB)
# Từ 6.5 đến dưới 8.0: khá (kí hiệu là K)
# Từ 8.0 đến dưới 9.0: giỏi (kí hiệu là G)
# Từ 9.0 trở lên: xuất sắc (kí hiệu là XS)
for i in ['1','2','3']:
    df.loc[(df['TBM'+i] < 5),'XL'+i] = 'Y'
    df.loc[(df['TBM'+i] >= 5) & (df['TBM'+i] < 6.5),'XL'+i] = 'TB'
    df.loc[(df['TBM'+i] >= 6.5) & (df['TBM'+i] < 8),'XL'+i] = 'K'
    df.loc[(df['TBM'+i] >= 8) & (df['TBM'+i] < 9),'XL'+i] = 'G'
    df.loc[(df['TBM'+i] >= 9),'XL'+i] = 'XS'



# 9. Tạo các biến US_TBM1, US_TBM2 và US_TBM3 chuyển điểm trung bình TBM1 ,TBM2, TBM3 từ thang điểm 10 của Việt Nam sang thang điểm 4 của Mỹ.
# Sử dụng phương pháp Min-Max Normalization    
for i in ["1","2","3"]:
    df["US_TBM"+i] = df["TBM"+i]/10 *4

# 10. Tạo biến kết quả xét tuyển (kí hiệu là KQXT) nhằm xác định sinh viên đậu (giá trị 1‖) và rớt ( giá trị 0) vào các khối dựa trên điểm DH1, DH2 và DH3 như sau:
# Với khối A, A1 nếu [(DH1*2 + DH2 + DH3)/4] lớn hơn hoặc bằng 5.0 thì đậu, ngược lại là rớt
# Với khối B nếu [(DH1 + DH2*2 + DH3)/4] lớn hơn hoặc bằng 5.0 thì đậu, ngược lại là rớt
# Với khối khác nếu [(DH1+ DH2 + DH3)/3] lớn hơn hoặc bằng 5.0 thì đậu, ngược lại là rớt

for i in df['KT']:
    df.loc[(i == 'A' or i == 'A1') & (((df['DH1']*2 + df['DH2'] + df['DH3'])/4) >= 5),'KQXT'] = 1
    df.loc[(i == 'A' or i == 'A1') & (((df['DH1']*2 + df['DH2'] + df['DH3'])/4) < 5),'KQXT'] = 0
    
    df.loc[(i == 'B') & (((df['DH1'] + df['DH2']*2 + df['DH3'])/4) >= 5),'KQXT'] = 1
    df.loc[(i == 'B') & (((df['DH1'] + df['DH2']*2 + df['DH3'])/4) < 5),'KQXT'] = 0
    
    df.loc[(i != 'A' or i != 'A1' or i != 'B') & (((df['DH1'] + df['DH2'] + df['DH3'])/3) >= 5),'KQXT'] = 1
    df.loc[(i != 'A' or i != 'A1' or i != 'B') & (((df['DH1'] + df['DH2'] + df['DH3'])/3) < 5),'KQXT'] = 0



print(df)
#print(df['DH1'])
#print(df['DH2'].sort_values(by=['GT'],ascending=True))
