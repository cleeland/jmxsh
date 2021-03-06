Summary: jmxsh command-line JMX client
Name: jmxsh
Version: 1.0
Release: 1
Group: Utilities
License: Apache 2.0, Sun, various-listed in jar file
URL: https://github.com/cleeland/jmxsh
Source: %{name}-%{version}-%{release}.tar.gz
Packager: Chris Cleeland
BuildArchitectures: noarch
#BuildRequires: jdk ant
Requires: jre

%define _source_payload w9.gzdio
%define _binary_payload w9.gzdio
%define _source_filedigest_algorithm 1
%define _binary_filedigest_algorithm 1

%description
jmxsh is a command-line JMX client that offers a menu-based browse and
a shell prompt that uses TCL.  It is scriptable.

%prep
%setup -c %{name}-%{version}


%install
pwd
for d in %{_prefix}/lib %{_bindir}; do \
  test -d %{buildroot}$d || mkdir -p %{buildroot}$d; \
done
cp jmxsh.jar %{buildroot}%{_prefix}/lib
cp jmxsh     %{buildroot}%{_bindir}
chmod -R +x  %{buildroot}%{_bindir}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%{_bindir}/*
%{_prefix}/lib*
