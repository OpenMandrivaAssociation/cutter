Summary:	Aborts TCP/IP connections
Name:		cutter
Version:	1.03
Release:	%mkrel 8
License:	GPLv2+
Group:		Networking/Other
URL:		http://www.lowth.com/cutter
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

