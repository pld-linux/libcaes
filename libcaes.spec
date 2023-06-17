# m4/libcerror.m4
%define		libcerror_ver	20120425
Summary:	Library to support cross-platform AES encryption
Summary(pl.UTF-8):	Biblioteka obsługująca wieloplatformowe szyfrowanie AES
Name:		libcaes
Version:	20230406
Release:	1
License:	LGPL v3+
Group:		Libraries
#Source0Download: https://github.com/libyal/libcaes/releases
Source0:	https://github.com/libyal/libcaes/releases/download/%{version}/%{name}-alpha-%{version}.tar.gz
# Source0-md5:	ac2c771c1afb65795288ec77fdbed465
URL:		https://github.com/libyal/libcaes/
BuildRequires:	autoconf >= 2.71
BuildRequires:	automake >= 1.6
BuildRequires:	gettext-tools >= 0.18.1
BuildRequires:	libcerror-devel >= %{libcerror_ver}
BuildRequires:	libtool >= 2:2
BuildRequires:	openssl-devel >= 1.0
BuildRequires:	pkgconfig
Requires:	libcerror >= %{libcerror_ver}
Requires:	openssl >= 1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libcaes is a library to support cross-platform AES encryption.

%description -l pl.UTF-8
libcaes to biblioteka obsługująca wieloplatformowe szyfrowanie AES.

%package devel
Summary:	Header files for libcaes library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libcaes
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libcerror-devel >= %{libcerror_ver}
Requires:	openssl-devel >= 1.0

%description devel
Header files for libcaes library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libcaes.

%package static
Summary:	Static libcaes library
Summary(pl.UTF-8):	Statyczna biblioteka libcaes
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libcaes library.

%description static -l pl.UTF-8
Statyczna biblioteka libcaes.

%prep
%setup -q

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libcaes.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/libcaes.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcaes.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcaes.so
%{_includedir}/libcaes
%{_includedir}/libcaes.h
%{_pkgconfigdir}/libcaes.pc
%{_mandir}/man3/libcaes.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libcaes.a
