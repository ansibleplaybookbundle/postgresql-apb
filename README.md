postgresql-apb
======================

[![Build Status](https://travis-ci.org/ansibleplaybookbundle/postgresql-apb.svg?branch=master)](https://travis-ci.org/openshift/ansible-service-broker)

An apb for deploying [PostgreSQL](https://www.postgresql.org).

## What it does
* Deploys 1 postgresql container.

## Requirements
* N/A

## Provision Parameters
* postgresql_password, Optional. Postgresql Admin database password. A randomly generated string will be set if empty.
* postgresql_version, Required, default '9.6', Postgresql version. 9.4, 9.5, and 9.6 are supported.

## Bind Parameters
* client_name, Required. Name of the client to bound. A new database will be created with this name
* client_user, Required. Client user name to create and grant permissions on the newly created database.
* client_password, Optional. Client user password. A randomly generated string will be set if empty.

## Running the application
`docker run --rm --net=host -v $HOME/.kube:/opt/apb/.kube:z -u $UID docker.io/ansibleplaybookbundle/postresql-apb provision`

## Tearing down the application
`docker run -e "OPENSHIFT_TARGET=<openshift_target>" -e "OPENSHIFT_TOKEN=<token>" ansibleplaybookbundle/postgresql-apb deprovision`
