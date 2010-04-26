# TODO
# - subpackages for
#  - different protocols (like kopete) - working, needs some more protocol packages
#  - huge deps (mono...)
# - kerberos 4 with zephyr support?
# - external zephyr?
#   http://packages.qa.debian.org/z/zephyr.html
# - update pl descriptions
# - restore e-d-s if http://developer.pidgin.im/ticket/10852 fixed
#
%bcond_without	cap		# without Contact Availability Prediction
%bcond_without	dbus		# without D-BUS (for pidgin-remote and others)
%bcond_without	doc		# do not generate and include documentation
%bcond_with	dotnet		# build with mono support
%bcond_with	evolution	# compile without the Pidgin-Evolution plugin
%bcond_with	gnutls		# use GnuTLS instead of NSS
%bcond_without	gtkspell	# without gtkspell support
%bcond_without	meanwhile	# without meanwhile support
%bcond_without	sasl		# disable SASL support
%bcond_without	text		# don't build text UI (finch)
%bcond_without 	silc		# Build without SILC libraries
%bcond_without 	nm		# NetworkManager support (requires D-Bus)

%if %{without dbus}
%undefine	with_nm
%endif

# plain i386 is not supported; mono uses cmpxchg/xadd which require i486
%ifarch i386
%undefine	with_dotnet
%endif

%define		gtk2_ver	2.10.6
%define		glib_ver	%(v=$(pkg-config --modversion glib-2.0 2>/dev/null | cut -d. -f 1,2); echo ${v:-ERROR})

%include	/usr/lib/rpm/macros.perl
Summary:	A client compatible with AOL's 'Instant Messenger'
Summary(de.UTF-8):	Pidgin ist ein Instant Messenger
Summary(hu.UTF-8):	Az AOL 'Instant Messenger'-ével kompatibilis kliens
Summary(ko.UTF-8):	AOL 인스턴트 메신저와 호환되는 클라이언트
Summary(pl.UTF-8):	Klient kompatybilny z AOL Instant Messenger
Summary(pt_BR.UTF-8):	Um cliente para o AOL Instant Messenger (AIM)
Name:		pidgin
Version:	2.6.6
Release:	2
License:	GPL v2+
Group:		Applications/Communications
Source0:	http://downloads.sourceforge.net/pidgin/%{name}-%{version}.tar.bz2
# Source0-md5:	b37ab6c52db8355e8c70c044c2ba17c1
Patch0:		%{name}-nolibs.patch
Patch1:		%{name}-dbus-dir.patch
Patch2:		%{name}-libgadu.patch
URL:		http://www.pidgin.im/
BuildRequires:	GConf2
BuildRequires:	GConf2-devel >= 2.16.0
%{?with_nm:BuildRequires:	NetworkManager-devel}
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.9
BuildRequires:	avahi-devel
BuildRequires:	avahi-glib-devel
BuildRequires:	check >= 0.9.4
%{?with_sasl:BuildRequires:	cyrus-sasl-devel}
%{?with_dbus:BuildRequires:	dbus-glib-devel >= 0.71}
%{?with_evolution:BuildRequires:	evolution-data-server-devel >= 1.8.1}
BuildRequires:	farsight2-devel
BuildRequires:	gettext-devel
%{?with_gnutls:BuildRequires:	gnutls-devel}
BuildRequires:	gstreamer-devel >= 0.10.10
BuildRequires:	gtk+2-devel >= 2:%{gtk2_ver}
%{?with_gtkspell:BuildRequires:	gtkspell-devel >= 1:2.0.16-2}
BuildRequires:	intltool
BuildRequires:	libgadu-devel
BuildRequires:	libidn-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.6.26
%{?with_meanwhile:BuildRequires:	meanwhile-devel >= 1.0.0}
%{?with_dotnet:BuildRequires:	mono-csharp}
%{?with_dotnet:BuildRequires:	mono-devel}
%{?with_text:BuildRequires:	ncurses-ext-devel}
%if %{without gnutls}
BuildRequires:	nspr-devel
BuildRequires:	nss-devel
%endif
BuildRequires:	perl-devel
BuildRequires:	pkgconfig
BuildRequires:	python-modules >= 1:2.4
BuildRequires:	rpm-perlprov
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.311
%{?with_silc:BuildRequires:	silc-toolkit-devel >= 1.1}
BuildRequires:	startup-notification-devel >= 0.5
BuildRequires:	tcl-devel
BuildRequires:	tk-devel
%if %{with cap}
BuildRequires:	sqlite3-devel >= 3.3
%endif
BuildRequires:	xorg-lib-libSM-devel
BuildRequires:	xorg-lib-libXScrnSaver-devel
%if %{with doc}
BuildRequires:	doxygen
BuildRequires:	graphviz
%endif
Requires(post,postun):	gtk+2
Requires(post,preun):	GConf2 >= 2.16.0
Requires:	hicolor-icon-theme
Requires:	libpurple = %{version}-%{release}
Requires:	libpurple-protocol
Suggests:	enchant-myspell
Obsoletes:	gaim
Obsoletes:	gaim-ui
Obsoletes:	gaim-ui-gtk
# discontinued gaim plugins
Obsoletes:	gaim-encryption
Obsoletes:	gaim-plugin-tlen
Obsoletes:	gaim-plugin-xmms-remote
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pidgin allows you to talk to anyone using AOL's Instant Messenger
service (you can sign up at http://www.aim.aol.com). It uses the TOC
version of the AOL protocol, so your buddy list is stored on AOL's
servers and can be retrieved from anywhere. It contains many of the
same features as AOL's IM client while at the same time incorporating
many new features. Pidgin also contains a multiple connection feature
which consists of protocol plugins. These plugins allow you to use
pidgin to connect to other chat services such as Yahoo!, ICQ, MSN,
Jabber, Napster, Zephyr, IRC and Gadu-Gadu.

The protocols are shipped by libpurple-protocol-foo.

%description -l hu.UTF-8
A Pidgin-nel beszélhetsz bárkivel, aki az AOL Instant Messenger
szolgáltatását használja (a http://www.aim.aol.com oldalon
íratkozhatsz fel). Az AOL protokoll TOC verzióját használja, így a
partnerlistád az AOL szerverein tárolják, így bárhonnan hozzáférhetsz.
Sok szolgáltatását tartalmazza az AOL IM kliensének, sőt néhány új
lehetőséget is tartalmaz. A Pidgin több kapcsolódási lehetőséggel
rendelkezik, amely a pluginoknak köszönhető. Ezen pluginok
segítségével a következő szerverekhez csatlakozhatsz: Yahoo!, ICQ,
MSN, Jabber, Napster, Zephyr, IRC és Gadu-Gadu.

A protokollokat a libpurple-protocol-foo csomagok szállítják.

%description -l pl.UTF-8
Pidgin pozwala na rozmowy z dowolną osobą używającą usługi AOL Instant
Messenger (można się zarejestrować pod adresem
http://www.aim.aol.com/). Program używa wersji TOC protokołu AOL więc
Twoja lista kontaktów jest zapisana na serwerze AOL i może być
przesłana gdziekolwiek. Pidgin zawiera wiele udogodnień dostępnych w
kliencie AOL IM jak również dodaje własne. Pidgin umożliwia także
dostęp do usług takich jak Yahoo!, ICQ, MSN, Jabber, Napster, Zephyr,
IRC oraz Gadu-Gadu.

%description -l pt_BR.UTF-8
Pidgin é um cliente para o AOL Instant Messenger (AIM) que usa o
serviço tik/toc da AOL. É desenvolvido ativamente e suporta muitas das
características do cliente da AOL, tendo uma interface similiar.
Também oferece suporte a outros protocolos, como: ICQ, IRC, Yahoo!,
MSN, Jabber e Napster.

%description -l de.UTF-8
Pidgin ist ein Instant Messenger der von Mark Spencer ursprünglich für
unixähnliche Systeme (GNU/Linux, BSD) geschrieben wurde, nun aber auch
auf Microsoft Windows und Mac OS X lauffähig ist und mit vielen
Plugins stark erweitert werden kann.

%package devel
Summary:	Development files for Pidgin client library
Summary(pl.UTF-8):	Pliki programistyczne biblioteki klienta Pidgina
Group:		Development/Libraries
Requires:	gtk+2-devel >= 2:%{gtk2_ver}
Requires:	libpurple-devel = %{version}-%{release}
Obsoletes:	gaim-devel

%description devel
Development files for Pidgin.

%description devel -l hu.UTF-8
Fejléc fájlok Pidginhez.

%description devel -l pl.UTF-8
Pliki programistyczne biblioteki Pidgina.

%package -n libpurple
Summary:	libpurple library for IM clients like Pidgin and Finch
Group:		Applications/Networking
%{?with_sasl:Requires:	cyrus-sasl-digest-md5}
%{?with_sasl:Requires:	cyrus-sasl-plain}
Requires:	glib2 >= 1:%{glib_ver}

%description -n libpurple
libpurple contains the core IM support for IM clients such as Pidgin
and Finch.

libpurple supports a variety of messaging protocols including AIM,
MSN, Yahoo!, Jabber, Bonjour, Gadu-Gadu, ICQ, IRC, Novell Groupwise,
QQ, Lotus Sametime, SILC, Simple and Zephyr.

%package -n libpurple-devel
Summary:	Development headers, documentation, and libraries for libpurple
Group:		Applications/Networking
Requires:	libpurple = %{version}-%{release}
%if %{with dbus}
Requires:	dbus-devel >= 0.60
%endif
Requires:	dbus-glib-devel >= 0.70

%description -n libpurple-devel
The libpurple-devel package contains the header files, developer
documentation, and libraries required for development of libpurple
based instant messaging clients or plugins for any libpurple based
client.

%package -n libpurple-perl
Summary:	Perl scripting support for libpurple
Group:		Applications/Networking
Requires:	libpurple = %{version}-%{release}

%description -n libpurple-perl
Perl plugin loader for libpurple. This package will allow you to write
or use libpurple plugins written in the Perl programming language.

%package -n libpurple-tcl
Summary:	Tcl scripting support for libpurple
Summary(hu.UTF-8):	Pidgin fájlok Tcl szkriptekhez
Summary(pl.UTF-8):	Pliki Pidgina dla skryptów w Tcl-u
Group:		Libraries
Requires:	libpurple = %{version}-%{release}
Obsoletes:	gaim-tcl
Obsoletes:	pidgin-tcl

%description -n libpurple-tcl
Tcl plugin loader for libpurple. This package will allow you to write
or use libpurple plugins written in the Tcl programming language.

%description -n libpurple-tcl -l hu.UTF-8
Ezzel a csomaggal lehetőséged nyílik a Pidgin lehetőségeit bővíteni
Tcl szkriptekkel.

%description -n libpurple-tcl -l pl.UTF-8
Ten pakiet daje możliwość rozszerzania funkcjonalności Pidgina za
pomocą skryptów w Tcl-u.

%package -n finch
Summary:	A text-based user interface for Pidgin
Group:		Applications/Networking
Requires:	libpurple = %{version}-%{release}

%description -n finch
A text-based user interface for using libpurple. This can be run from
a standard text console or from a terminal within X Windows. It uses
ncurses and our homegrown gnt library for drawing windows and text.

%package -n finch-devel
Summary:	Headers etc. for finch stuffs
Group:		Applications/Networking
Requires:	finch = %{version}-%{release}
Requires:	libpurple-devel = %{version}-%{release}
Requires:	ncurses-devel
Requires:	pkgconfig

%description -n finch-devel
The finch-devel package contains the header files, developer
documentation, and libraries required for development of Finch scripts
and plugins.

%package perl
Summary:	Pidgin files for Perl scripts
Summary(hu.UTF-8):	Pidgin fájlok Perl szkriptekhez
Summary(pl.UTF-8):	Pliki Pidgina dla skryptów w Perlu
Group:		Libraries
Requires:	libpurple = %{version}-%{release}
Requires:	libpurple-perl = %{version}-%{release}
Obsoletes:	gaim-perl

%description perl
This package gives you ability to extend Pidgin functionality with
Perl scripts.

%description perl -l hu.UTF-8
Ezzel a csomaggal lehetőséged nyílik a Pidgin lehetőségeit bővíteni
Perl szkriptekkel.

%description perl -l pl.UTF-8
Ten pakiet daje możliwość rozszerzania funkcjonalności Pidgina za
pomocą skryptów Perla.

%package plugin-evolution
Summary:	Plugin for Ximian Evolution integration
Summary(hu.UTF-8):	Plugin az Evolution-ba beépítéséhez
Summary(pl.UTF-8):	Wtyczka do integracji z Evolution
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	gaim-plugin-evolution

%description plugin-evolution
Provides integration with Ximian Evolution.

%description plugin-evolution -l hu.UTF-8
Plugin az Evolution-ba beépítéséhez.

%description plugin-evolution -l pl.UTF-8
Wtyczka do integracji z Evolution.

%package plugin-remote
Summary:	Pidgin Remote Control
Summary(hu.UTF-8):	Pidgin távoli irányítása
Summary(pl.UTF-8):	Zdalne sterowanie Pidginem
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	gaim-plugin-remote

%description plugin-remote
This package gives Pidgin the ability to be remote-controlled through
third-party applications or through the pidgin-remote tool.

%description plugin-remote -l hu.UTF-8
Ezzel a csomaggal lehetőséged nyílik a Pidgint távolról irányítani
külső alkalmazásokkal vagy a pidgin-remote eszközzel.

%description plugin-remote -l pl.UTF-8
Ten pakiet daje możliwość zdalnego sterowania Pidginem przez inne
aplikacje albo narzędzie pidgin-remote.

%package -n libpurple-protocol-aim
Summary:	Yahoo protocol support for AIM
Group:		Applications/Communications
Requires:	libpurple = %{version}-%{release}
Provides:	libpurple-protocol

%description -n libpurple-protocol-aim
AIM protocol support for pidgin.

%package -n libpurple-protocol-bonjour
Summary:	Yahoo protocol support for Bonjour
Group:		Applications/Communications
Requires:	libpurple = %{version}-%{release}
Provides:	libpurple-protocol

%description -n libpurple-protocol-bonjour
Bonjour protocol support for pidgin.

%package -n libpurple-protocol-gg
Summary:	Yahoo protocol support for Gadu-Gadu
Group:		Applications/Communications
Requires:	libpurple = %{version}-%{release}
Provides:	libpurple-protocol

%description -n libpurple-protocol-gg
Gadu-Gadu protocol support for pidgin.


%package -n libpurple-protocol-irc
Summary:	Yahoo protocol support for IRC
Group:		Applications/Communications
Requires:	libpurple = %{version}-%{release}
Provides:	libpurple-protocol

%description -n libpurple-protocol-irc
IRC protocol support for pidgin.

%package -n libpurple-protocol-icq
Summary:	Yahoo protocol support for ICQ
Group:		Applications/Communications
Requires:	libpurple = %{version}-%{release}
Provides:	libpurple-protocol

%description -n libpurple-protocol-icq
ICQ protocol support for pidgin.

%package -n libpurple-protocol-jabber
Summary:	Jabber protocol support for pidgin
Group:		Applications/Communications
Requires:	libpurple = %{version}-%{release}
Provides:	libpurple-protocol

%description -n libpurple-protocol-jabber
Jabber protocol support for pidgin.

%package -n libpurple-protocol-msn
Summary:	MSN protocol support for pidgin
Group:		Applications/Communications
Requires:	libpurple = %{version}-%{release}
Provides:	libpurple-protocol

%description -n libpurple-protocol-msn
MSN protocol support for pidgin.

%package -n libpurple-protocol-mtix
Summary:	MTix protocol support for pidgin
Group:		Applications/Communications
Requires:	libpurple = %{version}-%{release}
Provides:	libpurple-protocol

%description -n libpurple-protocol-mtix
MTix protocol support for pidgin.

%package -n libpurple-protocol-myspace
Summary:	MySpace protocol support for pidgin
Group:		Applications/Communications
Requires:	libpurple = %{version}-%{release}
Provides:	libpurple-protocol

%description -n libpurple-protocol-myspace
MySpace protocol support for pidgin.

%package -n libpurple-protocol-qq
Summary:	QQ protocol support for pidgin
Group:		Applications/Communications
Requires:	libpurple = %{version}-%{release}
Provides:	libpurple-protocol

%description -n libpurple-protocol-qq
QQ protocol support for pidgin.

%package -n libpurple-protocol-sametime
Summary:	Sametime protocol support for pidgin
Group:		Applications/Communications
Requires:	libpurple = %{version}-%{release}
Provides:	libpurple-protocol

%description -n libpurple-protocol-sametime
Sametime protocol support for pidgin.

%package -n libpurple-protocol-yahoo
Summary:	Yahoo protocol support for pidgin
Group:		Applications/Communications
Requires:	libpurple = %{version}-%{release}
Provides:	libpurple-protocol

%description -n libpurple-protocol-yahoo
Yahoo protocol support for pidgin.

%package -n libpurple-protocol-xmpp
Summary:	XMPP protocol support for pidgin (e.g. GTalk)
Group:		Applications/Communications
Requires:	libpurple = %{version}-%{release}
Provides:	libpurple-protocol

%description -n libpurple-protocol-xmpp
XMPP protocol support for pidgin (e.g. GTalk).

%package -n libpurple-protocol-zephyr
Summary:	Zephyr protocol support for pidgin
Group:		Applications/Communications
Requires:	libpurple = %{version}-%{release}
Provides:	libpurple-protocol

%description -n libpurple-protocol-zephyr
Zephyr protocol support for pidgin.

%package doc
Summary:	Pidgin documentation for developers (HTML format)
Summary(hu.UTF-8):	Pidgin dokumentáció fejlesztőknek (HTML formában)
Summary(pl.UTF-8):	Dokumentacja Pidgina dla programistów (format HTML)
Group:		Documentation
Obsoletes:	gaim-doc

%description doc
Pidgin documentation for developers (HTML format).

%description doc -l hu.UTF-8
Pidgin dokumentáció fejlesztőknek (HTML formátumban).

%description doc -l pl.UTF-8
Dokumentacja Pidgina dla programistów (format HTML).

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%if %{with dotnet}
if [ ! -f /proc/cpuinfo ]; then
	echo >&2 "Mono requires /proc to be mounted."
	exit 1
fi
%endif

%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4macros
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	%{!?with_gnutls:--enable-gnutls=no} \
	%{?with_gnutls:--enable-nss=no} \
	%{?with_doc:--enable-dot --enable-devhelp} \
	%{!?with_silc:--with-silc-includes=not_existent_directory} \
	--%{?with_cap:en}%{!?with_cap:dis}able-cap \
	%{?with_sasl:--enable-cyrus-sasl} \
	--%{?with_dbus:en}%{!?with_dbus:dis}able-dbus \
	--%{?with_nm:en}%{!?with_nm:dis}able-nm \
	--%{?with_evolution:en}%{!?with_evolution:dis}able-gevolution \
	%{!?with_gtkspell:--disable-gtkspell} \
	%{?with_dotnet:--enable-mono} \
	--%{?with_text:en}%{!?with_text:dis}able-consoleui

%{__make}
%{?with_doc:%{__make} docs}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/purple

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/finch/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/gnt/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/pidgin/{,private}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/purple-2/*.la
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/ca@valencia
%{__mv} $RPM_BUILD_ROOT%{_datadir}/locale/my{_MM,}
%{__mv} $RPM_BUILD_ROOT%{_datadir}/locale/ms{_MY,}

%find_lang %{name} --with-gnome
rm -f $RPM_BUILD_ROOT{%{perl_archlib}/perllocal.pod,%{perl_vendorarch}/auto/Pidgin/{,GtkUI}/.packlist}
rm -rf $RPM_BUILD_ROOT%{_datadir}/purple/ca-certs

%if %{with dbus}
rm $RPM_BUILD_ROOT%{_bindir}/purple-client-example
%endif

# no svg icons
rm $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps/pidgin.svg
rm -r $RPM_BUILD_ROOT%{_pixmapsdir}/pidgin/*/scalable

# rm windows icons
rm $RPM_BUILD_ROOT%{_pixmapsdir}/pidgin/tray/*/*.ico

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install purple.schemas
%update_icon_cache hicolor
if [ "$1" = 1 ]; then
%banner %{name} -e <<-EOF
	Please do not forget to install libpurple-protocols what do you need!
EOF
fi

%preun
%gconf_schema_uninstall purple.schemas

%postun
%update_icon_cache hicolor

%post	-n libpurple -p /sbin/ldconfig
%postun	-n libpurple -p /sbin/ldconfig

%post	-n finch	-p /sbin/ldconfig
%postun	-n finch	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog{,.API} HACKING NEWS PLUGIN_HOWTO README*
%attr(755,root,root) %{_bindir}/pidgin
%dir %{_libdir}/pidgin
%if %{with cap}
%attr(755,root,root) %{_libdir}/pidgin/cap.so
%endif
%attr(755,root,root) %{_libdir}/pidgin/convcolors.so
%attr(755,root,root) %{_libdir}/pidgin/extplacement.so
%attr(755,root,root) %{_libdir}/pidgin/pidginrc.so
%attr(755,root,root) %{_libdir}/pidgin/gestures.so
%attr(755,root,root) %{_libdir}/pidgin/gtkbuddynote.so
%attr(755,root,root) %{_libdir}/pidgin/history.so
%attr(755,root,root) %{_libdir}/pidgin/iconaway.so
%attr(755,root,root) %{_libdir}/pidgin/markerline.so
%attr(755,root,root) %{_libdir}/pidgin/notify.so
%attr(755,root,root) %{_libdir}/pidgin/relnot.so
%attr(755,root,root) %{_libdir}/pidgin/spellchk.so
%attr(755,root,root) %{_libdir}/pidgin/ticker.so
%attr(755,root,root) %{_libdir}/pidgin/timestamp.so
%attr(755,root,root) %{_libdir}/pidgin/timestamp_format.so
%attr(755,root,root) %{_libdir}/pidgin/vvconfig.so
%attr(755,root,root) %{_libdir}/pidgin/xmppconsole.so
%attr(755,root,root) %{_libdir}/pidgin/sendbutton.so
%attr(755,root,root) %{_libdir}/pidgin/themeedit.so
%attr(755,root,root) %{_libdir}/pidgin/xmppdisco.so
%if %{with dbus}
%attr(755,root,root) %{_libdir}/pidgin/musicmessaging.so
%endif
%{_mandir}/man1/pidgin.1*

%{_desktopdir}/pidgin.desktop
%{_pixmapsdir}/pidgin
%{_iconsdir}/hicolor/*/apps/pidgin.png

%files -n libpurple
%defattr(644,root,root,755)
%doc libpurple/purple-notifications-example
%dir %{_sysconfdir}/purple
%{_sysconfdir}/gconf/schemas/purple.schemas
%attr(755,root,root) %{_libdir}/libpurple.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpurple.so.0
%if %{with dbus}
%attr(755,root,root) %{_libdir}/libpurple-client.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpurple-client.so.0
%endif
%dir %{_libdir}/purple-2
%attr(755,root,root) %{_libdir}/purple-2/autoaccept.so
%attr(755,root,root) %{_libdir}/purple-2/buddynote.so
%attr(755,root,root) %{_libdir}/purple-2/idle.so
%attr(755,root,root) %{_libdir}/purple-2/joinpart.so
%attr(755,root,root) %{_libdir}/purple-2/libnovell.so
%attr(755,root,root) %{_libdir}/purple-2/liboscar.so.*
%attr(755,root,root) %{_libdir}/purple-2/liboscar.so
%attr(755,root,root) %{_libdir}/purple-2/libsimple.so
%attr(755,root,root) %{_libdir}/purple-2/log_reader.so
%attr(755,root,root) %{_libdir}/purple-2/newline.so
%attr(755,root,root) %{_libdir}/purple-2/offlinemsg.so
%attr(755,root,root) %{_libdir}/purple-2/psychic.so
%attr(755,root,root) %{_libdir}/purple-2/ssl.so
%attr(755,root,root) %{_libdir}/purple-2/statenotify.so
%if %{with dotnet}
%attr(755,root,root) %{_libdir}/purple-2/*.dll
%attr(755,root,root) %{_libdir}/purple-2/mono.so
%endif
%{?with_dbus:%attr(755,root,root) %{_libdir}/purple-2/dbus-example.so}
%{?with_silc:%attr(755,root,root) %{_libdir}/purple-2/libsilcpurple.so}
%{?with_gnutls:%attr(755,root,root) %{_libdir}/purple-2/ssl-gnutls.so}
%{!?with_gnutls:%attr(755,root,root) %{_libdir}/purple-2/ssl-nss.so}

%{_datadir}/sounds/purple
%{_datadir}/purple
%if %{with dbus}
%attr(755,root,root) %{_bindir}/purple-send
%attr(755,root,root) %{_bindir}/purple-send-async
%attr(755,root,root) %{_bindir}/purple-url-handler
%endif

%files -n libpurple-perl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/purple-2/perl.so
%dir %{_libdir}/purple-2/perl
%{_libdir}/purple-2/perl/*.pm
%dir %{_libdir}/purple-2/perl/auto
%dir %{_libdir}/purple-2/perl/auto/Purple
%{_libdir}/purple-2/perl/auto/Purple/*.bs
%{_libdir}/purple-2/perl/auto/Purple/*.ix
%attr(755,root,root) %{_libdir}/purple-2/perl/auto/Purple/*.so
%{_mandir}/man3/Purple.3pm*

%files -n libpurple-tcl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/purple-2/tcl.so

%files -n libpurple-devel
%defattr(644,root,root,755)
%{_aclocaldir}/purple.m4
%attr(755,root,root) %{_libdir}/libpurple.so
%{_libdir}/libpurple.la
%{_includedir}/libpurple
%{_pkgconfigdir}/purple.pc
%if %{with dbus}
%attr(755,root,root) %{_libdir}/libpurple-client.so
%{_libdir}/libpurple-client.la
%endif

%if %{with text}
%files -n finch
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/finch
%attr(755,root,root) %{_libdir}/libgnt.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgnt.so.0
%dir %{_libdir}/finch
%attr(755,root,root) %{_libdir}/finch/gntclipboard.so
%attr(755,root,root) %{_libdir}/finch/gntgf.so
%attr(755,root,root) %{_libdir}/finch/gnthistory.so
%attr(755,root,root) %{_libdir}/finch/gntlastlog.so
%attr(755,root,root) %{_libdir}/finch/gnttinyurl.so
%attr(755,root,root) %{_libdir}/finch/grouping.so
%dir %{_libdir}/gnt
%attr(755,root,root) %{_libdir}/gnt/*.so
%{_mandir}/man1/finch.*

%files -n finch-devel
%defattr(644,root,root,755)
%{_includedir}/finch
%{_includedir}/gnt
%attr(755,root,root) %{_libdir}/libgnt.so
%{_libdir}/libgnt.la
%{_pkgconfigdir}/finch.pc
%{_pkgconfigdir}/gnt.pc
%endif

%files devel
%defattr(644,root,root,755)
%{_includedir}/pidgin
%{_pkgconfigdir}/pidgin.pc

%files perl
%defattr(644,root,root,755)
%dir %{_libdir}/pidgin/perl
%{_libdir}/pidgin/perl/*.pm
%dir %{_libdir}/pidgin/perl/auto
%dir %{_libdir}/pidgin/perl/auto/Pidgin
%{_libdir}/pidgin/perl/auto/Pidgin/*.bs
%attr(755,root,root) %{_libdir}/pidgin/perl/auto/Pidgin/*.so
%{_mandir}/man3/Pidgin.3pm*

%if %{with evolution}
%files plugin-evolution
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/pidgin/gevolution.so
%endif

%if %{with dbus}
%files plugin-remote
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/purple-remote
%endif

%files -n libpurple-protocol-aim
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/purple-2/libaim.so

%files -n libpurple-protocol-bonjour
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/purple-2/libbonjour.so

%files -n libpurple-protocol-gg
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/purple-2/libgg.so

%files -n libpurple-protocol-irc
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/purple-2/libirc.so

%files -n libpurple-protocol-icq
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/purple-2/libicq.so

%files -n libpurple-protocol-jabber
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/purple-2/libjabber.so.*
%attr(755,root,root) %{_libdir}/purple-2/libjabber.so

%files -n libpurple-protocol-msn
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/purple-2/libmsn.so

%files -n libpurple-protocol-myspace
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/purple-2/libmyspace.so

%files -n libpurple-protocol-mtix
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/purple-2/libmxit.so

%files -n libpurple-protocol-qq
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/purple-2/libqq.so

%if %{with meanwhile}
%files -n libpurple-protocol-sametime
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/purple-2/libsametime.so
%endif

%files -n libpurple-protocol-xmpp
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/purple-2/libxmpp.so

%files -n libpurple-protocol-zephyr
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/purple-2/libzephyr.so

%files -n libpurple-protocol-yahoo
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/purple-2/libyahoo.so
%{_libdir}/purple-2/libyahoojp.so
%{_libdir}/purple-2/libymsg.so
%attr(755,root,root) %{_libdir}/purple-2/libymsg.so.0
%attr(755,root,root) %{_libdir}/purple-2/libymsg.so.0.0.0

%if %{with doc}
%files doc
%defattr(644,root,root,755)
%doc doc/html/*.{html,png,css}
%endif
