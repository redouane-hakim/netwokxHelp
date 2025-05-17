import matplotlib.pyplot as plt
import networkx as nx

# please install requirements : the libraries 


#;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! READ ALL COMMENTS !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::


#there is 4 type of Graph() :  undirected (no arrow) Directed(Arrow)
#                              MultiunDirected(two node can have multi edges , no arrow) 
#                              MultiDirected(two node can have multi edges ,arrow): automata
G = nx.MultiDiGraph()
edge_list = [(1, 2, {'w': 'A1'}), (2, 1, {'w': 'A2'}), (2, 3, {'w': 'B'}),
             (3, 1, {'w': 'C'}),
             (3, 4, {'w': 'D1'}), (4, 3, {'w': 'D2'}), (1, 5, {'w': 'E1'}),
             (5, 1, {'w': 'E2'}),
             (3, 5, {'w': 'F'}), (5, 4, {'w': 'G'})]
G.add_edges_from(edge_list)
#do the  .add_edge if you use a loop

pos = nx.spring_layout(G, seed=5)
#you can add more to the layout to be more concise 

fig, ax = plt.subplots()
#this is optional not needed for one single plot

nx.draw_networkx_nodes(G, pos, ax=ax)  #ax is optional  in all code 
nx.draw_networkx_labels(G, pos, ax=ax)




#create image func
fig.savefig("1.png", bbox_inches='tight', pad_inches=0)

# the lines between the nodes 

curved_edges = [(u,v,k,d) for (u,v,k,d) in G.edges(keys=True,data='w') if (v,u) in G.edges()]

#add a logic that will change this you need the curved line include the same nodes dfferent edge value 

straight_edges = list(set(list(G.edges(keys=True,data='w'))) - set(curved_edges))

# drawings you can add more design : here is how you can  add : arrow=true  arrowstyle ='-|>'
nx.draw_networkx_edges(G, pos, ax=ax, edgelist=straight_edges)

#curve ratio
arc_rad = 0.25

# connnectionstyle is how the edge  or how curvated is  ++angles ++curve
nx.draw_networkx_edges(G, pos, ax=ax, edgelist=curved_edges,
                       connectionstyle=f'arc3, rad = {arc_rad}')

#create image func
fig.savefig("2.png", bbox_inches='tight', pad_inches=0)

# this is the trick here to make the labels curvated by the same angle as the edge

#sparated curved / straight 



curved_edge_labels = {tuple(edge): f"{attr}" for *edge,attr in curved_edges}
straight_edge_labels=edge_labels = {tuple(edge): f"{attr}" for *edge,attr in straight_edges}
nx.draw_networkx_edge_labels(G, 
                             pos, 
                             curved_edge_labels,
                             label_pos=0.5,
                             bbox={"alpha": 0},
                             connectionstyle=f'arc3, rad = {arc_rad}',
                             ax=ax)
nx.draw_networkx_edge_labels(G, 
                             pos, 
                             straight_edge_labels,
                             label_pos=0.5,
                             bbox={"alpha": 0},
                             ax=ax)

#create image func
fig.savefig("3.png", bbox_inches='tight', pad_inches=0)


# the axe are optional you can plot it normally without the fig,ax this is used for educationnal purpose only 
# if you run the code you can see  3 image  
