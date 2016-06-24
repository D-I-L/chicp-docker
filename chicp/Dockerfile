FROM python:3.5-onbuild
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir -r /usr/src/app/src/chicp/chicp/requirements.txt
RUN ln -s /usr/src/app/data_access_agreement.html /usr/src/app/src/pydgin-auth/pydgin_auth/templates/data_access_agreement.html 
RUN pip install django-analytical
RUN django-admin startproject projCHICP
RUN cd projCHICP
RUN mkdir projCHICP/tmp
RUN chmod 777 projCHICP/tmp
RUN mkdir projCHICP/projCHICP/apache
RUN mkdir projCHICP/projCHICP/static
