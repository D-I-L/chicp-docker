# Google Anlytics
#GOOGLE_ANALYTICS_PROPERTY_ID = 'UA-324292-13'
#GOOGLE_ANALYTICS_TRACKING_STYLE = 2
#GOOGLE_ANALYTICS_DOMAIN = 'http://www.chicp.org'

#RECAPTCHA_KEY = '6LdpOBATAAAAAFwGyYPXqDlMTNpiC0F9wq4L8O7U';
#RECAPTCHA_SECRET = '6LdpOBATAAAAADRs20SRCh_mZot7WIHUUYw-42Ye';

RECAPTCHA_KEY = '6Lfx7BcTAAAAAM4ITVqz-jjXvhpAtQJkVNBUqlvs';
RECAPTCHA_SECRET = '6Lfx7BcTAAAAAKoaAnKDjCj6xER431A5XM8QRqFb';

# SMTP
DEFAULT_FROM_EMAIL = 'chicp-feedback@cimr.cam.ac.uk'
SERVER_EMAIL = 'chicp-feedback@cimr.cam.ac.uk'
EMAIL_HOST = 'email-smtp.eu-west-1.amazonaws.com'
EMAIL_HOST_USER = 'AKIAI6A2ZN5MYBW4GZJA'  # or 'user@gmail.com'
EMAIL_HOST_PASSWORD = 'AmMHQ4iXLtRK8szpz09kLCn2o+NqndeEDoMLfZhJLVPd'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_PORT = 25
EMAIL_USE_TLS = True
AWS_SES_REGION_NAME = 'eu-west-1'
AWS_SES_REGION_ENDPOINT = 'email.eu-west-1.amazonaws.com'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'chicp_authdb',
        'USER': 'webuser',
        'PASSWORD': 'webuser',
        'HOST': 'postgres',
        'PORT': '5432',
        'TEST': {
                'NAME': 'auto_tests',
            },
        },
}

AUTH_DB = 'default'
INCLUDE_USER_UPLOADS = False
ADMIN_URL_PATH = 'pydginadmin'
ELASTIC_PERMISSION_MODEL_APP_NAME = 'elastic'

ELASTIC = {
    'default': {
        'ELASTIC_URL': ['http://cp_elasticsearch:9200/'],
        'IDX': {
		'MARKER': {
               'name': 'dbsnp138'
           	},
                'CP_STATS_UD': {
                'name': 'cp:hg19_userdata_bed',
                'label': 'User Data',
                'idx_type': {},
                'data_type': 'log10p',
                
                },
                'CP_STATS_GWAS': {
                'name': 'cp:hg19_gwas_bed',
                'label': 'GWAS Statistic',
                'idx_type': {
                    'GWAS-BARRETT': {'label': 'T1D - Barrett et al.', 'type': 't1d_barrett', 'auth_public':True},
                },
                 'data_type': 'log10p',
            },
            'CP_TARGET_MIFSUD': {'name': 'cp:hg19_mifsud_chicago_pm', 'label': 'Mifsud et al.', 'auth_public': True},
        },
        'TEST': 'auto_tests',
        'REPOSITORY': 'my_backup',
        'TEST_REPO_DIR': '~/pydgin/pydgin/elastic/repos/test_snapshot/',
    }
}






