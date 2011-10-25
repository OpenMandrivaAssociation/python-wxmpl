%define module  wxmpl
%define name 	python-%{module}
%define version 2.0.0
%define release %mkrel 1

Summary: 	Painless matplotlib embedding in wxPython
Name: 	 	%{name}
Version: 	%{version}
Release: 	%{release}
Source0: 	%{module}-%{version}.tar.gz
License: 	BSD-like
Group: 	 	Development/Python
Url: 		http://csrri.iit.edu/~wxmpl/
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
Requires:  	python-matplotlib >= 0.98.1
Requires:	wxPython >= 2.6.3.2
BuildRequires:	python

%description
The wxmpl module provides a matplotlib FigureCanvas with
user-interaction features like point-under-cursor and zooming in on a
selected area.  Support for creating stripcharts (i.e., plots that
update as their data changes) is also included.

%prep
%setup -q -n %{module}-%{version}

%build
%__python setup.py build

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=INSTALLED_FILES

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README.txt LICENSE.txt ChangeLog reference/ demos/
%_bindir/*
%py_puresitedir/*
