%define modname Net-SSLeay
%define modver 1.92

Summary:	Perl extension for using OpenSSL
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	4
License:	BSD-like
Group:		Development/Perl
Url:		https://metacpan.org/pod/distribution/Net-SSLeay/lib/Net/SSLeay.pod
Source0:	https://cpan.metacpan.org/authors/id/C/CH/CHRISN/Net-SSLeay-%{modver}.tar.gz
Patch0:		Net-SSLeay-1.51-dont-add-extra-lib-paths.patch
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(MIME::Base64)
BuildRequires:	openssl
BuildRequires:	perl(Test)
BuildRequires:	perl-devel
BuildRequires:	perl-Test-Simple
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(zlib)

%description
Perl extension for using OpenSSL.

%prep
%autosetup -p1 -n %{modname}-%{modver}

%build
PERL_MM_USE_DEFAULT=1 perl Makefile.PL INSTALLDIRS=vendor
%make_build OPTIMIZE="%{optflags}"

#check
# testing the package implies contacting external sites (some are down ?)
#make test

%install
%make_install

%files
%doc Changes Credits README examples QuickRef
%{perl_vendorarch}/auto/Net
%{perl_vendorarch}/Net
%doc %{_mandir}/man3/*
