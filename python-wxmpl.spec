%define module  wxmpl
%define name 	python-%{module}
%define version 1.2.9
%define release %mkrel 3

Summary: 	Painless matplotlib embedding in wxPython
Name: 	 	%{name}
Version: 	%{version}
Release: 	%{release}
Source0: 	%{module}-%{version}.tar.bz2
License: 	BSD-like
Group: 	 	Development/Python
Url: 		http://agni.phys.iit.edu/~kmcivor/wxmpl/
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
BuildRequires:	python-devel
Requires:  	python-matplotlib, wxPython

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
rm -rf %{buildroot}
%__python setup.py install --root=%{buildroot} --record=INSTALLED_FILES

%clean
rm -rf %{buildroot}

%files -f INSTALLED_FILES
%defattr(-,root,root)
%doc README.txt LICENSE.txt ChangeLog tutorial/ demos/

