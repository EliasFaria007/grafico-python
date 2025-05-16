import matplotlib.pyplot as plt
fig,gnt=plt.subplots()
gnt.set_ylim(0, 50)
gnt.set_xlim(0, 160)
gnt.set_xlabel('dias de projeto')
gnt.set_ylabel('tarefas')
gnt.set_yticks([15,25,35])  
gnt.set_yticklabels(['tarefa 1','tarefa 2','tarefa 3'])
gnt.grid(True)
gnt.broken_barh([(0, 50), (100, 200), (130, 10)], (30, 9), facecolors=('tab:red'))
gnt.broken_barh([(40, 50)], (20, 9), facecolors=('tab:green'))
gnt.broken_barh([(1010, 10), (150, 10)], (10, 9), facecolors=('tab:blue'))

plt.show()