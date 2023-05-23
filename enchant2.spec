%global api 2
%global major 2
%define libname %mklibname enchant %api %major
%define devname %mklibname -d enchant %api

Name:          enchant2
Version:       2.4.0
Release:       1
Summary:       An Enchanting Spell Checking Library
Group:         System/Libraries

License:       LGPLv2+
URL:           https://github.com/AbiWord/enchant
Source0:       https://github.com/AbiWord/enchant/releases/download/v%{version}/enchant-%{version}.tar.gz

BuildRequires: pkgconfig(glib-2.0)
BuildRequires: aspell-devel
BuildRequires: hunspell-devel
BuildRequires: hspell-devel
BuildRequires: pkgconfig(libvoikko)
Provides:      bundled(gnulib)
Conflicts:     %{_lib}enchant2 < 2.2.3-2

%description
A library that wraps other spell checking backends.

%package aspell
Summary:       Integration with aspell for libenchant

%description aspell
Libraries necessary to integrate applications using libenchant with aspell.

%package voikko
Summary:       Integration with voikko for libenchant

%description voikko
Libraries necessary to integrate applications using libenchant with voikko.

%package hspell
Summary:       Integration with hspell for libenchant

%description hspell
Libraries necessary to integrate applications using libenchant with hspell.

%package -n %libname
Summary: An Enchanting Spell Checking Library
Group: System/Libraries
Obsoletes: %{_lib}enchant2 < 2.2.3-2

%description -n %libname
A library that wraps other spell checking backends.

%package -n %devname
Group: Development/C
Summary: Development files for %{name}
Provides: enchant2-devel
Requires: %libname%{?_isa} = %{version}-%{release}

%description -n %devname
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1 -n enchant-%{version}

%build
%configure \
    --with-aspell \
    --with-hunspell-dir=%{_datadir}/dict/ooo \
    --disable-static
%make_build pkgdatadir=%{_datadir}/enchant-2

%install
%make_install pkgdatadir=%{_datadir}/enchant-2
find %{buildroot} -name '*.la' -delete

%files
%doc AUTHORS NEWS README
%license COPYING.LIB
%{_bindir}/enchant-2
%{_bindir}/enchant-lsmod-2
%{_mandir}/man1/*
%{_datadir}/enchant-2/

%files -n %libname
%license COPYING.LIB
%{_libdir}/libenchant-%{api}.so.%{major}{,.*}
%dir %{_libdir}/enchant-2/
%{_libdir}/enchant-2/enchant_hunspell.so

%files aspell
%{_libdir}/enchant-2/enchant_aspell.so

%files voikko
%{_libdir}/enchant-2/enchant_voikko.so

%files hspell
%{_libdir}/enchant-2/enchant_hspell.so


%files -n %devname
%{_libdir}/libenchant-2.so
%{_libdir}/pkgconfig/enchant-2.pc
%{_includedir}/enchant-2/
