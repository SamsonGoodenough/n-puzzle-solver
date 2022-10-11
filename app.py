import dash
import dash_cytoscape as cyto
import dash_html_components as html
from lib.graph import Graph

cyto.load_extra_layouts()

graph = Graph([5, 1, 2, 3, 7, 4, 6, 8, 0])
goal = graph.findGoalState()


def getGraph():
    nodes = []
    edges = []
    queue = [graph.root]
    maxClr = goal.pathCost
    while len(queue) > 0:
        node = queue.pop(0)

        for child in node.children:
            queue.append(child)

        if str(node) == str(graph.root):
            nodeColor = "rgb(0, 0, 255)"
        elif str(node) == str(goal):
            nodeColor = "rgb(0, 255, 0)"
        else:
            nodeColor = "rgb(255, %s, 50)" % (255 - node.pathCost / maxClr * 255)

        nodes.append(
            {
                "data": {
                    "id": str(node.state.id),
                    "label": str(node.cost),
                    "cost": node.cost,
                    "pathCost": node.pathCost,
                    "clr": nodeColor,
                }
            }
        )
        if node.parent != None:
            edges.append(
                {
                    "data": {
                        "source": str(node.parent.state.id),
                        "target": str(node.state.id),
                    }
                }
            )

    return nodes + edges


app = dash.Dash(__name__)
elements = getGraph()

app.layout = html.Div(
    [
        cyto.Cytoscape(
            id="cytoscape",
            elements=elements,
            layout={
              "name": "cose",
              "animate": False,
              "nodeRepulsion": 8000,
              "nodeOverlap": 10,
              "directed": True
            },
            style={"width": "95vw", "height": "95vh"},
            stylesheet=[
                {
                    "selector": "node",
                    "style": {"label": "data(cost)", "background-color": "data(clr)"},
                },
                {
                    "selector": "edge",
                    "style": {
                        "curve-style": "bezier",
                        "target-arrow-shape": "triangle",
                    },
                },
            ],
        )
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
