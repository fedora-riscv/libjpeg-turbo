Name:		libjpeg-turbo
Version:	0.0.93
Release:	9%{?dist}
Summary:	A MMX/SSE2 accelerated library for manipulating JPEG image files

Group:		System Environment/Libraries
License:	wxWidgets
URL:		http://sourceforge.net/projects/libjpeg-turbo
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	autoconf, automake, libtool
%ifarch %{ix86} x86_64
BuildRequires:	nasm
%endif

Patch0:		libjpeg-turbo-programs.patch
Patch1:		libjpeg-turbo-nosimd.patch

%description
The libjpeg-turbo package contains a library of functions for manipulating
JPEG images

%package devel
Summary:	Headers for the libjpeg-turbo library
Group:		Development/Libraries
Obsoletes:	libjpeg-devel < 6b-47
Obsoletes:	libjpeg-static < 6b-47
Provides:	libjpeg-devel = 6b-47
Requires:	libjpeg-turbo%{?_isa} = %{version}-%{release}

%description devel
This package contains header files necessary for developing programs which
will manipulate JPEG files using the libjpeg-turbo library

%package utils
Summary:	Utilities for manipulating JPEG images
Group:		Applications/Multimedia
Obsoletes:	libjpeg < 6b-47

%description utils
The libjpeg-turbo-utils package contains simple client programs for
accessing the libjpeg functions. It contains cjpeg, djpeg, jpegtran,
rdjpgcom and wrjpgcom. Cjpeg compresses an image file into JPEG format.
Djpeg decompresses a JPEG file into a regular image file. Jpegtran
can perform various useful transformations on JPEG files. Rdjpgcom
displays any text comments included in a JPEG file. Wrjpgcom inserts
text comments into a JPEG file.

%prep
%setup -q

%patch0 -p1 -b .programs
%patch1 -p1 -b .nosimd

%build
autoreconf -fiv

%configure --disable-static

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

# Fix perms
chmod -x README-turbo.txt

# Remove unwanted files
rm -f $RPM_BUILD_ROOT/%{_libdir}/lib{,turbo}jpeg.la

# Don't distribute libjpegturbo because it is unversioned
rm -f $RPM_BUILD_ROOT/%{_includedir}/turbojpeg.h
rm -f $RPM_BUILD_ROOT/%{_libdir}/libturbojpeg.so

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc README README-turbo.txt change.log ChangeLog.txt LGPL.txt LICENSE.txt
%{_libdir}/libjpeg.so.62.0.0
%{_libdir}/libjpeg.so.62

%files devel
%defattr(-,root,root,-)
%doc coderules.doc jconfig.doc libjpeg.doc structure.doc example.c
%{_includedir}/jconfig.h
%{_includedir}/jerror.h
%{_includedir}/jmorecfg.h
%{_includedir}/jpeglib.h
%{_libdir}/libjpeg.so

%files utils
%defattr(-,root,root,-)
%doc usage.doc wizard.doc
%{_bindir}/cjpeg
%{_bindir}/djpeg
%{_bindir}/jpegtran
%{_bindir}/rdjpgcom
%{_bindir}/wrjpgcom
%{_mandir}/man1/cjpeg.1*
%{_mandir}/man1/djpeg.1*
%{_mandir}/man1/jpegtran.1*
%{_mandir}/man1/rdjpgcom.1*
%{_mandir}/man1/wrjpgcom.1*

%changelog
* Mon Jun 28 2010 Adam Tkac <atkac redhat com> 0.0.93-9
- merge review related fixes (#600243)

* Wed Jun 16 2010 Adam Tkac <atkac redhat com> 0.0.93-8
- merge review related fixes (#600243)

* Mon Jun 14 2010 Adam Tkac <atkac redhat com> 0.0.93-7
- obsolete -static libjpeg subpackage (#600243)

* Mon Jun 14 2010 Adam Tkac <atkac redhat com> 0.0.93-6
- improve package description a little (#600243)
- include example.c as %%doc in the -devel subpackage

* Fri Jun 11 2010 Adam Tkac <atkac redhat com> 0.0.93-5
- don't use "fc12" disttag in obsoletes/provides (#600243)

* Thu Jun 10 2010 Adam Tkac <atkac redhat com> 0.0.93-4
- fix compilation on platforms without MMX/SSE (#600243)

* Thu Jun 10 2010 Adam Tkac <atkac redhat com> 0.0.93-3
- package review related fixes (#600243)

* Wed Jun 09 2010 Adam Tkac <atkac redhat com> 0.0.93-2
- package review related fixes (#600243)

* Fri Jun 04 2010 Adam Tkac <atkac redhat com> 0.0.93-1
- initial package
