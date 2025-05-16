import matplotlib.pyplot as plt
labels= 'nenhum','ensino fundamental','ensino medio', 'ensino superior'
sizes=[30,40,20,10]
colors='skyblue','green','yellow','red'
patches,tests,autotexts=plt.pie(sizes,colors=colors,autopct='%1.0f%%',startangle=90)
plt.legend(patches,labels,loc="lower right")
plt.axis('equal')
plt.show()