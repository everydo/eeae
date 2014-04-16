
class IAcl:

    def __init__(self, obj):
        self.obj = obj

    def grant_role(self, role_id, pids):
        pass

    def deny_role(self, role_id, pids):
        pass

    def unset_role(self, role_id, pids):
        pass

    def check_permission(self, permission, pid):
        pass

    def get_role_pricipalss(self, role_id, include_inherited=False):
        pass

    def get_principal_roles(self, pid, include_inherited=False):
        pass
