%define	modname	Net-SSLeay
%define	modver	1.51

Summary:	Perl extension for using OpenSSL
Name:		perl-%{modname}
Version:	%{perl_convert_version %{modver}}
Release:	5
License:	BSD-like
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Net/%{modname}-%{modver}.tar.gz
Patch0:		Net-SSLeay-1.51-dont-add-extra-lib-paths.patch
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(MIME::Base64)
BuildRequires:	perl(Test::More)
BuildRequires:	openssl
BuildRequires:	perl-devel
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(zlib)

%description
Perl extension for using OpenSSL.

%prep
%setup -qn %{modname}-%{modver}
%apply_patches

%build
PERL_MM_USE_DEFAULT=1 perl Makefile.PL INSTALLDIRS=vendor
%make OPTIMIZE="%{optflags}"

%check
# testing the package implies contacting external sites (some are down ?)
#make test

%install
%makeinstall_std

%files
%doc Changes Credits README examples QuickRef
%{perl_vendorarch}/auto/Net
%{perl_vendorarch}/Net
%{_mandir}/man3/*

