#importing! always the first step
import csv
import numpy as np
import matplotlib.pyplot as plt

#setting up the lists
GroupA = [3,2,4,2,1,1,2,2]
GroupB = [6,3,5,7,3,5,2,3]

#Let's find the means
print("means:")
print(np.mean(GroupA))
print(np.mean(GroupB))
print("")

#Let's find the variance
print("variances:")
print(np.var(GroupA))
print(np.var(GroupB))
print("")

#Let's find the standard deviations
print("standard deviations:")
print(np.std(GroupA))
print(np.std(GroupB))
plt.clf()

#now lets create the graph!

#setting up the data, making the bars and setting the colors, creating the lists
xdata=[0,1]
ydata=[np.mean(GroupA), np.mean(GroupB)]
colors=["lightpink", "yellowgreen"] #sets the colors

#error bar that shows the standard deviation
yerrs=[0.927024810887, 1.63935963108]

#creating the bar graph, labeling the graph and y axis
plt.bar(xdata,ydata, width=0.6, color=colors, yerr=yerrs, capsize=5)
plt.suptitle("The Effect of Smell on Taste")
plt.ylabel("Taste from Sweet-1 to Spicy-10")

#labels the bars and shows what is GroupA and what is Group B
plt.xticks([0,1], ["No Smell", "Kimchi"])

#making the bar graph actually appear!
plt.show()