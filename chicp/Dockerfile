FROM python:3.5-onbuild
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install django-analytical
RUN django-admin startproject projCHICP
RUN cd projCHICP
RUN mkdir projCHICP/tmp
RUN chmod 777 projCHICP/tmp
RUN mkdir projCHICP/projCHICP/apache
RUN mkdir projCHICP/projCHICP/static
