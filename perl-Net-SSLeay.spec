%define	modname	Net-SSLeay
%define	modver	1.51

Name:		perl-%{modname}
Version:	%{perl_convert_version %{modver}}
Release:	4
Summary:	Perl extension for using OpenSSL
License:	BSD-like
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Net/%{modname}-%{modver}.tar.gz
Patch0:		Net-SSLeay-1.51-dont-add-extra-lib-paths.patch
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(MIME::Base64)
BuildRequires:	perl(Test::More)
BuildRequires:	openssl
BuildRequires:	pkgconfig(openssl)
BuildRequires:	perl-devel
BuildRequires:	pkgconfig(zlib)

%description
Perl extension for using OpenSSL.

%prep
%setup -q -n %{modname}-%{modver}
%patch0 -p1 -b .libpaths~

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
%{_mandir}/*/*

%changelog
* Fri Dec 28 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.510.0-1
- get rid of '-L/usr -L/usr/lib' getting passed to linker (P0)
- clean dependencies
- rebuild for new perl-5.16.2
- cleanups
- new version

* Fri Jan 27 2012 Oden Eriksson <oeriksson@mandriva.com> 1.420.0-5
+ Revision: 769283
- fix #65191 (perl-Net-SSLeay stop providing perl-Net_SSLeay and perl-Net_SSLeay.pm)

* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.420.0-4
+ Revision: 765536
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.420.0-3
+ Revision: 764060
- rebuilt for perl-5.14.x
- cleanup temporary deps, this was added in perl-devel instead

* Fri Jan 20 2012 Oden Eriksson <oeriksson@mandriva.com> 1.420.0-2
+ Revision: 763251
- force it

* Wed Nov 30 2011 Matthew Dawkins <mattydaw@mandriva.org> 1.420.0-1
+ Revision: 735518
- new version 1.42
- cleaned up spec
- removed defattr, mkrel, BuildRoot, clean section
- removed old obsoletes & provides
- removed bunk req for openssl

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.360.0-8
+ Revision: 667279
- mass rebuild

* Wed Dec 01 2010 Funda Wang <fwang@mandriva.org> 1.360.0-7mdv2011.0
+ Revision: 604334
- rebuild for new zlib

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 1.360.0-6mdv2011.0
+ Revision: 564569
- rebuild for perl 5.12.1

* Tue Jul 20 2010 Sandro Cazzaniga <kharec@mandriva.org> 1.360.0-5mdv2011.0
+ Revision: 555279
- rebuild
- rebuild

* Wed Apr 07 2010 Funda Wang <fwang@mandriva.org> 1.360.0-3mdv2010.1
+ Revision: 532508
- rebuild

* Fri Feb 26 2010 Oden Eriksson <oeriksson@mandriva.com> 1.360.0-2mdv2010.1
+ Revision: 511616
- rebuilt against openssl-0.9.8m

* Mon Feb 01 2010 Jérôme Quelin <jquelin@mandriva.org> 1.360.0-1mdv2010.1
+ Revision: 498982
- update to 1.36

* Sun Jul 12 2009 Jérôme Quelin <jquelin@mandriva.org> 1.350.0-2mdv2010.0
+ Revision: 395255
- rebuild to extract correct version

* Thu Jul 09 2009 Jérôme Quelin <jquelin@mandriva.org> 1.350.0-1mdv2010.0
+ Revision: 393743
- adding missing buildrequires
- adding missing buildrequires
- adding missing buildrequires:
- setting OPENSSL_PREFIX
- fixed wrong comparison in obsoletes
- renamed perl-Net_SSLeay.pm to perl-Net-SSLeay
- renamed spec file to match package
- renamed package to perl-Net-SSLeay (instead of perl-Net_SSLeay.pm
  formerly known as perl-Net_SSLeay)
- update to 1.35
- using %%perl_convert_version
- removed patch perl-Net_SSLeay-1.2.5-CVE-2005-0106.patch which has been
  merged upstream
- removed patch perl-Net_SSLeay-1.30-large-tcp-read.patch which seems to
  be merged (although a bit differently) upstream

  + Antoine Ginies <aginies@mandriva.com>
    - rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.30-7mdv2009.0
+ Revision: 223906
- rebuild

* Mon Jan 14 2008 Pixel <pixel@mandriva.com> 1.30-6mdv2008.1
+ Revision: 151338
- rebuild for perl-5.10.0

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Sep 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.30-5mdv2008.0
+ Revision: 90055
- rebuild

* Mon Aug 20 2007 Thierry Vignaud <tv@mandriva.org> 1.30-4mdv2008.0
+ Revision: 67514
- rebuild

