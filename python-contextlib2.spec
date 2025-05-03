#
# Conditional build:
%bcond_without	tests	# test target

Summary:	Backports and enhancements for the contextlib module
Summary(pl.UTF-8):	Backport oraz rozszerzenia dla modułu contextlib
Name:		python-contextlib2
Version:	0.6.0.post1
Release:	7
License:	PSF
Group:		Development/Languages/Python
#Source0Download: https://pypi.org/simple/contextlib2/
Source0:	https://files.pythonhosted.org/packages/source/c/contextlib2/contextlib2-%{version}.tar.gz
# Source0-md5:	d634281c2e61e575d8a68b9c56f8303a
URL:		https://contextlib2.readthedocs.io/
BuildRequires:	python-devel >= 1:2.7
%if %{with tests}
# requires unittest.TestCase.assertRaisesRegex(), available since 3.2
BuildRequires:	python-unittest2
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

%prep
%setup -q -n contextlib2-%{version}

%build
%py_build

%{?with_tests:%{__python} test_contextlib2.py}

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.txt NEWS.rst README.rst
%{py_sitescriptdir}/contextlib2.py[co]
%{py_sitescriptdir}/contextlib2-%{version}-py*.egg-info
