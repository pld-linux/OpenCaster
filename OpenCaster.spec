Summary:	MPEG transport stream generation and management tools
Name:		OpenCaster
Version:	3.1.4
Release:	1
License:	GPL v2+
Group:		Networking
Source0:	http://www.avalpa.com/assets/freesoft/opencaster/%{name}%{version}.tgz
# Source0-md5:	e5e0f93cbec504936c796468d392b323
URL:		http://avalpa.com/the-key-values/15-free-software/33-opencaster
BuildRequires:	libdvbcsa-devel
#BuildRequires:	libgomp-devel
BuildRequires:	python-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Free DVB TS server software useful for many purposes: carousel server,
PSI table generator, datacasting, MPEG2 "poor man" playout system.
Avalpa OpenCaster is a collection of tools that is able to generate an
MPEG-2 data structure (stored within a Transport Stream file).
Therefore it can can also manipulate the inside packets (video, audio,
teletext packets but also Service Information/Program Specific
Information ones).

%prep
%setup -q -n %{name}%{version}

%build
%{__make} \
	CFLAGS="%{rpmcflags}"

%{__make} -C tools/tscrypt \
	CFLAGS="%{rpmcflags}"

# ip2sec, oddparity

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} -C tools install \
	DESTDIR=$RPM_BUILD_ROOT%{_bindir}

%{__make} -C tools/tscrypt install \
	DESTDIR=$RPM_BUILD_ROOT%{_bindir}

cd libs/dvbobjects
%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%attr(755,root,root) %{_bindir}/*
%{python_sitearch}/dvbobjects*
