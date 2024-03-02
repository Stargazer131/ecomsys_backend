class CheckerRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'cart':
            return 'cart_db'
        elif model._meta.app_label == 'product':
            return 'product_db'
        return 'default'
    

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'cart':
            return 'cart_db'
        elif model._meta.app_label == 'product':
            return 'product_db'
        return 'default'
    

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'cart' or obj2._meta.app_label == 'cart':
            return True
        elif 'cart' not in [obj1._meta.app_label, obj2._meta.app_label]:
            return True
        elif obj1._meta.app_label == 'product' or obj2._meta.app_label == 'product':
            return True
        elif 'product' not in [obj1._meta.app_label, obj2._meta.app_label]:
            return True
        return False
    

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'cart':
            return db == 'cart_db'
        elif app_label == 'product':
            return db == 'product_db'
        return None