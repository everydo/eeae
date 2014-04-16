
class IWorkflowEngine:

    def __init__(self, obj):
        self.obj = obj

    def start(self):
        pass

    def list_tasks(self):
        pass

    def allowed_fields(self, pid):
        pass

    def disabled_fields(self, pid):
        pass

    def excute_action(self, step_name, action_name, as_principal=None, comment=""):
        pass

