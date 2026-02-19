class Node:
    def execute(self, state, browser):
        raise NotImplementedError

class PlannerNode(Node):
    def execute(self, state, browser):
        print("Planning next step...")

        plan = ["open_page", "fill_form", "submit"]
        
        if not state.action_history:
            state.current_step = plan[0]
        elif state.current_step == "open_page":
            state.current_step = plan[1]
        elif state.current_step == "fill_form":
            state.current_step = plan[2]
        else:
            return "end"

        return "browser_action"

class BrowserActionNode(Node):
    def execute(self, state, browser):
        print(f"Executing: {state.current_step}")
        state.action_history.append(state.current_step)

        try:
            if state.current_step == "open_page":
                browser.open_page("https://the-internet.herokuapp.com/login")

            elif state.current_step == "fill_form":
                browser.type_text("#username", "tomsmith")
                browser.type_text("#password", "SuperSecretPassword!")

            elif state.current_step == "submit":
                browser.click("button[type='submit']")

        except Exception as e:
            state.errors.append(str(e))
            print("Error detected:", e)
            return "recovery"

        return "validator"


class RecoveryNode(Node):
    def execute(self, state, browser):
        print("Recovery triggered...")
        state.errors.append("Recovered from failure")
        return "planner"

class HumanApprovalNode(Node):
    def execute(self, state, browser):
        decision = input("Approve next action? (y/n): ")
        state.human_feedback = decision

        if decision.lower() == "n":
            return "end"

        return "browser_action"

class ValidatorNode(Node):
    def execute(self, state, browser):
        print("Validating last action...")

        if state.errors:
            print("Validation failed")
            return "recovery"

        print("Validation passed")
        return "planner"
