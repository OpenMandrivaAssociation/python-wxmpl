%define module  wxmpl
%define name 	python-%{module}
%define version 2.0.0
%define release %mkrel 2

Summary: 	Painless matplotlib embedding in wxPython
Name: 	 	%{name}
Version: 	%{version}
Release: 	%{release}
Source0: 	%{module}-%{version}.tar.gz
License: 	BSD-like
Group: 	 	Development/Python
Url: 		https://csrri.iit.edu/~wxmpl/
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
Requires:  	python-matplotlib-wx >= 0.98.1
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


%changelog
* Tue Oct 25 2011 Lev Givon <lev@mandriva.org> 2.0.0-2mdv2011.0
+ Revision: 707153
- Require python-matplotlib-wx.
- Update to 2.0.0.

* Thu Nov 04 2010 Funda Wang <fwang@mandriva.org> 1.3.1-2mdv2011.0
+ Revision: 593152
- update file list

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 1.3.1-2mdv2010.0
+ Revision: 442545
- rebuild

* Tue Feb 24 2009 Lev Givon <lev@mandriva.org> 1.3.1-1mdv2009.1
+ Revision: 344542
- Update to 1.3.1.

* Fri Jan 02 2009 Funda Wang <fwang@mandriva.org> 1.2.9-5mdv2009.1
+ Revision: 323407
- rebuild

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 1.2.9-4mdv2009.0
+ Revision: 259862
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 1.2.9-3mdv2009.0
+ Revision: 247710
- rebuild

* Sun Dec 16 2007 Lev Givon <lev@mandriva.org> 1.2.9-1mdv2008.1
+ Revision: 120766
- import python-wxmpl

