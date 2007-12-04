%define	name	linuxsms
%define version	0.77
%define release	 %mkrel 3


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
mkdir -p %buildroot/%_menudir
cat > %buildroot/%_menudir/%name << EOF
?package(%name): \
command="%_bindir/xlinuxsms.pl" \
needs="X11" \
icon="%name.png" \
section="Office/Communications/Phone" \
title="LinuxSMS" \
longtitle="%summary"
EOF

%post
%update_menus

%postun
%update_menus

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(0755,root,bin)
%{_bindir}/linuxsms
%{_bindir}/xlinuxsms.pl
%defattr(-,root,root,0755)
%doc BUGS CHANGES COPYING README README.ES TODO
%{_mandir}/man1/linuxsms.1*
%{_menudir}/*
%{_miconsdir}/*
%{_iconsdir}/*.png
%{_liconsdir}/*

