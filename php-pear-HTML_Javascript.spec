%define	_class		HTML
%define	_subclass	Javascript
%define	modname	%{_class}_%{_subclass}

Summary:	An interface for creating simple JS scripts
Name:		php-pear-%{modname}
Version:	1.1.2
Release:	17
License:	PHP License
Group:		Development/PHP
Url:		http://pear.php.net/package/HTML_Javascript/
Source0:	http://download.pear.php.net/package/%{modname}-%{version}.tgz
BuildArch:	noarch
BuildRequires:	php-pear
Requires(post,preun):	php-pear
Requires:	php-pear

%description
Provides two classes:
- HTML_Javascript for performing basic JS operations
- HTML_Javascript_Convert for converting variables
Allow output data to a file, to the standart output (print), or
return.

%prep
%setup -qc
mv package.xml %{modname}-%{version}/%{modname}.xml

%install
cd %{modname}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{modname}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{modname}.xml %{buildroot}%{_datadir}/pear/packages

%files
%doc %{modname}-%{version}/examples
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{modname}.xml

