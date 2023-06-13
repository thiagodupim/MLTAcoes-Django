from rolepermissions.roles import AbstractUserRole

class Gerente(AbstractUserRole):
    available_permissions = {'criar_acoes': True, 'editar_acoes': True, 'deletar_acoes': True}

class Cliente(AbstractUserRole):
    available_permissions = {'ver_acoes': True}