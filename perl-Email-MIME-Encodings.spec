#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Email
%define		pnam	MIME-Encodings
Summary:	Email::MIME::Encodings - a unified interface to MIME encoding and decoding
Summary(pl.UTF-8):	Email::MIME::Encodings - jednolity interfejs do kodowania i dekodowania MIME
Name:		perl-Email-MIME-Encodings
Version:	1.3
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	adb933af2ff9c3cc8e158bbdcf3d19e5
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-MIME-Base64 >= 3.05
BuildRequires:	perl(MIME::QuotedPrint) >= 3.03
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module simply wraps MIME::Base64 and MIME::QuotedPrint so that
you can throw the contents of a Content-Transfer-Encoding header at
some text and have the right thing happen.

%description -l pl.UTF-8
Ten moduł w prosty sposób obudowuje MIME::Base64 i MIME::QuotedPrint
tak, że można rzutować zawartość nagłówka Content-Transfer-Encoding na
jakiś tekst i wtedy stanie się to, co powinno.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%dir %{perl_vendorlib}/Email/MIME
%{perl_vendorlib}/Email/MIME/*.pm
%{_mandir}/man3/*
