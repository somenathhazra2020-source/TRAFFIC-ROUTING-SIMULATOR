# Traffic Routing Simulator Web App (Dijkstra's Algorithm)

A simple Flask-based web app to simulate traffic routing using Dijkstra's algorithm.

## Features

- Interactive web UI to select start/end nodes
- Finds shortest path and distance
- Easy to extend road map

## Requirements

- Python 3.x
- Flask (`pip install flask`)

## Setup & Run

1. **Clone or copy files to your repository**
2. **Install Flask**

```sh
pip install flask
```

3. **Folder structure should be:**
```
traffic-routing-simulator/
├── app.py
└── templates/
    └── index.html
├── README.md
```

4. **Run the app:**

```sh
python app.py
```

5. **Open your browser and go to:** [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Customizing the Road Network

Edit the `build_sample_graph()` function in `app.py` to add/remove nodes and edges.

## Example

Select "A" as start and "F" as end node, then click "Find Shortest Path".

---

Want advanced features or visualization? Open an issue or request!
