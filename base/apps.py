from django.apps import AppConfig

# Configuration class for the 'base' app
class BaseConfig(AppConfig):
    # Sets the default field type for primary keys in the models
    default_auto_field = 'django.db.models.BigAutoField'
    # BigAutoField is an auto-incrementing 64-bit integer field used for primary keys by default

    name = 'base'
    # Specifies the name of the application (matches the app's directory name)
