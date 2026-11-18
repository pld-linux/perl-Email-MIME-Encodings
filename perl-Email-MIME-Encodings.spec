#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Email
%define		pnam	MIME-Encodings
Summary:	Email::MIME::Encodings - a unified interface to MIME encoding and decoding
Summary(pl.UTF-8):	Email::MIME::Encodings - jednolity interfejs do kodowania i dekodowania MIME
Name:		perl-Email-MIME-Encodings
Version:	1.317
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-module/Email/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	dd6744509775b75f4df0330cb5174539
URL:		http://search.cpan.org/dist/Email-MIME-Encodings/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-MIME-Base64 >= 3.05
BuildRequires:	perl(MIME::QuotedPrint) >= 3.05
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
