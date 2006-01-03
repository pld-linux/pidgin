# TODO
# - nas, silc/silcclient?
# - kerberos 4 with zephyr support?
# - external zephyr?
#   http://packages.qa.debian.org/z/zephyr.html
#
%bcond_without	doc		# do not generate and include documentation
%bcond_without	evolution	# compile without the Gaim-Evolution plugin
%bcond_without	gtkspell	# without gtkspell support
%bcond_without	dbus	# without dbus (for gaim-remote and others)
#
%define		_pre	beta1
%include        /usr/lib/rpm/macros.perl
Summary:	A client compatible with AOL's 'Instant Messenger'
Summary(ko):	AOL 인스턴트 메신저와 호환되는 클라이언트
Summary(pl):	Klient kompatybilny z AOL Instant Messenger
Summary(pt_BR):	Um cliente para o AOL Instant Messenger (AIM)
Summary(de):	Gaim ist ein Instant Messenger
Name:		gaim
Version:	2.0.0
Release:	0.%{_pre}.2
Epoch:		1
License:	GPL
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/gaim/%{name}-%{version}%{_pre}.tar.bz2
# Source0-md5:	15d2c460112af93ceff4818f29f6c1b8
#Source0:	http://dl.sourceforge.net/gaim/%{name}-%{version}.tar.bz2
Patch0:		%{name}-nolibs.patch
Patch1:		%{name}-desktop.patch
Patch2:		%{name}-GG-evo.patch
Patch3:		%{name}-va.patch
URL:		http://gaim.sourceforge.net/
BuildRequires:	audiofile-devel
BuildRequires:	autoconf
BuildRequires:	automake
%{?with_dbus:BuildRequires:	dbus-glib-devel >= 0.35}
%{?with_evolution:BuildRequires: evolution-data-server-devel >= 0.0.95}
BuildRequires:	gettext-devel
BuildRequires:	gettext-autopoint
BuildRequires:	gtk+2-devel >= 1:2.2.0
%{?with_gtkspell:BuildRequires: gtkspell-devel >= 2.0.4}
BuildRequires:	howl-devel
BuildRequires:	libao-devel
BuildRequires:	libtool
BuildRequires:	perl-devel
BuildRequires:	pkgconfig
BuildRequires:	rpm-perlprov
BuildRequires:	rpmbuild(macros) >= 1.177
BuildRequires:	tcl-devel
BuildRequires:	tk-devel
BuildRequires:	xcursor-devel
%if %{with doc}
BuildRequires:	doxygen
BuildRequires:	graphviz
%endif
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
#Requires:	libao
# weird: it *should* break after DynaLoader's version change, but it doesn't
#Requires:	perl(DynaLoader) = %(%{__perl} -MDynaLoader -e 'print DynaLoader->VERSION')
Obsoletes:	gaim-ui
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
Messenger (mo퓆a si� zarejestrowa� pod adresem
http://www.aim.aol.com/). Program u퓓wa wersji TOC protoko퀅 AOL wi�c
Twoja lista kontakt�w jest zapisana na serwerze AOL i mo풽 by�
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

%description -l de
Gaim ist ein Instant Messenger der von Mark Spencer urspr�nglich f�r
unix�hnliche Systeme (GNU/Linux, BSD) geschrieben wurde, nun aber auch
auf Microsoft Windows und Mac OS X lauff�hig ist und mit vielen
Plugins stark erweitert werden kann.

%package libs
Summary:	Gaim client library
Summary(pl):	Biblioteka klienta Gaim
Group:		Libraries
Epoch:		1

%description libs
Gaim client library.

%description libs -l pl
Biblioteka klienta Gaim.

%package devel
Summary:	Development files for Gaim client library
Summary(pl):	Pliki programistyczne biblioteki klienta Gaim
Group:		Development/Libraries
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Requires:	glib2-devel >= 2.0.0
Requires:	gtk+2-devel >= 1:2.2.0

%description devel
Development files for gaim.

%description devel -l pl
Pliki programistyczne biblioteki gaim-remote.

%package perl
Summary:	Gaim files for Perl scripts
Summary(pl):	Pliki Gaima dla skrypt�w w Perlu
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description perl
This package gives you ability to extend Gaim functionality with Perl
scripts.

%description perl -l pl
Ten pakiet daje mo퓄iwo뜻 rozszerzania funkcjonalno턢i Gaima za pomoc�
skrypt�w Perla.

%package tcl
Summary:	Gaim files for Tcl scripts
Summary(pl):	Pliki Gaima dla skrypt�w w Tcl-u
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description tcl
This package gives you ability to extend Gaim functionality with Tcl
scripts.

%description tcl -l pl
Ten pakiet daje mo퓄iwo뜻 rozszerzania funkcjonalno턢i Gaima za pomoc�
skrypt�w w Tcl-u.

%package plugin-evolution
Summary:	Plugin for Ximian Evolution integration
Summary(pl):	Wtyczka do integracji z Evolution
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-evolution
Provides integration with Ximian Evolution.

%description plugin-evolution -l pl
Wtyczka do integracji z Evolution.

%package plugin-remote
Summary:	Gaim Remote Control
Summary(pl):	Zdalne sterowanie Gaimem
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-remote
This package gives Gaim the ability to be remote-controlled through
third-party applications or through the gaim-remote tool.

%description plugin-remote -l pl
Ten pakiet daje mo퓄iwo뜻 zdalnego sterowania Gaimem przez inne
aplikacje albo narz�dzie gaim-remote.

%package doc
Summary:	Gaim documentation for developers (HTML format)
Summary(pl):	Dokumentacja Gaim dla programist�w (format HTML)
Group:		Documentation

%description doc
Gaim documentation for developers (HTML format).

%description doc -l pl
Dokumentacja Gaim dla programist�w (format HTML).

%triggerpostun -- %{name} < 1:1.3.1-1.10
%banner -e %{name} <<EOF
The Ximian Evolution and gaim-remote plugins have been separated to separate packages.
If you need then please install %{name}-plugin-evolution and %{name}-plugin-remote
EOF

%prep
%setup -qn %{name}-%{version}%{_pre}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
./setup-gettext
%{__libtoolize}
%{__aclocal} -I m4macros
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--disable-nas \
	--enable-nss=no \
	--with-perl-lib=vendor \
	%{?with_dbus:--enable-dbus --with-dbus-session-dir=/usr/share/dbus-1} \
	%{!?with_evolution:--disable-gevolution} \
	%{!?with_gtkspell:--disable-gtkspell}

%{__make}
%{?with_doc:%{__make} docs}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/gaim/*.la

%find_lang %{name} --with-gnome --all-name
rm -f $RPM_BUILD_ROOT{%{perl_archlib}/perllocal.pod,%{perl_vendorarch}/auto/Gaim/.packlist}

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README* HACKING doc/{CREDITS,FAQ}
%attr(755,root,root) %{_bindir}/gaim
%dir %{_libdir}/gaim
%attr(755,root,root) %{_libdir}/gaim/docklet.so
%attr(755,root,root) %{_libdir}/gaim/extplacement.so
%attr(755,root,root) %{_libdir}/gaim/gaimrc.so
%attr(755,root,root) %{_libdir}/gaim/gestures.so
%attr(755,root,root) %{_libdir}/gaim/history.so
%attr(755,root,root) %{_libdir}/gaim/iconaway.so
%attr(755,root,root) %{_libdir}/gaim/idle.so
%attr(755,root,root) %{_libdir}/gaim/libbonjour.so
%attr(755,root,root) %{_libdir}/gaim/libgg.so
%attr(755,root,root) %{_libdir}/gaim/libirc.so
%attr(755,root,root) %{_libdir}/gaim/libjabber.so
%attr(755,root,root) %{_libdir}/gaim/libmsn.so
%attr(755,root,root) %{_libdir}/gaim/libnovell.so
%attr(755,root,root) %{_libdir}/gaim/liboscar.so
%attr(755,root,root) %{_libdir}/gaim/libsimple.so
%attr(755,root,root) %{_libdir}/gaim/libyahoo.so
%attr(755,root,root) %{_libdir}/gaim/libzephyr.so
%attr(755,root,root) %{_libdir}/gaim/notify.so
%attr(755,root,root) %{_libdir}/gaim/relnot.so
%attr(755,root,root) %{_libdir}/gaim/spellchk.so
%attr(755,root,root) %{_libdir}/gaim/ssl-gnutls.so
%attr(755,root,root) %{_libdir}/gaim/ssl-nss.so
%attr(755,root,root) %{_libdir}/gaim/ssl.so
%attr(755,root,root) %{_libdir}/gaim/statenotify.so
%attr(755,root,root) %{_libdir}/gaim/ticker.so
%attr(755,root,root) %{_libdir}/gaim/timestamp.so
%if %{with dbus}
%attr(755,root,root) %{_libdir}/gaim/musicmessaging.so
%endif
%{_datadir}/sounds/%{name}
%{_mandir}/man?/*

%{_desktopdir}/gaim.desktop
%{_pixmapsdir}/*

%files libs
%defattr(644,root,root,755)
%if %{with dbus}
%attr(755,root,root) %{_libdir}/libgaim-client.so.*.*.*
%endif

%files devel
%defattr(644,root,root,755)
%if %{with dbus}
%attr(755,root,root) %{_libdir}/libgaim-client.so
%{_libdir}/libgaim-client.la
%endif
%{_aclocaldir}/*.m4
%dir %{_includedir}/gaim
%{_includedir}/gaim/*.h
%{_pkgconfigdir}/*

%files perl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gaim/libgaimperl.so
%attr(755,root,root) %{_libdir}/gaim/perl.so
%{perl_vendorarch}/*.pm
%dir %{perl_vendorarch}/auto/Gaim
%{perl_vendorarch}/auto/Gaim/*.ix
%{perl_vendorarch}/auto/Gaim/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Gaim/*.so

%files tcl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gaim/tcl.so

%if %{with evolution}
%files plugin-evolution
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gaim/gevolution.so
%endif

%if %{with dbus}
%files plugin-remote
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gaim-remote.py
%endif

%if %{with doc}
%files doc
%defattr(644,root,root,755)
%doc doc/html/*.{html,png,css}
%endif
