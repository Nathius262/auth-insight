from django.apps import AppConfig

class AuthenticationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'authentication'
    model = None

    def ready(self):
        from . import signals
        import joblib, os
        from django.conf import settings
        model_path = os.path.join(settings.BASE_DIR, 'xgb_model.pkl')
        AuthenticationConfig.model = joblib.load(model_path)
        #print(self.model)
