#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Net-OpenSSH
Version  : 0.78
Release  : 1
URL      : https://cpan.metacpan.org/authors/id/S/SA/SALVA/Net-OpenSSH-0.78.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/S/SA/SALVA/Net-OpenSSH-0.78.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libn/libnet-openssh-perl/libnet-openssh-perl_0.78-1.debian.tar.xz
Summary  : 'Perl SSH client package implemented on top of OpenSSH'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Net-OpenSSH-man

%description
Net-OpenSSH
===========
Perl wrapper for OpenSSH secure shell client.
INSTALLATION

%package man
Summary: man components for the perl-Net-OpenSSH package.
Group: Default

%description man
man components for the perl-Net-OpenSSH package.


%prep
tar -xf %{SOURCE1}
cd ..
%setup -q -n Net-OpenSSH-0.78
mkdir -p %{_topdir}/BUILD/Net-OpenSSH-0.78/deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Net-OpenSSH-0.78/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.26.1/Net/OpenSSH.pm
/usr/lib/perl5/site_perl/5.26.1/Net/OpenSSH/ConnectionCache.pm
/usr/lib/perl5/site_perl/5.26.1/Net/OpenSSH/Constants.pm
/usr/lib/perl5/site_perl/5.26.1/Net/OpenSSH/ModuleLoader.pm
/usr/lib/perl5/site_perl/5.26.1/Net/OpenSSH/OSTracer.pm
/usr/lib/perl5/site_perl/5.26.1/Net/OpenSSH/ObjectRemote.pm
/usr/lib/perl5/site_perl/5.26.1/Net/OpenSSH/SSH.pm
/usr/lib/perl5/site_perl/5.26.1/Net/OpenSSH/ShellQuoter.pm
/usr/lib/perl5/site_perl/5.26.1/Net/OpenSSH/ShellQuoter/Chain.pm
/usr/lib/perl5/site_perl/5.26.1/Net/OpenSSH/ShellQuoter/MSCmd.pm
/usr/lib/perl5/site_perl/5.26.1/Net/OpenSSH/ShellQuoter/MSWin.pm
/usr/lib/perl5/site_perl/5.26.1/Net/OpenSSH/ShellQuoter/POSIX.pm
/usr/lib/perl5/site_perl/5.26.1/Net/OpenSSH/ShellQuoter/csh.pm
/usr/lib/perl5/site_perl/5.26.1/Net/OpenSSH/ShellQuoter/fish.pm

%files man
%defattr(-,root,root,-)
/usr/share/man/man3/Net::OpenSSH.3
/usr/share/man/man3/Net::OpenSSH::ConnectionCache.3
/usr/share/man/man3/Net::OpenSSH::Constants.3
/usr/share/man/man3/Net::OpenSSH::OSTracer.3
/usr/share/man/man3/Net::OpenSSH::SSH.3
/usr/share/man/man3/Net::OpenSSH::ShellQuoter::MSCmd.3
/usr/share/man/man3/Net::OpenSSH::ShellQuoter::MSWin.3
