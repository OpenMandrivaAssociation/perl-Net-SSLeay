%define upstream_name      Net-SSLeay
%define upstream_version 1.42

Name:		    perl-%{upstream_name}
Version:	    %perl_convert_version %{upstream_version}
Release:	    2
Summary:	    Perl extension for using OpenSSL
License:	    BSD-like
Group:		    Development/Perl
Url:            http://search.cpan.org/dist/%{upstream_name}
Source0:        http://www.cpan.org/modules/by-module/Net/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:  openssl >= 0.9.3a
BuildRequires:	openssl-devel
BuildRequires:	perl-devel
BuildRequires:	zlib-devel
# temporary dep due to the perl-5.14 bump
BuildRequires:  perl-List-MoreUtils >= 0.320.0-4

%description
Perl extension for using OpenSSL.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
%__chmod 755 examples

%build
# note the %{_prefix} which must passed to Makefile.PL, weird but necessary :-(
echo | %{__perl} Makefile.PL %{_prefix} INSTALLDIRS=vendor
%make OPTIMIZE="$RPM_OPT_FLAGS"
perl -p -i -e 's|/usr/local/bin|/usr/bin|g;' *.pm examples/*

%check
# testing the package implies contacting external sites (some are down ?)
#make test

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%doc Changes Credits README examples QuickRef
%{perl_vendorarch}/auto/Net
%{perl_vendorarch}/Net
%{_mandir}/*/*

