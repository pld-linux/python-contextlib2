#
# Conditional build:
%bcond_without	python2	# CPython 2.x module
%bcond_without	python3	# CPython 3.x module
%bcond_without	tests	# test target

Summary:	Backports and enhancements for the contextlib module
Summary(pl.UTF-8):	Backport oraz rozszerzenia dla modułu contextlib
Name:		python-contextlib2
Version:	0.6.0.post1
Release:	5
License:	PSF
Group:		Development/Languages/Python
#Source0Download: https://pypi.org/simple/contextlib2/
Source0:	https://files.pythonhosted.org/packages/source/c/contextlib2/contextlib2-%{version}.tar.gz
# Source0-md5:	d634281c2e61e575d8a68b9c56f8303a
URL:		https://contextlib2.readthedocs.io/
%if %{with python2}
BuildRequires:	python-devel >= 1:2.7
%if %{with tests}
# requires unittest.TestCase.assertRaisesRegex(), available since 3.2
BuildRequires:	python-unittest2
%endif
%endif
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.4
%endif
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
contextlib2 is a backport of the `standard library's contextlib module
<https://docs.python.org/3.5/library/contextlib.html> to earlier
Python versions.

contextlib module provides utilities for with-statement contexts.

%description -l pl.UTF-8
contextlib2 to backport modułu contextlib z biblioteki standardowej
(<https://docs.python.org/3.5/library/contextlib.html>) do starszych
wersji Pythona.

Moduł contextlib udostępnia narzędzia dla kontekstów ustalanych
instrukcją with.

%package -n python3-contextlib2
Summary:	Backports and enhancements for the contextlib module
Summary(pl.UTF-8):	Backport oraz rozszerzenia dla modułu contextlib
Group:		Development/Languages/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-contextlib2
contextlib2 is a backport of the `standard library's contextlib module
<https://docs.python.org/3.5/library/contextlib.html> to earlier
Python versions.

contextlib module provides utilities for with-statement contexts.

%description -n python3-contextlib2 -l pl.UTF-8
contextlib2 to backport modułu contextlib z biblioteki standardowej
(<https://docs.python.org/3.5/library/contextlib.html>) do starszych
wersji Pythona.

Moduł contextlib udostępnia narzędzia dla kontekstów ustalanych
instrukcją with.

%prep
%setup -q -n contextlib2-%{version}

%build
%if %{with python2}
%py_build

%{?with_tests:%{__python} test_contextlib2.py}
%endif

%if %{with python3}
%py3_build

%{?with_tests:%{__python3} test_contextlib2.py}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE.txt NEWS.rst README.rst
%{py_sitescriptdir}/contextlib2.py[co]
%{py_sitescriptdir}/contextlib2-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-contextlib2
%defattr(644,root,root,755)
%doc LICENSE.txt NEWS.rst README.rst
%{py3_sitescriptdir}/contextlib2.py
%{py3_sitescriptdir}/__pycache__/contextlib2.cpython-*.py[co]
%{py3_sitescriptdir}/contextlib2-%{version}-py*.egg-info
%endif
