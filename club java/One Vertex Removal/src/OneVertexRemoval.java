import java.util.*;

public class OneVertexRemoval {
    public static void main(String[] args) {
        Graph graph = new Graph();
        Vertex A = graph.addVertex("A");
        Vertex B = graph.addVertex("B");
        Vertex C = graph.addVertex("C");
        Vertex D = graph.addVertex("D");
        Vertex E = graph.addVertex("E");
        Vertex F = graph.addVertex("F");
        graph.addEdge(A, B);
        graph.addEdge(A, C);
        graph.addEdge(B, C);
        graph.addEdge(B, D);
        graph.addEdge(F, D);
        graph.addEdge(E, D);

        graph.printAdjacencyList();
        System.out.println(graph.isConnected());

        removeOneVertexWithDFS(graph, A);
        graph.printAdjacencyList();
        System.out.println(graph.isConnected());

        removeOneVertexWithDFS(graph, A);
        graph.printAdjacencyList();
        System.out.println(graph.isConnected());
    }

    public static void removeOneVertexWithDFS(Graph graph, Vertex root) {
        Set<Vertex> visited = new HashSet<>();
        Stack<Vertex> stack = new Stack<>();
        stack.push(root);
        while(!stack.isEmpty()){
            Vertex top = stack.pop();
            if(!visited.contains(top)){
                visited.add(top);
                if(graph.getAdjVertices(top).stream().allMatch(visited::contains)) {
                    graph.removeVertex(top);
                    break;
                }
                for (Vertex v:graph.getAdjVertices(top)){
                    stack.push(v);
                }
            }
        }
    }
}

class Vertex {
    String label;
    Vertex(String label) {
        this.label = label;
    }
}


class Graph {
    /**
    {A -> { B, C },
     B -> { A },
     C -> { A }}
     **/
    Map<Vertex, List<Vertex>> adjVertices = new HashMap<>();

    List<Vertex> getAdjVertices(Vertex v) {
        return adjVertices.get(v);
    }

    Vertex addVertex(String label) {
        Vertex key = new Vertex(label);
        adjVertices.putIfAbsent(key, new ArrayList<>());
        return key;
    }

    void removeVertex(Vertex v) {
        adjVertices.values().stream().forEach(e -> e.remove(v));
        adjVertices.remove(v);
    }

    void addEdge(Vertex v1, Vertex v2) {
        adjVertices.putIfAbsent(v1, new ArrayList<>());
        adjVertices.putIfAbsent(v2, new ArrayList<>());

        adjVertices.get(v1).add(v2);
        adjVertices.get(v2).add(v1);
    }

    void removeEdge(String label1, String label2) {
        Vertex v1 = new Vertex(label1);
        Vertex v2 = new Vertex(label2);
        if(adjVertices.containsKey(v1)) {
            adjVertices.get(v1).remove(v2);
        }
        if(adjVertices.containsKey(v2)) {
            adjVertices.get(v2).remove(v1);
        }
    }

    void printAdjacencyList() {
        for (Map.Entry<Vertex, List<Vertex>> entry : adjVertices.entrySet()) {
            System.out.print(entry.getKey().label + " -> ");
            List<Vertex> neighbors = entry.getValue();
            for (int i = 0; i < neighbors.size(); i++) {
                System.out.print(neighbors.get(i).label);
                if (i < neighbors.size() - 1) {
                    System.out.print(", ");
                }
            }
            System.out.println("");
        }
        System.out.println("");
    }

    boolean isConnected() {
        if (adjVertices.isEmpty()) {
            return true;
        }

        Set<Vertex> visited = new HashSet<>();
        Vertex startVertex = adjVertices.keySet().iterator().next();
        dfs(startVertex, visited);

        return visited.size() == adjVertices.size();
    }

    void dfs(Vertex vertex, Set<Vertex> visited) {
        visited.add(vertex);
        List<Vertex> neighbors = adjVertices.getOrDefault(vertex, Collections.emptyList());
        for (Vertex neighbor : neighbors) {
            if (!visited.contains(neighbor)) {
                dfs(neighbor, visited);
            }
        }
    }
}