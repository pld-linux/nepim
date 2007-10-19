Summary:	tool for measuring available bandwidth between hosts
Name:		nepim
Version:	0.43
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://download.savannah.gnu.org/releases/nepim/%{name}-%{version}.tar.gz
# Source0-md5:	2fd3214c47c046f552c34d66c3f87c05
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

%prep
%setup -q

%build
cd src
%{__make} \
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
