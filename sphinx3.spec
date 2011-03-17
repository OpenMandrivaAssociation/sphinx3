Name: sphinx3
Version: 0.8
Release: %mkrel 1
Summary: CMU Sphinx Recognition System
Summary(ru_RU.UTF-8): Система распознавания речи
Group: Sound
License: BSD-style (see COPYING)
Url: http://cmusphinx.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-%{version}

Source: %{name}-%{version}.tar.gz

Requires: sphinxbase
BuildRequires: sphinxbase sphinxbase-devel

Source1: Makefile.patch
Source2: Makefile.inc.patch
Source3: Makefile.an4.patch
Source4: Makefile2.patch

%define Werror_cflags %nil
%define _disable_ld_no_undefined 1

%description
The CMU Sphinx Recognition System is a library and a set
of examples and utilities for speech recognition.
This package will install the sphinx3 library and some examples.

%package devel
Summary:        libraries and header files for Sphinx
Group:          Development/C
Requires:       %{name} = %{version}-%{release}

%description devel
The CMU Sphinx Recognition System is a library and a set
of examples and utilities for speech recognition.
This package contains libraries and header files need for development.

%prep
%setup
patch -p0 -F 90 Makefile.in %{SOURCE1}
patch -p0 -F 90 include/Makefile.in %{SOURCE2}
patch -p0 -F 90 model/lm/an4/Makefile.in %{SOURCE3}


%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
# ./autogen.sh
%configure
patch -p0 -F 90 Makefile %{SOURCE4}
patch -p0 -F 90 include/Makefile %{SOURCE4}
patch -p0 -F 90 model/lm/an4/Makefile %{SOURCE4}
%make

%install
make install DESTDIR=%{buildroot}

%clean
rm -fr %{buildroot}

%post
ldconfig

%postun
ldconfig

%files
%defattr(-,root,root)
%doc AUTHORS COPYING INSTALL README NEWS doc/*.ppt
%doc doc/*.html doc/*.pdf doc/*.txt doc/*.gif
%{_bindir}/*
%{_datadir}/%{name}
%{_libdir}/*.so.*
%{_libdir}/*.so

%files devel
%defattr(-,root,root)
%{_libdir}/*.a
%{_libdir}/*.la
%{_includedir}/%{name}/
%{_libdir}/pkgconfig/%{name}.pc
