Summary:	AirTraf 802.11 - Wireless traffic sniffer
Summary(pl):	AirTraf 802.11 - program pods³uchuj±cy sieci bezprzewodowe
Name:		airtraf
Version:	1.1
Release:	1
License:	GPL v2
Group:		Networking
Source0:	http://www.elixar.com/%{name}-%{version}.tar.gz
# Source0-md5:	2f999dc4cef573e14959261ad6c81294
Patch0:		%{name}-ncurses.patch
URL:		http://www.elixar.com/
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AirTraf is a wireless sniffer that can detect and determine exactly
what is being transmitted over 802.11 wireless networks.

%description -l pl
AirTraf to sniffer (wêszyciel) sieci bezprzewodowych potrafi±cy wykryæ
i ustaliæ co jest aktualnie przesy³ane przez sieæ bezprzewodow±.

%prep
%setup -q
%patch0	-p1

%build
%{__make} -C src \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

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
