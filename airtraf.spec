Summary:	AirTraf 802.11 Wireless traffic sniffer
Name:		airtraf
Version:	1.1
Release:	0.1
License:	GPL
Group:		Networking
Source0:	http://www.elixar.com/%{name}-%{version}.tar.gz
# Source0-md5:	2f999dc4cef573e14959261ad6c81294
Patch0:		%{name}-ncurses.patch
URL:		http://www.elixar.com/
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AirTraf 1.0 is a wireless sniffer that can detect and determine
exactly what is being transmitted over 802.11 wireless networks.

%prep
%setup -q -n %{name}-%{version}
%patch0	-p1

%build
cd src
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}

install src/airtraf $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Authors INSTALL docs

%attr(755,root,root) %{_bindir}/*
