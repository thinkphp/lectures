---
layout: post
disqus: y
title: Detect Cycle in a Directed Graph
---

Detect Cycle in a Directed Graph
----------

Given a directed graph your task is to complete the method isCycle to detect if there is a cycle in the graph or not. You should not read any input from stdin/console. There are multiple test cases. For each test case, this method will be called individually.

Input (only to be used for Expected Output): The first line of the input contains an integer ‘T’ denoting the number of test cases. Then ‘T’ test cases follow. Each test case consists of two lines. Description of test cases is as follows: The First line of each test case contains two integers ‘N’ and ‘M’ which denotes the no of vertices and no of edges respectively. The Second line of each test case contains ‘M’ space separated pairs u and v denoting that there is an unidirected edge from u to v.

Output: The method should return true if there is a cycle else it should return false.

Constraints:
1 <= T <= 100
1 <= N, M <= 100
0 <=u , v <= N-1

Input: 2
2 2
0 1 0 0
4 3
0 1 1 2 2 3

Output:
1
0

In above first test case there is a graph with 2 vertices and 2 edges the first edge is from 0 to 1 and other edge is from 0 to 0 . In the second test case there is a graph with 3 vertices and 3 edges from 0 to 1 , 1 to 2 and 2 to 3

```c++

#include<bits/stdc++.h>
#define N 100
#define WHITE 0
#define GREY 1
#define BLACK 2

using namespace std;

class Graph {

      int V;
      list<int> *adj;
        
      public:
      Graph(int V);
      void addEdge(int v, int w);
      bool isCyclic();         
};

Graph::Graph(int V) {

      this->V = V;

      adj = new list<int>[V]; 
};

void Graph::addEdge(int v, int w){

       adj[v].push_back(w);
};

bool hasCycle(std::list<int> adj[], int colours[], int u) {

     colours[u] = GREY;

     for( const auto&v:adj[u] ) {

          switch( colours[v] ) {
            
                  case GREY: 

                       return true;         
                  case WHITE: 

                       if(hasCycle(adj, colours, v))   
                       return true;         
          }
     }

     colours[ u ] = BLACK;

     return false;     
}

bool Graph::isCyclic() {

    static int colours[N];

    for (int i = 0; i < V; i++) {

        colours[i] = WHITE;
    }

    for (int i = 0; i < V; i++) {

        if (colours[i] == 0) {

            if (hasCycle(adj, colours, i)) {

                return true;
            }
        }
    }

    return false;    
}


int main() {

     int nodes, edges, T;

     cin>>T;

     while(T--) {
 
     cin>>nodes>>edges;

     Graph *g = new Graph(nodes); 

     for(int i = 0; i < edges; ++i) {

             int u,v;

             cin>>u>>v;

             g->addEdge(u,v);
     } 

     cout<<g->isCyclic()<<endl; 

     }

return(0);



```
