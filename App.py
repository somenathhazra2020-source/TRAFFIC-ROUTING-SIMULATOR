from flask import Flask, render_template, request
import heapq

app = Flask(__name__)

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}

    def add_node(self, value):
        self.nodes.add(value)
        if value not in self.edges:
            self.edges[value] = {}

    def add_edge(self, from_node, to_node, distance):
        self.add_node(from_node)
        self.add_node(to_node)
        self.edges[from_node][to_node] = distance
        self.edges[to_node][from_node] = distance

    def neighbors(self, node):
        return self.edges[node].items()

def build_sample_graph():
    g = Graph()
    g.add_edge('A', 'B', 4)
    g.add_edge('A', 'C', 2)
    g.add_edge('B', 'C', 5)
    g.add_edge('B', 'D', 10)
    g.add_edge('C', 'E', 3)
    g.add_edge('E', 'D', 4)
    g.add_edge('D', 'F', 11)
    return g

def dijkstra(graph, start, end):
    queue = [(0, start, [])]
    seen = set()
    min_dist = {start: 0}
    while queue:
        (cost, node, path) = heapq.heappop(queue)
        if node in seen:
            continue
        path = path + [node]
        if node == end:
            return (cost, path)
        seen.add(node)
        for neighbor, weight in graph.neighbors(node):
            if neighbor in seen:
                continue
            prev = min_dist.get(neighbor, None)
            next_cost = cost + weight
            if prev is None or next_cost < prev:
                min_dist[neighbor] = next_cost
                heapq.heappush(queue, (next_cost, neighbor, path))
    return (float("inf"), [])

@app.route("/", methods=["GET", "POST"])
def index():
    g = build_sample_graph()
    nodes = sorted(g.nodes)
    result = None
    if request.method == "POST":
        start = request.form.get("start")
        end = request.form.get("end")
        if start in nodes and end in nodes:
            distance, path = dijkstra(g, start, end)
            if path:
                result = {
                    "path": " → ".join(path),
                    "distance": distance,
                    "start": start,
                    "end": end
                }
            else:
                result = {"error": f"No path found from {start} to {end}."}
        else:
            result = {"error": "Invalid nodes selected."}
    return render_template("index.html", nodes=nodes, result=result)

if __name__ == "__main__":
    app.run(debug=True)
