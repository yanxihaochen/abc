import matplotlib.pyplot as plt
categories = ['A', 'B', 'C', 'D']
values = [5, 7, 3, 8]
plt.figure(figsize=(8, 6))
plt.bar(categories, values, color='skyblue')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Chart of Categories vs. Values')
plt.grid(True, axis='y')
plt.show()
