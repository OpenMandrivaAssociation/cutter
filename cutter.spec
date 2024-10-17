Summary:	Aborts TCP/IP connections
Name:		cutter
Version:	1.03
Release:	9
License:	GPLv2+
Group:		Networking/Other
URL:		https://www.lowth.com/cutter
Source0:	%{name}-%{version}.tar.bz2
Patch1:		%{name}-1.02-fixnonnatted.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
Cutter is an open source program that allows Linux firewall administrators to
abort TCP/IP connections routed over the firewall or router on which it is run.

%prep

%setup -q
%patch1 -p1 -b .fixnonnatted

%build

%{__cc} %{optflags} -o cutter cutter.c

%install
%{__rm} -rf %{buildroot}

%{__install} -d %{buildroot}%{_sbindir}
%{__install} -m755 %{name} %{buildroot}%{_sbindir}/%{name}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%attr(0755,root,root) %{_sbindir}/%{name}



%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 1.03-8mdv2011.0
+ Revision: 610180
- rebuild

  + Sandro Cazzaniga <kharec@mandriva.org>
    - Fix licence
    - New Maintainers

* Mon Dec 07 2009 Jérôme Brenier <incubusss@mandriva.org> 1.03-6mdv2010.1
+ Revision: 474572
- fix license tag

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Tue Jul 22 2008 Thierry Vignaud <tv@mandriva.org> 1.03-4mdv2009.0
+ Revision: 240516
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri Apr 27 2007 Oden Eriksson <oeriksson@mandriva.com> 1.03-2mdv2008.0
+ Revision: 18569
- rebuild


* Thu Mar 23 2006 Lenny Cartier <lenny@mandriva.com> 1.03-1mdk
- 1.03

* Sun Dec 25 2005 Oden Eriksson <oeriksson@mandriva.com> 1.02-4mdk
- rebuild

* Fri Oct 15 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 1.02-3mdk
- rpmbuildupdated

* Sat Aug 23 2003 Ben Reser <ben@reser.org> 1.02-2mdk
- Fix to work with connections that are not NAT'ed
- Fix group it's not a Monitoring tool.
- Macroize

* Fri Jun 27 2003 Oden Eriksson <oden.eriksson@kvikkjokk.net> 1.02-1mdk
- initial cooker contrib

