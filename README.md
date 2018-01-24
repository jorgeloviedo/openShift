# Flask Sample Application

This repository provides a sample Python web application implemented using the Flask web framework and hosted using ``gunicorn``. It is intended to be used to demonstrate deployment of Python web applications to OpenShift 3.

## Implementation Notes

This sample Python application relies on the support provided by the default S2I builder for deploying a WSGI application using the ``gunicorn`` WSGI server. The requirements which need to be satisfied for this to work are:

* The WSGI application code file needs to be named ``wsgi.py``.
* The WSGI application entry point within the code file needs to be named ``application``.
* The ``gunicorn`` package must be listed in the ``requirements.txt`` file for ``pip``.

In addition, the ``.s2i/environment`` file has been created to allow environment variables to be set to override the behaviour of the default S2I builder for Python.

* The environment variable ``APP_CONFIG`` has been set to declare the name of the config file for ``gunicorn``.

## Deployment Steps

To deploy this sample Python web application from the OpenShift web console, you should select ``python:2.7``, ``python:3.3``, ``python:3.4`` or ``python:latest``, when using _Add to project_. Use of ``python:latest`` is the same as having selected the most up to date Python version available, which at this time is ``python:3.4``.

The HTTPS URL of this code repository which should be supplied to the _Git Repository URL_ field when using _Add to project_ is:

* https://github.com/OpenShiftDemos/os-sample-python.git

If using the ``oc`` command line tool instead of the OpenShift web console, to deploy this sample Python web application, you can run:

```
oc new-app https://github.com/OpenShiftDemos/os-sample-python.git
```

In this case, because no language type was specified, OpenShift will determine the language by inspecting the code repository. Because the code repository contains a ``requirements.txt``, it will subsequently be interpreted as including a Python application. When such automatic detection is used, ``python:latest`` will be used.

If needing to select a specific Python version when using ``oc new-app``, you should instead use the form:

```
oc new-app python:2.7~https://github.com/OpenShiftDemos/os-sample-python.git
```

# Open Shift

###### OpenShift es Kubernetes para empresas
* https://www.redhat.com/es/topics/containers/what-is-kubernetes

###### Red Hat® OpenShift es una plataforma de aplicaciones de contenedores que aporta Docker y Kubernetes a la empresa.
* https://www.openshift.com/
* https://www.redhat.com/es/technologies/cloud-computing/openshift
	``Red Hat OpenShift Container Platform``
	``Red Hat OpenShift Dedicated``
	``Red Hat OpenShift Online``

###### Instalación y configuración del cliente de Openshift - Tunel para el CLI de Openshift
* https://torusware.com/es/blog/2017/02/openshift-origin-jenkins-almacenamiento-persistente-glusterfs/

###### OpenShift Origin is a distribution of Kubernetes optimized for continuous application development and multi-tenant deployment. OpenShift adds developer and operations-centric tools on top of Kubernetes to enable rapid application development, easy deployment and scaling, and long-term lifecycle maintenance for small and large teams.
* https://github.com/openshift/origin
* https://github.com/openshift/origin/releases

###### Docker, Kubernetes, Openshift y Openstack para mi abuela
* https://www.youtube.com/watch?v=DtyAJmIyxPo
* open shift 27 minutos 23 segundos del video

###### Openshift quickstart: Django
* https://github.com/openshift/django-ex

###### Interactive Learning Portal
* https://learn.openshift.com/

###### Download OpenShift Origin
* https://www.openshift.org/download.html#oc-platforms

###### Installation and Configuration - Advanced Installation
* https://docs.openshift.org/latest/install_config/install/advanced_install.html

###### Create and Build an Image Using the Web Console
* https://docs.openshift.org/latest/getting_started/developers_console.html

###### Python Template Repository Layout
* https://developers.openshift.com/languages/python/repository-layout.html

###### Getting Started with the Flask Microframework
* https://developers.openshift.com/languages/python/flask.html

###### Distribución de librerías Python con setup.py
* https://rukbottoland.com/blog/distribucion-de-librerias-python-con-setuppy/
* https://github.com/rukbotto/starwars-ipsum/