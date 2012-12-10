%define	name	linuxsms
%define version	0.77
%define release	 %mkrel 7


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



%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.77-7mdv2011.0
+ Revision: 620243
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.77-6mdv2010.0
+ Revision: 429856
- rebuild

* Mon Jul 28 2008 Thierry Vignaud <tv@mandriva.org> 0.77-5mdv2009.0
+ Revision: 251117
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Dec 19 2007 Thierry Vignaud <tv@mandriva.org> 0.77-3mdv2008.1
+ Revision: 133065
- auto-convert XDG menu entry
- kill re-definition of %%buildroot on Pixel's request
- use %%mkrel
- fix hardcoded man page extension
- import linuxsms


* Fri Jul 08 2005 Lenny Cartier <lenny@mandriva.com> 0.77-3mdk
- rebuild

* Wed May 12 2004 Daouda LO <daouda@mandrakesoft.com> 0.77-2mdk
- fix the '-pady' option for tk frontend (pointed by Adam)

* Tue May 04 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.77-1mdk
- 0.77

* Fri Feb 20 2004 David Baudens <baudens@mandrakesoft.com> 0.76-2mdk
- Fix menu
- Allow to be launched

* Thu Dec 04 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.76-1mdk
- 0.76

* Sun Nov 23 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.74-1mdk
- 0.74

* Fri Nov 15 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.73-1mdk
- patch merged upstream (for e-zones portal)
- update xlinuxsms interface

* Mon Nov 03 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.71-1mdk
- 0.71

* Mon Sep 22 2003 Tibor Pittich <Tibor.Pittich@phuture.sk> 0.68-2mdk
- fixed title and section definitions
- fixed version in changelog, grrrr

* Mon Sep 22 2003 Tibor Pittich <Tibor.Pittich@phuture.sk> 0.68-1mdk
- new version
- drop prefix
- repackaged icons
- macroszification and other cosmetic changes in spec file
- added patch to allow send sms via e-zones portal (Eurotel Slovakia)
  thanks to Juraj Bednar

* Wed Aug 27 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.67-1mdk
- 0.67

* Fri Jun 27 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.65-1mdk
- 0.65

* Mon May 19 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.63-1mdk
- 0.63

* Thu Apr 10 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.62-1mdk
- 0.62
- regenerate patch

* Mon Feb 24 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.60-1mdk
- 0.60

* Sun Jan 05 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.59-1mdk
- 0.59

* Mon Oct 28 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.57-1mdk
- 0.57

* Mon Oct 07 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.56-1mdk
- 0.56

* Fri Sep 20 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.55-1mdk
- 0.55

* Mon Jul 15 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.49-1mdk
- 0.49

* Mon Jul 08 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.48-1mdk
- 0.48

* Mon Jun 24 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.46-1mdk
- 0.46

* Mon Jun 10 2002 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.45-1mdk
- new release

* Mon May 27 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.44-1mdk
- from Juan Manuel Garcia Molina <juanma_gm@wanadoo.es> :
	- Add patch to change the Makefile (avoid static bindir/mandir).
	- Add TCL GUI for linuxsms (aka xlinuxsms.pl).
	- Modify Makefile to include xlinuxsms.pl.
- 0.44

