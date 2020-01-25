#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Data
%define		pnam	Validate-Domain
Summary:	Domain validation methods Perl module
Name:		perl-Data-Validate-Domain
Version:	0.10
Release:	1
License:	GPL+ or Artistic
Group:		Development/Libraries
Source0:	http://search.cpan.org/CPAN/authors/id/N/NE/NEELY/Data-Validate-Domain-%{version}.tar.gz
# Source0-md5:	1331c0f47c024a83c610f8598490423a
URL:		http://search.cpan.org/dist/Data-Validate-Domain
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with autodeps} || %{with tests}
BuildRequires:	perl(Exporter)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Net::Domain::TLD) >= 1.62
BuildRequires:	perl(Test::More)
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module collects domain validation routines to make input
validation, and untainting easier and more readable.

All functions return an untainted value if the test passes, and undef
if it fails. This means that you should always check for a defined
status explicitly. Don't assume the return will be true. (e.g.
is_username('0'))

The value to test is always the first (and often only) argument.

%prep
%setup -q -n Data-Validate-Domain-%{version}

find lib -name "*.pm" -exec chmod -c a-x {} +

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Data/Validate/Domain.pm
%{_mandir}/man3/Data::Validate::Domain.3pm*
