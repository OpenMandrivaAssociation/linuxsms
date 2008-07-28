%define	name	linuxsms
%define version	0.77
%define release	 %mkrel 5


%define summary	Cool script to send SMS

Summary:	%summary
Name:		%name
Version:	%version
Release:	%release
Source0:	%name-%version.tar.bz2
Source1:	%name-icons.tar.bz2
Source2:	xlinuxsms.pl.bz2
Patch0:		%name-makefile.patch.bz2
Patch1:		linuxsms-0.77-pady.patch.bz2
License:	GPL
Group:		Communications
URL:		http://linuxsms.sourceforge.net
BuildRoot:	%_tmppath/%name-buildroot
Buildarch:	noarch

%description
Linuxsms is a cool script in Perl for send short messages to gsm phones
(aka: sms 8-)) written by z0mbie.
Also includes a small Perl script with a GUI for linuxsms.

%prep
%setup -q
%setup -q -T -D -a1
%patch0 -p1 -b .linuxsms-makefile.patch
bzcat %{SOURCE2} > xlinuxsms.pl
%patch1 -p1

%build

%install
%makeinstall

# install icons
%__install -D -m 644 %{name}48.png %buildroot/%_liconsdir/%name.png
%__install -D -m 644 %{name}32.png %buildroot/%_iconsdir/%name.png
%__install -D -m 644 %{name}16.png %buildroot/%_miconsdir/%name.png

# menu
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%name.desktop
[Desktop Entry]
Type=Application
Exec=%_bindir/xlinuxsms.pl
Icon=%name
Categories=Network;
Name=LinuxSMS
Comment=%summary
EOF

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%update_menus
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(0755,root,bin)
%{_bindir}/linuxsms
%{_bindir}/xlinuxsms.pl
%defattr(-,root,root,0755)
%doc BUGS CHANGES COPYING README README.ES TODO
%{_mandir}/man1/linuxsms.1*
%{_datadir}/applications/mandriva-*.desktop
%{_miconsdir}/*
%{_iconsdir}/*.png
%{_liconsdir}/*

