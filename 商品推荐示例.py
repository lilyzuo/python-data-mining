
# coding: utf-8

# In[4]:

import numpy as np
dataset_filename='affinity_dataset.txt'
X=np.loadtxt(dataset_filename)
n_samples,n_features=X.shape
print("This dataset has {0} samples and {1} features".format(n_samples,n_features))
#The name of the feature,for your reference
features=['bread','milk','cheese','apples','bananas']


# In[17]:

#1. Support and Confidence Calculation
#1.1 how many rows contain our premise
num_apple_purchases=0
for sample in X:
    if sample[3]==1 :
        num_apple_purchases+=1
print ("{0} people bought apples".format(num_apple_purchases))
#for sample in [X],reforce to add new list strip


# In[20]:

#how many of cases that a person bought apples involved people purchasing bananas
rule_valid=0
rule_invalid=0
for sample in X:
    if sample[3]==1:
        if sample[4]==1:
            rule_valid+=1
        else:
            rule_invalid+=1
print ("{0} people bought both,{1} people bought only apples.".format(rule_valid,rule_invalid))


# In[24]:

#support and confidence calculation
support=rule_valid/n_samples
confidience=rule_valid/num_apple_purchases
print(support,'---',confidence)


# 支持度: P(A∪B)，即A和B这两个项集在事务集D中同时出现的概率。
# 置信度: P(B｜A)，即在出现项集A的事务集D中，项集B也同时出现的概率。

# In[25]:

print("The support is {0} and the confidence is {1:.3f}.".format(support, confidence))
# Confidence can be thought of as a percentage using the following:
print("As a percentage, that is {0:.1f}%.".format(100 * confidence))


# ##############构建规则字典，得到了支持度字典和置信度字典

# In[32]:

from collections import defaultdict
#get all possible rules
valid_rules = defaultdict(int)
#help(defaultdict)
invalid_rules = defaultdict(int)
num_occurences = defaultdict(int)

for sample in X:
    for premise in range(n_features):
        if sample[premise] == 0: continue
        num_occurences[premise] += 1
        for conclusion in range(n_features):
            if conclusion == premise: continue
            if sample[conclusion] == 1:
                valid_rules[(premise,conclusion)] += 1
            else:
                invalid_rules[(premise,conclusion)] +=1


# In[34]:

support = defaultdict(float)
confidence = defaultdict(float)
for premise,conclusion in valid_rules.keys():
    support[(premise,conclusion)] = valid_rules[(premise,conclusion)]/n_samples
    confidence[(premise,conclusion)] = valid_rules[(premise,conclusion)]/num_occurences[premise]


# In[38]:

for premise,conclusion in confidence:
    print("Rule: If a person buys {0} they will also buy {1}".format(features[premise],features[conclusion]))
    print("- Confidence:{0:.3f}".format(confidence[(premise,conclusion)]))
    print("-Support:{0:.3f}".format(support[(premise,conclusion)]))
    print("")


# In[39]:

def print_rule(premise,conclusion,support,confidence,features):
    print("Rule: If a person buys {0} they will also buy {1}".format(features[premise],features[conclusion]))
    print("- Confidence:{0:.3f}".format(confidence[(premise,conclusion)]))
    print("- Support:{0:.3f}".format(support[(premise,conclusion)]))
    print("")

premise,conclusion=3,4
print_rule(premise,conclusion,support,confidence,features)


# #############排序结果输出

# In[40]:

from pprint import pprint
from operator import itemgetter
sorted_support = sorted(support.items(),key=itemgetter(1),reverse=True)
sorted_confidence = sorted(confidence.items(), key=itemgetter(1), reverse=True)
for index in range(5):
    print("Rule #{0}".format(index+1))
    (premise,conclusion) = sorted_confidence[index][0]
    print_rule(premise,conclusion,support,confidence,features)


# In[ ]:



