%if 0%{?copr}
%define build_timestamp .%(date +"%Y%m%d%H%M%%S")
%else
%define build_timestamp %{nil}
%endif

Name: 		postgresql-apb-role
Version:	1.0.8
Release:	1%{build_timestamp}%{?dist}
Summary:	Ansible Playbook for PostgreSQL APB

License:	ASL 2.0
URL:		https://github.com/ansibleplaybookbundle/RHSCL-PostgreSQL-APB
Source0:	https://github.com/ansibleplaybookbundle/RHSCL-PostgreSQL-APB/archive/%{name}-%{version}.tar.gz
BuildArch:  	noarch

%description
%{summary}

%prep
%setup -q -n %{name}-%{version}

%install
mkdir -p %{buildroot}/opt/apb/ %{buildroot}/opt/ansible/
mv playbooks %{buildroot}/opt/apb/actions
mv roles %{buildroot}/opt/ansible/roles

%files
%doc
/opt/apb/actions
/opt/ansible/roles

%changelog
* Fri Oct 13 2017 Jason Montleon <jmontleo@redhat.com> 1.0.8-1
- Ensure proper templating with quotes on image (dymurray@redhat.com)

* Fri Oct 13 2017 Jason Montleon <jmontleo@redhat.com> 1.0.7-1
- stop prefixing the repository with the registry and org twice
  (jmontleo@redhat.com)

* Tue Oct 10 2017 Jason Montleon <jmontleo@redhat.com> 1.0.6-1
- Update dockerfiles (david.j.zager@gmail.com)
- Bug 1500364 - Update apb.yml with all dependent images
  (david.j.zager@gmail.com)

* Thu Oct 05 2017 Jason Montleon <jmontleo@redhat.com> 1.0.5-1
- Add support to update a dev deployment to a prod deployment
  (jmontleo@redhat.com)
- Bug 1498571 - Remove image from APB (david.j.zager@gmail.com)

* Wed Oct 04 2017 Jason Montleon <jmontleo@redhat.com> 1.0.4-1
- Bug 1498185 - Move version label onto APB spec (dymurray@redhat.com)
- Fix nightly metadata (jmontleo@redhat.com)
- Update url for postgresql apb (david.j.zager@gmail.com)
- Bumped APB spec version to 1.0 (dymurray@redhat.com)
- Updated APB to include proper providerDisplayName metadata
  (dymurray@redhat.com)

* Tue Sep 19 2017 Jason Montleon <jmontleo@redhat.com> 1.0.3-1
- new package built with tito

* Mon Aug 21 2017 Jason Montleon <jmontleo@redhat.com> 1.0.2-1
- Fix rhscl-postgresql-apb deprovision (#116) (jmontleo@redhat.com)

* Fri Aug 18 2017 Jason Montleon <jmontleo@redhat.com> 1.0.1-1
- new package built with tito

