#!/bin/bash

echo "going to sleep for 5 seconds ......."
sleep 5
sed -i 's|from transform import|from svgutils.transform import|' /usr/src/app/src/svgutils/src/svgutils/templates.py

find src -name "000*" -exec rm -rf {} \;

python projCHICP/manage.py makemigrations
python projCHICP/manage.py migrate
#python projCHICP/manage.py makemigrations pydgin_auth
#python projCHICP/manage.py migrate --fake-intial
python projCHICP/manage.py makemigrations elastic
python projCHICP/manage.py migrate elastic
python projCHICP/manage.py collectstatic --noinput

#subs for elastic2
#sed -i 's|2000000|10000|' /usr/src/app/src/chicp/chicp/views.py

#python projCHICP/manage.py runserver 0:9000
cd projCHICP
/usr/local/bin/gunicorn projCHICP.wsgi:application -w 2 -b :8000

