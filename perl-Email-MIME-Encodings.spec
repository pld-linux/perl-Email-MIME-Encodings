#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Email
%define	pnam	MIME-Encodings
Summary:	Email::MIME::Encodings - a unified interface to MIME encoding and decoding
Summary(pl):	Email::MIME::Encodings - jednolity interfejs do kodowania i dekodowania MIME
Name:		perl-Email-MIME-Encodings
Version:	1.1
Release:	1
# same as perl
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9dc94a2052e8c02a2b2b0926731ffa72
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{!?_without_tests:1}0
BuildRequires:	perl(MIME::Base64)
BuildRequires:	perl(MIME::QuotedPrint)
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module simply wraps MIME::Base64 and MIME::QuotedPrint so that
you can throw the contents of a Content-Transfer-Encoding header at
some text and have the right thing happen.

%description -l pl
Ten modu³ w prosty sposób obudowuje MIME::Base64 i MIME::QuotedPrint
tak, ¿e mo¿na rzutowaæ zawarto¶æ nag³ówka Content-Transfer-Encoding na
jaki¶ tekst i wtedy stanie siê to, co powinno.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{!?_without_tests:%{__make} test}

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
