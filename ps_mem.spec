%bcond_without	tests # tests

Summary:	Memory profiling tool
Name:		ps_mem
Version:	3.12
Release:	1
License:	LGPL v2+
Group:		Base
URL:		https://github.com/pixelb/ps_mem
Source0:	https://github.com/pixelb/ps_mem/archive/v%{version}.tar.gz
# Source0-md5:	44888ba627eccc338feff401c1785feb
BuildRequires:	python3-modules
BuildRequires:	python3-setuptools
BuildArch:	noarch

%description
The ps_mem tool reports how much core memory is used per program (not
per process). In detail it reports: sum(private RAM for program
processes) + sum(Shared RAM for program processes) The shared RAM is
problematic to calculate, and the tool automatically selects the most
accurate method available for the running kernel.

%prep
%setup -q

%build
%py3_build %{?with_tests:test}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

sed -e 's|^#!.*|#!%{__python3}|' build-3/lib/ps_mem.py > $RPM_BUILD_ROOT%{_bindir}/ps_mem
chmod 755 $RPM_BUILD_ROOT%{_bindir}/ps_mem

cp -p %{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
