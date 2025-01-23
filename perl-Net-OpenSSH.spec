#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v21
# autospec commit: 94c6be0
#
Name     : perl-Net-OpenSSH
Version  : 0.84
Release  : 31
URL      : https://cpan.metacpan.org/authors/id/S/SA/SALVA/Net-OpenSSH-0.84.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/S/SA/SALVA/Net-OpenSSH-0.84.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libn/libnet-openssh-perl/libnet-openssh-perl_0.78-1.debian.tar.xz
Summary  : 'Perl SSH client package implemented on top of OpenSSH'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Net-OpenSSH-license = %{version}-%{release}
Requires: perl-Net-OpenSSH-perl = %{version}-%{release}
Requires: perl(Object::Remote::Role::Connector::PerlInterpreter)
BuildRequires : buildreq-cpan
BuildRequires : perl(Digest::MD5)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Net-OpenSSH
===========
Perl wrapper for OpenSSH secure shell client.
INSTALLATION

%package dev
Summary: dev components for the perl-Net-OpenSSH package.
Group: Development
Provides: perl-Net-OpenSSH-devel = %{version}-%{release}
Requires: perl-Net-OpenSSH = %{version}-%{release}

%description dev
dev components for the perl-Net-OpenSSH package.


%package license
Summary: license components for the perl-Net-OpenSSH package.
Group: Default

%description license
license components for the perl-Net-OpenSSH package.


%package perl
Summary: perl components for the perl-Net-OpenSSH package.
Group: Default
Requires: perl-Net-OpenSSH = %{version}-%{release}

%description perl
perl components for the perl-Net-OpenSSH package.


%prep
%setup -q -n Net-OpenSSH-0.84
cd %{_builddir}
tar xf %{_sourcedir}/libnet-openssh-perl_0.78-1.debian.tar.xz
cd %{_builddir}/Net-OpenSSH-0.84
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Net-OpenSSH-0.84/deblicense/
pushd ..
cp -a Net-OpenSSH-0.84 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Net-OpenSSH
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Net-OpenSSH/358e44dddf4d5eb61f97778a8f1bd7845ee8d25f || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Net::OpenSSH.3
/usr/share/man/man3/Net::OpenSSH::ConnectionCache.3
/usr/share/man/man3/Net::OpenSSH::Constants.3
/usr/share/man/man3/Net::OpenSSH::OSTracer.3
/usr/share/man/man3/Net::OpenSSH::SSH.3
/usr/share/man/man3/Net::OpenSSH::ShellQuoter::MSCmd.3
/usr/share/man/man3/Net::OpenSSH::ShellQuoter::MSWin.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Net-OpenSSH/358e44dddf4d5eb61f97778a8f1bd7845ee8d25f

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
