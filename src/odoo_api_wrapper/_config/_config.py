from dotenvironment import DotEnvironment

env = DotEnvironment('ODOO_API_WRAPPER_')

class CONFIG:
    URL = env.variable('URL')
    API_KEY = env.variable('API_KEY')
    DATABASE = env.variable('DATABASE')
    LANG = env.variable('LANG', default= 'en_US')
