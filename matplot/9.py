#Matplotlib

import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3,4,5,6,7,8,9,10])
y = np.array([1, 4, 9, 16, 25, 36, 30, 20, 15, 10])


# plt.plot(x, y, marker="D", linestyle="--", color="red",mec="black",ms=10)
# plt.xlabel("X axis")   
# plt.ylabel("Y axis")
# plt.title("Simple Line Plot")


#Bar chat

# fruit = ['Apple', 'Banana', 'Mango', 'Orange', 'Grapes']
# price = [100, 40, 70, 60, 120]
# plt.bar(fruit, price, color=['red', 'yellow', 'green', 'orange', 'purple'], edgecolor='black')
# plt.xlabel("Fruits")
# plt.ylabel("Price in Rs")
# plt.show()  

#Horizontal Bar chart

fruit = ['Apple', 'Banana', 'Mango', 'Orange', 'Grapes']
price = [100, 40, 70, 60, 120]
# plt.barh(fruit, price, color=['red', 'yellow', 'green', 'orange', 'purple'], edgecolor='black')
# plt.xlabel("Fruits")
# plt.ylabel("Price in Rs")
# plt.show()  

#Pie chart
# plt.pie(price, labels=fruit, autopct='%1.1f%%', startangle=140)
# plt.show()

#Scatter plot
plt.scatter(x, y, color='blue', marker='o')
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("Simple Scatter Plot")
plt.show()