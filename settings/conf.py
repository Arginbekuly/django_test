from decouple import config



#-------------Env id--------------
#
ENV_POSSIBLE_OPTIONS = (
    "local",
    "prod",
)

ENV_ID = config("DJANGORLAR_ENV_ID",default="local", cast =str)
SECRET_KEY = 'django-insecure-w7f#2qz^pb8q9sw#)*as*co2dfry^u!6!cu(-qr9zx^)x(-rd!'