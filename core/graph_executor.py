class GraphExecutor:
    def __init__(self, nodes):
        self.nodes = nodes

    def run(self, state, browser):
        current_node = "planner"

        while current_node != "end":
            print(f"\n--- Node: {current_node} ---")
            node = self.nodes[current_node]
            next_node = node.execute(state, browser)
            current_node = next_node

        print("Execution Finished.")
