#libclastfm-0.4_p20120315.tar.xz


%define git_date 20120315
%define major 1
%define libname %mklibname clastfm %{major}
%define develname %mklibname -d clastfm
%define develnamest %mklibname -d clastfm -s


Name:           libclastfm
Version:        0.4
Release:        1
Summary:        Unofficial C-API for the Last.fm web service

Group:          System/Libraries
License:        GPLv3+
URL:            https://liblastfm.sourceforge.net/
Source0:        %{name}-%{version}_p20120315.tar.xz
BuildRequires:  libtool
BuildRequires:  libcurl-devel

%description
libclastfm is an unofficial C-API for the Last.fm web service written with
libcurl. It was written because the official CBS Interactive Last.fm library
requires Nokia QT, which is usually not desired when using GTK+ based distros.

This library supports much more than basic scrobble submission. You can send
shouts, fetch Album covers and much more.

Due to the naming conflict with the official last.fm library, this library will
install as "libclastfm".

%package -n	%libname
Summary:        Unofficial C-API for the Last.fm web service
Group:          System/Libraries

%description -n  %libname
libclastfm is an unofficial C-API for the Last.fm web service written with
libcurl. It was written because the official CBS Interactive Last.fm library
requires Nokia QT, which is usually not desired when using GTK+ based distros.

This library supports much more than basic scrobble submission. You can send
shouts, fetch Album covers and much more.

Due to the naming conflict with the official last.fm library, this library will
install as "libclastfm".


%package -n	%develname
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	clastfm-devel = %{version}-%{release}

%description -n	%develname
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package -n	%develnamest
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel-static = %{version}-%{release}
Provides:	clastfm-devel-static = %{version}-%{release}

%description -n  %develnamest
The %{name}-devel package contains static libraries and header files for
developing applications that use %{name}.


%prep
%setup -qn %{name}-%{version}_p%git_date


%build
NOCONFIGURE=1 sh autogen.sh
%configure2_5x
%make


%install
%makeinstall_std
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%files -n %libname
%doc AUTHORS ChangeLog COPYING NEWS README
%{_libdir}/%{name}.so.*

%files -n %develname
%{_includedir}/*
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%files -n %develnamest
%{_libdir}/*.a
