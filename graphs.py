import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

f = open("mytestfile.fastq","r")


def grab_seq(opened_file):
    """return a list with all the sequence needed for analysis from a fastq file"""
    counter = 0
    seq = []
    for i in opened_file:
        counter += 1
        if counter % 4 == 0:
            seq.append(i.strip("\n"))
    return seq


def list_prob(seq_list):
    """return a list of all the correct probability"""
    result = []
    for seq in seq_list:
        temp = []
        for i in seq:
            temp.append(ord(i)-33)
        prob = []
        for i in temp:
            prob.append(1-10**(-i/10))
        result.append(prob)
    return result


def analysis(prob_list):
    """create 4 lists for maximum, minimum, mean, and median, respectively"""
    maxi = []
    mini = []
    mean = []
    median = []
    for i in prob_list:
        maxi.append(max(i))
        mini.append(min(i))
        mean.append(sum(i)/len(i))
        median.append(np.median(i))
    return maxi, mini, mean, median


maximum, minimum, mean, median = analysis(list_prob(grab_seq(f)))


def data_frame(list1, list2, list3, list4):
    d = {"maximum": list1, "minimum": list2, "mean": list3, "median": list4}
    return pd.DataFrame(d)

def data_frame1(l1, l2, l3, l4):
    l = []
    l.extend(l1)
    l.extend(l2)
    l.extend(l3)
    l.extend(l4)
    c = []
    for i in range(len(l1)):
        c.append("max")
    for i in range(len(l2)):
        c.append("min")
    for i in range(len(l3)):
        c.append("mean")
    for i in range(len(l4)):
        c.append("median")
    d = {'data': l, 'category':c }
    return pd.DataFrame(d)


#print(data_frame1(maximum, minimum, mean, median))
#print(data_frame(maximum, minimum, mean, median))

# generate the first graph, scatterplot
sns.set()
sns.set_context("notebook")
sns.scatterplot(x = 'mean', y = 'median', data = data_frame(maximum, minimum, mean, median), size = 10)
plt.show()

# generate the swarmplot graph, which is a categorical scatterplot with non-overlapping points.
# sns.set()
# sns.set_context("notebook")
# sns.swarmplot(x = 'mean', y = 'median', data = data_frame(maximum, minium, mean, median), size = 5, palette="spring")
# plt.show()

#generate the histogram graph.
sns.set()
sns.set_context("notebook")
ax = sns.distplot(mean, rug_kws={"color": "g"}, bins=10, rug = True, kde = False)
ax.set(xlabel = "mean")
plt.show()

#generate a box plot graph of all categories
sns.set()
sns.set_context("notebook")
sns.boxplot(x = "category", y = "data", data = data_frame1(maximum, minimum, mean, median), palette="spring", linewidth=2.5)
plt.show()

#generate a box plot graph of median and mean
sns.set()
sns.set_context("notebook")
sns.boxplot(x = "median", y = "mean", data = data_frame(maximum, minimum, mean, median), palette="spring", linewidth=2.5)
plt.show()

#generate a linear graph
sns.set()
sns.set_context("notebook")
sns.regplot(x = "mean", y = "median", data = data_frame(maximum, minimum, mean, median), line_kws = {"color":"red"})
plt.show()