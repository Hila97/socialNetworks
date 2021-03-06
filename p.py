import networkx as nx
import matplotlib.pyplot as plt
import community
import collections
import numpy as np
import scipy as sp
from collections import Counter
from operator import itemgetter
import scipy.special
import seaborn as sns


# יבוא דאטא ראשוני
Data = open('fake_claim.csv', "r")
# Data = open('ClaimFakeCOVID-19_tweets_replies_5.csv', "r")
next(Data, None)  # skip the first line in the input file
Graphtype = nx.DiGraph()
G = nx.parse_edgelist(Data, delimiter=',', create_using=Graphtype, nodetype=int, data=(('weight', float),))
original_nodes = list(G.nodes)
original_edges = list(G.edges)
print("number of nodes ", len(original_nodes))
print("number of edges ", len(original_edges))
# print("original_nodes", original_nodes)
# print("original_edges", original_edges)

# ציור גרף מקורי
color_map = []
for node in G:
    if node < 1000000:
        color_map.append('red')  # articles
    else:
        color_map.append('#4a86e8')  # users
# nx.draw(G, node_color=color_map, with_labels=False)
# #pos = nx.spring_layout(G)
# plt.show()

# רכיבי קשירות
# print("num of strongly cc ", nx.number_strongly_connected_components(G))
# print("num of weakly cc ", nx.number_weakly_connected_components(G))
# print("all the components")
b = sorted(nx.weakly_connected_components(G), key=len, reverse=True)
# print("b", b)

# a=[list(cc) for cc in nx.strongly_connected_components(G)]
# print("connected com", a)
#

# max=0
# adam=0
# for n in original_nodes:
#     degree=G.degree(n)
#     if(degree>max):
#         max=degree
#         adam=n
# print("max",max)
# print("adam",adam)
# NH=nx.DiGraph()
# succ=list(G.successors(adam))
# pre= list(G.predecessors(adam))
# allNodes=succ+pre+[adam]
# #print("allNodes",allNodes)

# ציור רכיב הקשירות הגדול ביותר
largest = len(b[0])
#print("largest connected components ", largest)
NH = G.subgraph(b[0])
nodes=list(NH.nodes)
edges=list(NH.edges)
print("largest connected components nodes",len(nodes))
print("largest connected components edges",len(edges))
color_map = []
for node in NH:
    if node < 1000000:
        color_map.append('red')  # articles
    else:
        color_map.append('#4a86e8')  # users
# nx.draw(NH, node_color=color_map, with_labels=False)
# plt.show()

# print("diameter",nx.diameter(NH.to_undirected()))
# print("average",nx.average_shortest_path_length(NH))


# דרגות בגרף
# degree_sequence = sorted([d for n, d in G.degree()], reverse=True)
# degree sequence
# print("degree",degree_sequence)
# degreeCount = collections.Counter(degree_sequence)
# s=dict(sorted(degreeCount.items(), key=lambda item: item[0]))
# print(s)
######## degree  histogram ###################33
#
# degree_sequence = sorted([d for n, d in G.degree()], reverse=True)  # degree sequence
# print("degree",degree_sequence)
# degreeCount = collections.Counter(degree_sequence)
# deg, cnt = zip(*degreeCount.items())
# fig, ax = plt.subplots()
# plt.bar(deg, cnt, width=0.80, color="b")
# plt.title("Degree Histogram")
# plt.ylabel("Count")
# plt.yscale('log')
# plt.xlabel("Degree")
# plt.xscale('log')
# plt.show()
# ax.set_xticks([d + 0.4 for d in deg])
# ax.set_xticklabels(deg)
#
# # draw graph in inset
#plt.axes([0.4, 0.4, 0.5, 0.5])
#Gcc = G.subgraph(sorted(nx.strongly_connected_components(G), key=len, reverse=True)[0])
#pos = nx.spring_layout(G)
#plt.axis("off")
# # nx.draw_networkx_nodes(G, pos, node_size=20)
# # nx.draw_networkx_edges(G, pos, alpha=0.4)


# מדדי מרכזיות

# print("degree centrality", nx.degree_centrality(G))
# print(nx.in_degree_centrality(G))
# print(nx.out_degree_centrality(G))
# print("betweenness", nx.betweenness_centrality(G, k=100, normalized=True, weight=None, endpoints=False, seed=None))
# print("pagerank", nx.pagerank(G, alpha=0.8))
# print("closeness", nx.closeness_centrality(G))

degree_centrality=nx.degree_centrality(NH)
a={k: v for k, v in sorted(degree_centrality.items(), key=lambda item: item[1], reverse=True)}
#print("####################",a)
# node_sizes=[]
# for x in degree_centrality.values():
#     node_sizes.append(x*1000)
#
in_degree=nx.in_degree_centrality(NH)
# node_sizes=[]
# for x in in_degree.values():
#     node_sizes.append(x*1000)

out_degree=nx.out_degree_centrality(NH)
# node_sizes=[]
# for x in out_degree.values():
#     node_sizes.append(x*1000)

betweenness=nx.betweenness_centrality(NH, k=None, normalized=True, weight=None, endpoints=False, seed=None)
# node_sizes=[]
# for x in betweenness.values():
#     node_sizes.append(x*1000)

page_rank= nx.pagerank(NH, alpha=0.8)
# node_sizes=[]
# for x in page_rank.values():
#     node_sizes.append(x*1000)


closeness=nx.closeness_centrality(NH)
# node_sizes=[]
# for x in closeness.values():
#     node_sizes.append(x*1000)
#

# nx.draw(NH, node_color=color_map,node_size=node_sizes, with_labels=False)
# # # pos = nx.spring_layout(G)
# plt.show()

# degree_sequence = sorted([d for n, d in NH.in_degree()], reverse=True)  # degree sequence
# print("degree",degree_sequence)
# degreeCount = collections.Counter(degree_sequence)
# deg, cnt = zip(*degreeCount.items())
# fig, ax = plt.subplots()
# plt.bar(deg, cnt, width=0.80, color="b")
# plt.title("Degree Histogram")
# plt.ylabel("Count")
# plt.yscale('log')
# plt.xlabel("Degree")
# plt.xscale('log')
# plt.show()


#מטלה 3
#יצירת גרפים אקראיים
#erdos
# ERG = nx.erdos_renyi_graph(len(nodes), 0.0083, seed=None, directed=False)
# # nx.draw(ERG, with_labels=False)
# # plt.show()
# print("nodes:",len(list(ERG.nodes)))
# print("edges:",len(list(ERG.edges)))

#gilbart
# a=int(scipy.special.binom(len(nodes), 2)*0.0083)
# C=nx.dense_gnm_random_graph(len(nodes),len(edges))
# # nx.draw(C, with_labels=False)
# # plt.show()
# print("nodes:",len(list(C.nodes)))
# print("edges:",len(list(C.edges)))

#configuration
# degrees = []
# degree_list = NH.degree(original_nodes)
# for d in degree_list:
#     degrees.append(d[1])
#
# print(degrees)
# CM = nx.configuration_model(degrees, create_using=None, seed=None)
# nx.draw(CM, with_labels=False)
# plt.show()
# print("nodes:",len(list(CM.nodes)))
# print("edges:",len(list(CM.edges)))
# התפלגות דרגות
# degree_sequence = sorted([d for n, d in NH.degree()], reverse=True)  # degree sequence
# print("degree",degree_sequence)
# degreeCount = collections.Counter(degree_sequence)
# deg, cnt = zip(*degreeCount.items())
# p=[]
# for x in cnt:
#     p.append(x/len(nodes))
# print("cnt",cnt)
# print("probabily",p)
# fig, ax = plt.subplots()
# plt.bar(deg, p, width=0.80, color="b")
# plt.title("Degree Histogram")
# plt.ylabel("probability")
# plt.xlabel("Degree")
# plt.xscale('log')
# plt.yscale('log')
# plt.show()

# sns.distplot(random.exponential(size=1000), hist=False)
# plt.show()

#רכיבי קשירות בגרפים האקראיים- כי הם יצאו לא קשירים
#רכיב קשירות הכי גדול בתוך ארדוס
# b = sorted(nx.connected_components(ERG), key=len, reverse=True)
# G2 = ERG.subgraph(b[0])
# nodes=list(G2.nodes)
# edges=list(G2.edges)
# print("largest connected components nodes",nodes)
# print("largest connected components edges",edges)
# print("num of nodes and edges", len(nodes),len(edges))
# nx.draw(G2,with_labels=False)
# plt.show()
#רכיב קשירות הכי גדול בתוך גילברט
# b = sorted(nx.connected_components(C), key=len, reverse=True)
# G3 = C.subgraph(b[0])
# nodes=list(G3.nodes)
# edges=list(G3.edges)
# print("largest connected components nodes",nodes)
# print("largest connected components edges",edges)
# print("num of nodes and edges", len(nodes),len(edges))
# nx.draw(G3,with_labels=False)
# plt.show()

#רכיב קשירות הכי גדול בקונפיג
# b = sorted(nx.connected_components(CM), key=len, reverse=True)
# G4 = CM.subgraph(b[0])
# nodes=list(G4.nodes)
# edges=list(G4.edges)
# print("largest connected components nodes",nodes)
# print("largest connected components edges",edges)
# print("num of nodes and edges", len(nodes),len(edges))
# nx.draw(G4,with_labels=False)
# plt.show()

#ממוצע מסלול
# print(nx.average_shortest_path_length(NH))
# print(nx.average_shortest_path_length(G2))
# print(nx.average_shortest_path_length(G3))
#print(nx.average_shortest_path_length(G4))

#ממוצע דרגות
# print("degree avg")
# degree_list=NH.degree(original_nodes)
# cnt=0
# for x in degree_list:
#     cnt+=x[1]
# avg=cnt/len(original_nodes)
# print(avg)
#
# degree_list=ERG.degree(list(ERG.nodes))
# cnt=0
# for x in degree_list:
#     cnt+=x[1]
# avg=cnt/len(list(ERG.nodes))
# print(avg)
#
# degree_list=C.degree(list(C.nodes))
# cnt=0
# for x in degree_list:
#     cnt+=x[1]
# avg=cnt/len(list(C.nodes))
# print(avg)

# degree_list=CM.degree(list(CM.nodes))
# cnt=0
# for x in degree_list:
#     cnt+=x[1]
# avg=cnt/len(list(CM.nodes))
# print(avg)


#ניסוי יצירת גרף רק משתמשים 1
DG = nx.DiGraph()

only_users=[]
only_claims=[]
for node in NH:
    if node<1000000:
        only_claims.append(node)
    elif node >1000000:
        only_users.append(node)  # users

# print("####################################33333")
# print(only_users)
# print(only_claims)

DG.add_nodes_from(only_users)

for l in only_claims:
    claims_out = list(NH.successors(l))
    claims_in = list(NH.predecessors(l))
    for x in claims_in:
        for y in claims_out:
            DG.add_edge(x, y)

color_map = []
for node in DG:
    if node ==1240250000000000000:
        color_map.append('yellow')
    elif node==1242960000000000000:
        color_map.append('pink')
    elif node < 1000000:
        color_map.append('red')  # articles
    else:
        color_map.append('green')  # users
# nx.draw(DG, node_color=color_map,  with_labels=False)
# plt.show()
print("nodes:",len(list(DG.nodes)), "edges:",len(list(DG.edges)))
# print("diameter",nx.diameter(DG.to_undirected()))
# print("average",nx.average_shortest_path_length(DG))

# התפלגות דרגות
# degree_sequence = DG.in_degree()
# print(degree_sequence)
# degree_sequence = sorted([d for n, d in DG.in_degree()], reverse=True)  # degree sequence
# print("degree", degree_sequence)
# degreeCount = collections.Counter(degree_sequence)
# deg, cnt = zip(*degreeCount.items())
# print("cnt",cnt)
# fig, ax = plt.subplots()
# plt.bar(deg, cnt, width=0.80, color="b")
# plt.title("Degree Histogram")
# plt.ylabel("count")
# plt.xlabel("Degree")
# # plt.xscale('log')
# # plt.yscale('log')
# plt.show()
#
# #התפלגות עם נרמול של העמודות
# plt.hist(deg, bins=np.logspace(np.log10(1), np.log10(1000), 50), density=True, stacked=True, edgecolor='black')
# plt.gca().set_xscale("log")
# plt.gca().set_yscale("log")
# plt.show()
# x=np.array(deg)
# y=np.array(cnt)
#
# #Applying a linear fit with .polyfit()
# fit = np.polyfit(x,y,1)
# ang_coeff = fit[0]
# intercept = fit[1]
# print(fit)
# fit_eq = ang_coeff*x + intercept  #obtaining the y axis values for the fitting function
# print(fit_eq)
# #Plotting the data
# fig = plt.figure()
# ax = fig.subplots()
# ax.plot(x, fit_eq,color = 'r', alpha = 0.5, label = 'Linear fit')
# ax.scatter(x,y,s = 5, color = 'b', label = 'Data points') #Original data points
# ax.set_title('Linear fit ')
# ax.legend()
# # plt.xscale('log')
# # plt.yscale('log')
# plt.show()
#
#




degree_sequence=DG.in_degree()
print(degree_sequence)
degree_sequence = sorted([d for n, d in DG.in_degree()], reverse=True)  # degree sequence
print("degree", degree_sequence)



page_rank=nx.pagerank(DG, alpha=0.8)
a=dict(sorted(page_rank.items(), reverse=True, key=lambda item: item[1]))
print("page rank",a)

closeness=nx.closeness_centrality(DG)
a=dict(sorted(closeness.items(), reverse=True, key=lambda item: item[1]))
print("closeness",a)
# key=list(a.keys())
# value=list(a.values())
# fig, ax = plt.subplots()
# # ax.fmt_ydata = millions
# plt.plot(key, value, 'o')
# plt.show()


#configuration
# degrees = []
# degree_list = DG.degree(original_nodes)
# for d in degree_list:
#     degrees.append(d[1])
# print(degrees)
# CM = nx.configuration_model(degrees, create_using=None, seed=None)
# # nx.draw(CM, with_labels=False)
# # plt.show()
# print("nodes:",len(list(CM.nodes)))
# print("edges:",len(list(CM.edges)))

#erdos
# ERG = nx.erdos_renyi_graph(len(list(DG.nodes)), 0.56, seed=None, directed=False)
# # nx.draw(ERG, with_labels=False)
# # plt.show()
# print("nodes:",len(list(ERG.nodes)))
# print("edges:",len(list(ERG.edges)))

clustering=nx.clustering(DG, nodes=None, weight=None)
a=dict(sorted(clustering.items(), reverse=True, key=lambda item: item[1]))
print("clustering",a)

print(nx.transitivity(DG))
