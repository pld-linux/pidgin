# This file does not like to be adapterized!
#
%bcond_with	doc	# generate and include documentation
#
%include        /usr/lib/rpm/macros.perl
Summary:	A client compatible with AOL's 'Instant Messenger'
Summary(ko):	AOL 인스턴트 메신저와 호환되는 클라이언트
Summary(pl):	Klient kompatybilny z AOL Instant Messenger
Summary(pt_BR):	Um cliente para o AOL Instant Messenger (AIM)
Name:		gaim
Version:	0.76
Release:	0.6
Epoch:		1
License:	GPL
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	832126135930b4a13537d1270088c2dc
Patch0:		%{name}-nolibs.patch
Patch1:		%{name}-missing-file.patch
URL:		http://gaim.sourceforge.net/
BuildRequires:	audiofile-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2.2.0
BuildRequires:	libao-devel
BuildRequires:	libtool
BuildRequires:	perl-devel
BuildRequires:	pkgconfig
%if %{with doc}
BuildRequires:	doxygen
BuildRequires:	graphviz
%endif
Requires:	gaim-ui = %{epoch}:%{version}
Requires:	libao
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gaim allows you to talk to anyone using AOL's Instant Messenger
service (you can sign up at http://www.aim.aol.com). It uses the TOC
version of the AOL protocol, so your buddy list is stored on AOL's
servers and can be retrieved from anywhere. It contains many of the
same features as AOL's IM client while at the same time incorporating
many new features. Gaim also contains a multiple connection feature
which consists of protocol plugins. These plugins allow you to use
gaim to connect to other chat services such as Yahoo!, ICQ, MSN,
Jabber, Napster, Zephyr, IRC and Gadu-Gadu.

%description -l pl
Gaim pozwala na rozmowy z dowoln� osob� u퓓waj켧� us퀅gi AOL Instant
Messenger (mo퓆a si� zarejstrowa� pod adresem
http://www.aim.aol.com/). Program u퓓wa wersji TOC protoko퀅 AOL wi�c
Twoja lista kontakt�w jest zapisana na serwerze AOL i mo풽 byc
przes쿪na gdziekolwiek. Gaim zawiera wiele udogodnie� dost�pnych w
kliencie AOL IM jak r�wnie� dodaje w쿪sne. Gaim umo퓄iwia tak풽 dost�p
do us퀅g takich jak Yahoo!, ICQ, MSN, Jabber, Napster, Zephyr, IRC
oraz Gadu-Gadu.

%description -l pt_BR
GAIM � um cliente para o AOL Instant Messenger (AIM) que usa o servi�o
tik/toc da AOL. � desenvolvido ativamente e suporta muitas das
caracter�sticas do cliente da AOL, tendo uma interface similiar.
Tamb�m oferece suporte a outros protocolos, como: ICQ, IRC, Yahoo!,
MSN, Jabber e Napster.

%package ui-gtk
Summary:	gtk+ user interface for gaim
Summary(pl):	Interfejs u퓓tkownika gaim korzystaj켧y z gtk+
Group:		Applications/Communications
Provides:	gaim-ui = %{epoch}:%{version}-%{release}

%description ui-gtk
gtk+ user interface for gaim.

%description ui-gtk -l pl
Interfejs u퓓tkownika gaim korzystaj켧y z gtk+.

%package devel
Summary:	Development files for gaim-remote library
Summary(pl):	Pliki programistyczne biblioteki gaim-remote
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}

%description devel
Development files for gaim-remote library.

%description devel -l pl
Pliki programistyczne biblioteki gaim-remote.

%package perl
Summary:	Gaim files for perl scripts
Summary(pl):	Pliki Gaim dla skrypt�w perl
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}

%description perl
Gaim files for perl scripts.

%description perl -l pl
Pliki Gaim dla skrypt�w perl.

%package doc
Summary:	Gaim documentation for developers (HTML format)
Summary(pl):	Dokumentacja Gaim dla programist�w (format HTML)
Group:		Development/Libraries

%description doc
Gaim documentation for developers (HTML format).

%description doc -l pl
Dokumentacja Gaim dla programist�w (format HTML).

%prep
%setup -q 
%patch0 -p1
%patch1	-p1

%build
rm -f configure.in
%{__libtoolize}
%{__gettextize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--disable-nas \
	--enable-nss=no \
	--with-perl-lib=vendor

%{__make}
%{?with_doc:%{__make} docs}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/gaim/*.la

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README* HACKING doc/{CREDITS,FAQ}
%attr(755,root,root) %{_bindir}/gaim-remote
%attr(755,root,root) %{_libdir}/libgaim-remote.so.0.0.0
%dir %{_libdir}/gaim
%attr(755,root,root) %{_libdir}/gaim/[!i]*.so
%attr(755,root,root) %{_libdir}/gaim/idle*.so
%{_pixmapsdir}/*
%{_mandir}/man?/*
%{_datadir}/sounds/%{name}

%files ui-gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gaim
%attr(755,root,root) %{_libdir}/gaim/iconaway.so
%{_desktopdir}/gaim.desktop

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgaim-remote.so
%{_libdir}/libgaim-remote.la
%dir %{_includedir}/gaim-remote
%{_includedir}/gaim-remote/remote-socket.h
%{_includedir}/gaim-remote/remote.h

%files perl
%defattr(644,root,root,755)
%{perl_vendorarch}/*.pm
%dir %{perl_vendorarch}/auto/Gaim
%{perl_vendorarch}/auto/Gaim/*.ix
%{perl_vendorarch}/auto/Gaim/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Gaim/*.so

%if %{with doc}
%files doc
%defattr(644,root,root,755)
%doc doc/html/*.{html,png,css}
%endif
