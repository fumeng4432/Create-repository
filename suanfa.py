import pandas as pd  # 导入pandas库，用于数据处理和分析
from sklearn.ensemble import RandomForestRegressor  # 从sklearn导入随机森林回归器
from sklearn.model_selection import train_test_split  # 从sklearn导入数据集分割函数
from sklearn.metrics import r2_score  # 从sklearn导入R方评分函数，用于评估模型性能
pd.set_option('display.unicode.east_asian_width',True)  # 设置pandas显示选项，使中文字符对齐
insurance_df = pd.read_csv('insurance-chinese.csv',encoding='gbk')  # 读取保险数据CSV文件，使用GBK编码
output=insurance_df['医疗费用']  # 提取目标变量'医疗费用'列作为输出
features=insurance_df[['年龄','性别','BMI','子女数量','是否吸烟','区域']]  # 选取特征列作为输入变量
features = pd.get_dummies(features)  # 对分类变量进行独热编码，转换为数值型特征
x_train, x_test, y_train, y_test =train_test_split(features, output,train_size=0.8)  # 将数据分为训练集(80%)和测试集(20%)
rfr = RandomForestRegressor()  # 创建随机森林回归器实例
rfr.fit(x_train, y_train)  # 用训练集数据训练模型
y_pred =rfr.predict(x_test)  # 使用训练好的模型对测试集进行预测
r2 =r2_score(y_test,y_pred)  # 计算预测值与真实值的R方得分，评估模型性能
print(f'该模型的可决系数(R-squared)是:{r2}')  # 输出模型的R方得分
