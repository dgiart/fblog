from rolepermissions.roles import AbstractUserRole

class SuperUser(AbstractUserRole):
    available_permissions = {
        'create': True,
    }
class TeamLeader(AbstractUserRole):
    available_permissions = {
        'create': True,
    }

class Analyst(AbstractUserRole):
    available_permissions = {
        'edit': True,
    }
