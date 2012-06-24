# TODO: optflags
Summary:	Tool for measuring available bandwidth between hosts
Summary(pl.UTF-8):	Narzędzie do pomiaru dostępnego pasma między hostami
Name:		nepim
Version:	0.46
Release:	0.1
License:	GPL
Group:		Applications/Networking
Source0:	http://download.savannah.gnu.org/releases/nepim/%{name}-%{version}.tar.gz
# Source0-md5:	23b9543423f750be1150de9b9a6b9a79
URL:		http://www.nongnu.org/nepim/
BuildRequires:	liboop-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Network Pipemeter is a tool for measuring available bandwidth between
hosts. It is also useful to generate network traffic for testing
purposes. It operates in client/server mode, is friendly towards
crossing NAT and stateful firewalls, is able to handle multiple
parallel traffic streams, reports periodic partial statistics along
the testing, accepts rich tunning from command-line options, and
supports IPv6.

%description -l pl.UTF-8
Network Pipemeter to narzędzie do pomiaru dostępnego pasma między
hostami. Jest przydatne także do generowania ruchu sieciowego w celach
testowych. Działa w trybie klient-serwer, jest przyjazny dla omijania
NAT-u i firewalli z obsługą stanów (stateful), potrafi obsługiwać
wiele równoległych strumieni ruchu, podaje na bieżąco częściowe
raporty statystyczne, daje się w znaczny sposób konfigurować z linii
poleceń i obsługuje IPv6.

%prep
%setup -q

%build
%{__make} -C src \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT

install -D src/nepim $RPM_BUILD_ROOT/%{_bindir}/nepim

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%attr(755,root,root) %{_bindir}/nepim
