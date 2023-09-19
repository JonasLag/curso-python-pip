# es ncesario importar e instalar la biblioteca "matplotlib"
import matplotlib.pyplot as plt

#se genera una función que grafica los datos de una manera dinamica
def generate_bar_chart(name, labels, values):
  fig, ax = plt.subplots()
  ax.bar(labels,values )  
  plt.savefig(f'./imgs/{name}.png')
  plt.close()

'''
##se genera una función que grafica los datos definidos previamente.
def generate_bar_chart():
  labels = ['a', ' b', 'c']
  values = [100, 200, 80]
  
  fig, ax = plt.subplots()
  ax.bar(labels,values )
  plt.show()
'''
def generate_pie_chart(labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels = labels)
  ax.axis('equal')
  plt.savefig('pie.png')
  plt.close()
  
if __name__ == '__main__':
  labels = ['a', ' b', 'c']
  values = [100, 400, 800]
  generate_pie_chart(labels, values)
  generate_bar_chart(labels, values)
  