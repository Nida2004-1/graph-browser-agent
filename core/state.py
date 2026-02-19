class AgentState:
    def __init__(self):
        self.action_history = []
        self.extracted_data = {}
        self.errors = []
        self.dom_snapshot = None
        self.human_feedback = None
        self.current_step = None
