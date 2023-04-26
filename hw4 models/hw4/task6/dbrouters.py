# from . models import Customer, Product


class DBRouter:

    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'task6':
            return 'postgres'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'task6':
            return 'postgres'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        # db_set = {'postgres'}
        # if obj1._state.db in db_set and obj2._state.db in db_set:
        #     return True
        if obj1._meta.app_label == 'task6' or obj2._meta.app_label == 'task6':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'task6':
            return True
        return None

