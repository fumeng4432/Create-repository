import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import joblib

# 加载数据
df = pd.read_csv('student_data_adjusted_rounded.csv')

# 查看实际列名（调试用）
print("CSV文件实际列名：", df.columns.tolist())

# 选择特征和目标变量（使用CSV中实际存在的列名）
features = ['期中考试分数', '上课出勤率', '作业完成率', '每周学习时长（小时）']
target = '期末考试分数'

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(df[features], df[target], test_size=0.2, random_state=42)

# 创建并训练随机森林回归模型（减小模型大小的参数调整）
model = RandomForestRegressor(
    n_estimators=50,  # 减少树的数量（从100减少到30）
    max_depth=10,     # 限制树的最大深度
    min_samples_split=5,  # 增加分裂所需的最小样本数
    min_samples_leaf=3,   # 增加叶子节点的最小样本数
    random_state=42
)
model.fit(X_train, y_train)

# 评估模型
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f'模型均方误差: {mse}')

# 保存模型为pkl文件（带压缩）
joblib.dump(model, 'score_prediction_model.pkl', compress=9)
print('模型已保存为score_prediction_model.pkl（已压缩）')

# 输出模型特征重要性
feature_importance = pd.DataFrame({
    '特征': features,
    '重要性': model.feature_importances_
}).sort_values('重要性', ascending=False)

print('特征重要性:')
print(feature_importance)
