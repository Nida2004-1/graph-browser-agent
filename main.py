from core.state import AgentState
from core.nodes import PlannerNode, BrowserActionNode, RecoveryNode, ValidatorNode, HumanApprovalNode
from core.graph_executor import GraphExecutor
import importlib.util
import os

# Load `browser/playwright_wrapper.py` directly to avoid import shadowing by a top-level
# `browser.py` file that may exist in the working directory.
spec = importlib.util.spec_from_file_location(
    "playwright_wrapper",
    os.path.join(os.path.dirname(__file__), "browser", "playwright_wrapper.py"),
)
playwright_wrapper = importlib.util.module_from_spec(spec)
spec.loader.exec_module(playwright_wrapper)
BrowserWrapper = playwright_wrapper.BrowserWrapper



# Dummy browser placeholder (Person B will replace)
class DummyBrowser:
    pass

def main():
    state = AgentState()
    browser = BrowserWrapper()



    nodes = {
        "planner": PlannerNode(),
        "browser_action": BrowserActionNode(),
        "recovery": RecoveryNode(),
        "validator": ValidatorNode(),
        "human": HumanApprovalNode(),
        "end": None
    }

    executor = GraphExecutor(nodes)
    executor.run(state, browser)

    print("\nFinal State:")
    print("Actions:", state.action_history)
    print("Errors:", state.errors)
    print("Human feedback:", state.human_feedback)
    # Keep browser open until user decides to close it so it doesn't close automatically
    try:
        decision = input("Press Enter to close the browser and exit, or type 'keep' to leave it open: ")
    except EOFError:
        decision = ""

    if decision.strip().lower() != "keep":
        try:
            browser.close()
        except Exception:
            pass

if __name__ == "__main__":
    main()
    
