Summary:	AirTraf 802.11 - Wireless traffic sniffer
Summary(pl.UTF-8):   AirTraf 802.11 - program podsłuchujący sieci bezprzewodowe
Name:		airtraf
Version:	1.1
Release:	2
License:	GPL v2
Group:		Networking
Source0:	http://www.elixar.com/%{name}-%{version}.tar.gz
# Source0-md5:	2f999dc4cef573e14959261ad6c81294
Patch0:		%{name}-ncurses.patch
Patch1:		%{name}-types.patch
URL:		http://www.elixar.com/
BuildRequires:	ncurses-ext-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AirTraf is a wireless sniffer that can detect and determine exactly
what is being transmitted over 802.11 wireless networks.

%description -l pl.UTF-8
AirTraf to sniffer (węszyciel) sieci bezprzewodowych potrafiący wykryć
i ustalić co jest aktualnie przesyłane przez sieć bezprzewodową.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

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
