# TODO
# - fix broken linking, see filterout_ld
# - fix unref symbols:
#   Unresolved symbols found in: /usr/lib64/purple-2/libjabber.so.0
#   Unresolved symbols found in: /usr/lib64/purple-2/liboscar.so.0
#   Unresolved symbols found in: /usr/lib64/purple-2/libymsg.so.0
# - perl is installed to wrong dir on x8664:
#   /usr/lib/perl5/x86_64-pld-linux-thread-multi/perllocal.pod
# - subpackages for
#  - huge deps (mono...)
# - kerberos 4 with zephyr support?
# - external zephyr?
#   http://packages.qa.debian.org/z/zephyr.html
# - gtk3 status: http://developer.pidgin.im/wiki/GTK3
#
%bcond_without	cap		# without Contact Availability Prediction
%bcond_without	dbus		# without D-BUS (for pidgin-remote and others)
%bcond_without	doc		# do not generate and include documentation
%bcond_with	dotnet		# build with mono support
%bcond_without	perl		# build without Perl support
%bcond_with	evolution	# compile without the Pidgin-Evolution plugin
%bcond_with	gnutls		# use GnuTLS instead of NSS
%bcond_without	gtkspell	# without gtkspell support
%bcond_without	meanwhile	# without meanwhile support
%bcond_without	sasl		# disable SASL support
%bcond_without	text		# don't build text UI (finch)
%bcond_without	silc		# Build without SILC libraries
%bcond_without	nm		# NetworkManager support (requires D-Bus)
%bcond_without	vv		# Voice and Video support

%if %{without dbus}
%undefine	with_nm
%endif

# plain i386 is not supported; mono uses cmpxchg/xadd which require i486
%ifarch i386
%undefine	with_dotnet
%endif

%define		gtk2_ver	2.10.6
%define		glib2_ver	2.24.0

%{?with_perl:%include	/usr/lib/rpm/macros.perl}
Summary:	A GTK+ based multiprotocol instant messaging client
Summary(de.UTF-8):	Pidgin ist ein Instant Messenger
Summary(hu.UTF-8):	Az AOL 'Instant Messenger'-ével kompatibilis kliens
Summary(ko.UTF-8):	AOL 인스턴트 메신저와 호환되는 클라이언트
Summary(pl.UTF-8):	Oparty na GTK+ klient komunikatorów obsługujący wiele protokołów
Summary(pt_BR.UTF-8):	Um cliente para o AOL Instant Messenger (AIM)
Name:		pidgin
Version:	2.13.0
Release:	5
License:	GPL v2+
Group:		Applications/Communications
Source0:	http://downloads.sourceforge.net/pidgin/%{name}-%{version}.tar.bz2
# Source0-md5:	423403494fe1951e47cc75231f743bb0
Patch0:		%{name}-nolibs.patch
Patch1:		%{name}-dbus-dir.patch
# Patch2:		%{name}-libgadu.patch
# http://developer.pidgin.im/ticket/14936
Patch3:		%{name}-port-to-farstream.patch
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
BuildRequires:	farstream-devel
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:%{glib2_ver}
%{?with_gnutls:BuildRequires:	gnutls-devel}
BuildRequires:	gstreamer0.10-devel >= 0.10.10
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
BuildRequires:	rpm >= 4.4.9-56
%if %{without gnutls}
BuildRequires:	nspr-devel
BuildRequires:	nss-devel
%endif
%{?with_perl:BuildRequires:	perl-devel}
BuildRequires:	pkgconfig
BuildRequires:	protobuf-c-devel
BuildRequires:	python-modules >= 1:2.4
%{?with_perl:BuildRequires:	rpm-perlprov}
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.583
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
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
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
Obsoletes:	libpurple-protocol-msn
Obsoletes:	libpurple-protocol-mxit
Obsoletes:	libpurple-protocol-myspace
Obsoletes:	libpurple-protocol-yahoo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# keep in sync ca-certificates
%if "%{pld_release}" == "th"
%define		openssldir	/etc/openssl/certs
%else
%define		openssldir	/var/lib/openssl/certs
%endif

# /usr/bin/ld: gntaccount.o: undefined reference to symbol 'cur_term'
# /usr/bin/ld: note: 'cur_term' is defined in DSO /lib64/libtinfow.so.6 so try adding it to the linker command line
# /lib64/libtinfow.so.6: could not read symbols: Invalid operation
%define		filterout_ld	-Wl,--no-copy-dt-needed-entries

# lots of purple and libxml syms
%define		skip_post_check_so	libjabber.so.0 libymsg.so.0 liboscar.so.0

%description
Pidgin allows you to talk to anyone using a variety of messaging
protocols including AIM, MSN, Yahoo!, Jabber, Bonjour, Gadu-Gadu, ICQ,
IRC, Novell Groupwise, QQ, Lotus Sametime, SILC, Simple and Zephyr.

The protocol plugins are packaged as libpurple-protocol-foo.

Pidgin supports many common features of other clients, as well as many
unique features, such as perl scripting, TCL scripting and C plugins.

Pidgin is not affiliated with or endorsed by America Online, Inc.,
Microsoft Corporation, Yahoo! Inc., or ICQ Inc.

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
Pidgin pozwala na rozmowy z osobami używającymi różnych protokołów
komunikatorów, w tym: AIM, MSN, Yahoo!, Jabber, Bonjour, Gadu-Gadu,
ICQ, IRC, Novell Groupwise, QQ, Lotus Sametime, SILC, Simple i Zephyr.

Wtyczki dla protokołów znajdują się w pakietach libpurple-protocol-*.

Pidgin obsługuje wiele popularnych funkcji innych klientów, a także
wiele własnych, takich jak obsługa skryptów perla i Tcl-a oraz wtyczek
w C.

Pidgin nie jest powiązany ani autoryzowany przez firmy America Online
Inc., Microsoft Corporation, Yahoo! Inc ani ICQ Inc.

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
Summary(pl.UTF-8):	Biblioteka libpurple dla klientów komunikatorów, takich jak Pidgin czy Finch
Group:		Applications/Networking
Requires:	ca-certificates
%{?with_sasl:Requires: cyrus-sasl-digest-md5}
%{?with_sasl:Requires: cyrus-sasl-plain}
Requires:	glib2 >= 1:%{glib2_ver}
Obsoletes:	libpurple-protocol-dir < 2.6.6-2
Obsoletes:	pidgin-libs < 2.6.6-2

%description -n libpurple
libpurple contains the core IM support for IM clients such as Pidgin
and Finch.

libpurple supports a variety of messaging protocols including AIM,
MSN, Yahoo!, Jabber, Bonjour, Gadu-Gadu, ICQ, IRC, Novell Groupwise,
QQ, Lotus Sametime, SILC, Simple and Zephyr.

%description -n libpurple -l pl.UTF-8
libpurple zawiera podstawową obsługę komunikacji dla klientów
komunikatorów takich jak Pidgin czy Finch.

libpurple obsługuje wiele protokołów komunikatorów, w tym AIM, MSN,
Yahoo!, Jabber, Bonjour, Gadu-Gadu, ICQ, IRC, Novell Groupwise, QQ,
Lotus Sametime, SILC, Simple i Zephyr.

%package -n libpurple-devel
Summary:	Development headers and other files libpurple
Summary(pl.UTF-8):	Pliki nagłówkowe i inne programistyczne do biblioteki libpurple
Group:		Applications/Networking
Requires:	libpurple = %{version}-%{release}
%if %{with dbus}
Requires:	dbus-devel >= 0.60
%endif
Requires:	dbus-glib-devel >= 0.70
Requires:	farstream-devel
Obsoletes:	pidgin-devel < 2.6.6-2

%description -n libpurple-devel
The libpurple-devel package contains the header files and other
development files required for development of libpurple based instant
messaging clients or plugins for any libpurple based client.

%description -n libpurple-devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe oraz inne niezbędne do
programowania komunikatorów opartych na bibliotece libpurple oraz
wtyczek dla tej biblioteki.

%package -n libpurple-perl
Summary:	Perl scripting support for libpurple
Summary(pl.UTF-8):	Obsługa skryptów Perla dla libpurple
Group:		Applications/Networking
Requires:	libpurple = %{version}-%{release}

%description -n libpurple-perl
Perl plugin loader for libpurple. This package will allow you to write
or use libpurple plugins written in the Perl programming language.

%description -n libpurple-perl -l pl.UTF-8
Moduł wczytujący wtyczki perlowe dla libpurple. Umożliwia tworzenie
oraz wykorzystywanie wtyczek dla libpurple napisanych w języku Perl.

%package -n libpurple-tcl
Summary:	Tcl scripting support for libpurple
Summary(hu.UTF-8):	Pidgin fájlok Tcl szkriptekhez
Summary(pl.UTF-8):	Obsługa skryptów Tcl-a dla libpurple
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
Moduł wczytujący wtyczki Tcl-a dla libpurple. Umożliwia tworzenie oraz
wykorzystywanie wtyczek dla libpurple napisanych w języku Tcl.

%package -n finch
Summary:	A text-based user interface for Pidgin
Summary(pl.UTF-8):	Tekstowy interfejs użytkownika dla Pidgina
Group:		Applications/Networking
Requires:	libpurple = %{version}-%{release}

%description -n finch
A text-based user interface for using libpurple. This can be run from
a standard text console or from a terminal within X Window System. It
uses ncurses and our homegrown gnt library for drawing windows and
text.

%description -n finch -l pl.UTF-8
Tekstowy interfejs użytkownika wykorzystujący libpurple. Może być
uruchamiany na standardowej konsoli tekstowej lub z poziomu terminala
w systemi X Window. Wykorzystuje ncurses oraz własną bibliotekę gnt do
rysowania okien i wyświetlania tekstu.

%package -n finch-devel
Summary:	Header files and similar for Finch stuffs
Summary(pl.UTF-8):	Pliki nagłówkowe do elementów Fincha
Group:		Applications/Networking
Requires:	finch = %{version}-%{release}
Requires:	libpurple-devel = %{version}-%{release}
Requires:	ncurses-devel

%description -n finch-devel
The finch-devel package contains the header files and other
development files required for development of Finch scripts and
plugins.

%description -n finch-devel -l pl.UTF-8
Ten pakiet zwiera pliki nagłówkowe oraz inne niezbędne do
programowania skryptów oraz wtyczek do Fincha.

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

%package -n libpurple-protocol-oscar
Summary:	Oscar protocol (AIM/ICQ Networks) support for libpurple
Summary(pl.UTF-8):	Obsługa protokołu Oscar (sieci AIM/ICQ) dla biblioteki libpurple
Group:		Applications/Communications
Requires:	libpurple = %{version}-%{release}
Provides:	libpurple-protocol
Obsoletes:	libpurple-protocol-aim
Obsoletes:	libpurple-protocol-icq

%description -n libpurple-protocol-oscar
Oscar protocol (AIM/ICQ Networks) support for libpurple.

%description -n libpurple-protocol-oscar -l pl.UTF-8
Obsługa protokołu Oscar (sieci AIM/ICQ) dla biblioteki libpurple.

%package -n libpurple-protocol-bonjour
Summary:	Bonjour protocol support for libpurple
Summary(pl.UTF-8):	Obsługa protokołu Bonjour dla biblioteki libpurple
Group:		Applications/Communications
Requires:	libpurple = %{version}-%{release}
Provides:	libpurple-protocol

%description -n libpurple-protocol-bonjour
Bonjour protocol support for libpurple.

%description -n libpurple-protocol-bonjour -l pl.UTF-8
Obsługa protokołu Bonjour dla biblioteki libpurple.

%package -n libpurple-protocol-gg
Summary:	Gadu-Gadu protocol support for libpurple
Summary(pl.UTF-8):	Obsługa protokołu Gadu-Gadu dla biblioteki libpurple
Group:		Applications/Communications
Requires:	libpurple = %{version}-%{release}
Provides:	libpurple-protocol

%description -n libpurple-protocol-gg
Gadu-Gadu protocol support for libpurple.

%description -n libpurple-protocol-gg -l pl.UTF-8
Obsługa protokołu Gadu-Gadu dla biblioteki libpurple.

%package -n libpurple-protocol-groupwise
Summary:	Novell GroupWise Messenger protocol support for libpurple
Summary(pl.UTF-8):	Obsługa protokołu aplikacji Novell GroupWise Messenger dla biblioteki libpurple
Group:		Applications/Communications
Requires:	libpurple = %{version}-%{release}
Provides:	libpurple-protocol

%description -n libpurple-protocol-groupwise
Novell GroupWise Messenger protocol support for libpurple.

%description -n libpurple-protocol-groupwise -l pl.UTF-8
Obsługa protokołu aplikacji Novell GroupWise Messenger dla biblioteki
libpurple.

%package -n libpurple-protocol-irc
Summary:	IRC protocol support for libpurple
Summary(pl.UTF-8):	Obsługa protokołu IRC dla biblioteki libpurple
Group:		Applications/Communications
Requires:	libpurple = %{version}-%{release}
Provides:	libpurple-protocol

%description -n libpurple-protocol-irc
IRC protocol support for libpurple.

%description -n libpurple-protocol-irc -l pl.UTF-8
Obsługa protokołu IRC dla biblioteki libpurple.

%package -n libpurple-protocol-simple
Summary:	SIP/SIMPLE protocol support for libpurple
Summary(pl.UTF-8):	Obsługa protokołu SIP/SIMPLE dla libpurple
Group:		Applications/Communications
Requires:	libpurple = %{version}-%{release}
Provides:	libpurple-protocol

%description -n libpurple-protocol-simple
SIP/SIMPLE protocol support for libpurple.

%description -n libpurple-protocol-simple -l pl.UTF-8
Obsługa protokołu SIP/SIMPLE dla libpurple.

%package -n libpurple-protocol-sametime
Summary:	Lotus Sametime protocol support for libpurple
Summary(pl.UTF-8):	Obsługa protokołu Lotus Sametime dla libpurple
Group:		Applications/Communications
URL:		http://meanwhile.sourceforge.net/
Requires:	libpurple = %{version}-%{release}
Provides:	libpurple-protocol

%description -n libpurple-protocol-sametime
Lotus Sametime protocol support for libpurple. This plugin relies on
MeanWhile library.

%description -n libpurple-protocol-sametime -l pl.UTF-8
Obsługa protokołu Lotus Sametime dla libpurple. Ta wtyczka
wykorzystuje bibliotekę MeanWhile.

%package -n libpurple-protocol-silc
Summary:	SILC protocol support for libpurple
Summary(pl.UTF-8):	Obsługa protokołu SILC dla libpurple
Group:		Applications/Communications
URL:		http://silcnet.org/
Requires:	libpurple = %{version}-%{release}
Provides:	libpurple-protocol

%description -n libpurple-protocol-silc
Secure Internet Live Conferencing (SILC) protocol support for
libpurple.

%description -n libpurple-protocol-silc -l pl.UTF-8
Obsługa protokołu SILC (Secure Internet Live Conferencing) dla
libpurple.

%package -n libpurple-protocol-xmpp
Summary:	XMPP (Jabber, GTalk) protocol support for libpurple
Summary(pl.UTF-8):	Obsługa protokołu XMPP (Jabber, GTalk) dla libpurple
Group:		Applications/Communications
Requires:	libpurple = %{version}-%{release}
Provides:	libpurple-protocol
Obsoletes:	libpurple-protocol-jabber

%description -n libpurple-protocol-xmpp
Extensible Messaging and Presence Protocol (XMPP) protocol support for
libpurple. This protocol is used by e.g. Jabber or GTalk.

%description -n libpurple-protocol-xmpp -l pl.UTF-8
Obsługa protokołu XMPP (Extensible Messaging and Presence Protocol)
dla biblioteki libpurple. Protokół ten jest wykorzystywany m.in. przez
Jabbera i GTalk.

%package -n libpurple-protocol-zephyr
Summary:	Zephyr protocol support for libpurple
Summary(pl.UTF-8):	Obsługa protokołu Zephyr dla libpurple
Group:		Applications/Communications
Requires:	libpurple = %{version}-%{release}
Provides:	libpurple-protocol

%description -n libpurple-protocol-zephyr
Zephyr protocol support for libpurple.

%description -n libpurple-protocol-zephyr -l pl.UTF-8
Obsługa protokołu Zephyr dla libpurple.

%package doc
Summary:	Pidgin documentation for developers (HTML format)
Summary(hu.UTF-8):	Pidgin dokumentáció fejlesztőknek (HTML formában)
Summary(pl.UTF-8):	Dokumentacja Pidgina dla programistów (format HTML)
Group:		Documentation
Obsoletes:	gaim-doc
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

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
#%%patch2 -p1
#%patch3 -p1

%build
%if %{with dotnet}
if [ ! -f /proc/cpuinfo ]; then
	echo >&2 "Mono requires /proc to be mounted."
	exit 1
fi
%endif

# %{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4macros
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--with-extraversion=%{release} \
	--with-system-ssl-certs=%{openssldir} \
	--disable-schemas-install \
	--disable-silent-rules \
	--%{?with_vv:en}%{!?with_vv:dis}able-vv \
	%{!?with_gnutls:--enable-gnutls=no} \
	%{?with_gnutls:--enable-nss=no} \
	%{?with_doc:--enable-dot --enable-devhelp} \
	%{!?with_silc:--with-silc-includes=not_existent_directory} \
	%{?with_sasl:--enable-cyrus-sasl} \
	--%{?with_cap:en}%{!?with_cap:dis}able-cap \
	--%{?with_dbus:en}%{!?with_dbus:dis}able-dbus \
	--%{?with_nm:en}%{!?with_nm:dis}able-nm \
	--%{?with_evolution:en}%{!?with_evolution:dis}able-gevolution \
	--%{!?with_gtkspell:dis}%{?with_gtkspell:en}able-gtkspell \
	--%{!?with_dotnet:dis}%{?with_dotnet:en}able-mono \
	--%{!?with_perl:dis}%{?with_perl:en}able-perl \
	--%{?with_text:en}%{!?with_text:dis}able-consoleui \
	--with-gadu-libs=%{_libdir} \
	--with-gadu-includes=%{_includedir}

%{__make}
%{?with_doc:%{__make} docs}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/purple

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/mhr
%{__mv} $RPM_BUILD_ROOT%{_localedir}/my{_MM,}
%{__mv} $RPM_BUILD_ROOT%{_localedir}/ms{_MY,}
%{__rm} -rf $RPM_BUILD_ROOT%{_localedir}/ku_IQ

%find_lang %{name} --with-gnome

%{__rm} $RPM_BUILD_ROOT%{_libdir}/finch/*.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/gnt/*.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/pidgin/*.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/purple-2/*.la

%if %{with perl}
%{__rm} $RPM_BUILD_ROOT%{_prefix}/lib/perl5/*/perllocal.pod
%{__rm} $RPM_BUILD_ROOT%{_libdir}/pidgin/perl/auto/Pidgin/.packlist
%{__rm} $RPM_BUILD_ROOT%{_libdir}/purple-2/perl/auto/Purple/.packlist
%endif

%if %{with dbus}
%{__rm} $RPM_BUILD_ROOT%{_bindir}/purple-client-example
%{__rm} $RPM_BUILD_ROOT%{_libdir}/purple-2/dbus-example.so
%endif

# resolve soname symlinks, affected plugins have rpath pointing there
for a in $RPM_BUILD_ROOT%{_libdir}/purple-2/lib*.so.*.*.*; do
	soname=$(objdump -p $a | awk '/SONAME/{print $2}')
	mv $a $(dirname $a)/$soname
	rm ${a%.*.*.*}
done

# rm windows icons
%{__rm} $RPM_BUILD_ROOT%{_pixmapsdir}/pidgin/tray/*/*.ico

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
%{_sysconfdir}/gconf/schemas/purple.schemas
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
%attr(755,root,root) %{_libdir}/pidgin/transparency.so
%{?with_vv:%attr(755,root,root) %{_libdir}/pidgin/vvconfig.so}
%attr(755,root,root) %{_libdir}/pidgin/xmppconsole.so
%attr(755,root,root) %{_libdir}/pidgin/sendbutton.so
%attr(755,root,root) %{_libdir}/pidgin/themeedit.so
%attr(755,root,root) %{_libdir}/pidgin/xmppdisco.so
%if %{with dbus}
%attr(755,root,root) %{_libdir}/pidgin/musicmessaging.so
%endif
%{_mandir}/man1/pidgin.1*

%{_datadir}/appdata/pidgin.appdata.xml
%{_desktopdir}/pidgin.desktop
%{_pixmapsdir}/pidgin
%{_iconsdir}/hicolor/*/apps/pidgin.png
%{_iconsdir}/hicolor/*/apps/pidgin.svg

%files -n libpurple
%defattr(644,root,root,755)
%doc libpurple/purple-notifications-example
%dir %{_sysconfdir}/purple
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
%attr(755,root,root) %{_libdir}/purple-2/log_reader.so
%attr(755,root,root) %{_libdir}/purple-2/newline.so
%attr(755,root,root) %{_libdir}/purple-2/offlinemsg.so
%attr(755,root,root) %{_libdir}/purple-2/psychic.so
%attr(755,root,root) %{_libdir}/purple-2/ssl.so
%attr(755,root,root) %{_libdir}/purple-2/nss-prefs.so
%{?with_gnutls:%attr(755,root,root) %{_libdir}/purple-2/ssl-gnutls.so}
%{!?with_gnutls:%attr(755,root,root) %{_libdir}/purple-2/ssl-nss.so}
%attr(755,root,root) %{_libdir}/purple-2/statenotify.so
%if %{with dotnet}
#%attr(755,root,root) %{_libdir}/purple-2/*.dll
#%attr(755,root,root) %{_libdir}/purple-2/mono.so
%endif

%{_datadir}/sounds/purple
%if %{with dbus}
%attr(755,root,root) %{_bindir}/purple-send
%attr(755,root,root) %{_bindir}/purple-send-async
%attr(755,root,root) %{_bindir}/purple-url-handler
%endif

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

%if %{with perl}
%files -n libpurple-perl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/purple-2/perl.so
%dir %{_libdir}/purple-2/perl
%{_libdir}/purple-2/perl/*.pm
%dir %{_libdir}/purple-2/perl/auto
%dir %{_libdir}/purple-2/perl/auto/Purple
%{_libdir}/purple-2/perl/auto/Purple/*.ix
%attr(755,root,root) %{_libdir}/purple-2/perl/auto/Purple/*.so
%{_mandir}/man3/Purple.3pm*
%endif

%files -n libpurple-tcl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/purple-2/tcl.so

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

%if %{with perl}
%files perl
%defattr(644,root,root,755)
%dir %{_libdir}/pidgin/perl
%{_libdir}/pidgin/perl/*.pm
%dir %{_libdir}/pidgin/perl/auto
%dir %{_libdir}/pidgin/perl/auto/Pidgin
%attr(755,root,root) %{_libdir}/pidgin/perl/auto/Pidgin/*.so
%{_mandir}/man3/Pidgin.3pm*
%endif

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

%files -n libpurple-protocol-oscar
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/purple-2/libicq.so
%attr(755,root,root) %{_libdir}/purple-2/libaim.so
# shared library for aim/icq protocols
%attr(755,root,root) %{_libdir}/purple-2/liboscar.so.0

%files -n libpurple-protocol-bonjour
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/purple-2/libbonjour.so

%files -n libpurple-protocol-gg
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/purple-2/libgg.so

%files -n libpurple-protocol-groupwise
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/purple-2/libnovell.so

%files -n libpurple-protocol-irc
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/purple-2/libirc.so

%files -n libpurple-protocol-simple
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/purple-2/libsimple.so

%if %{with silc}
%files -n libpurple-protocol-silc
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/purple-2/libsilcpurple.so
%endif

%if %{with meanwhile}
%files -n libpurple-protocol-sametime
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/purple-2/libsametime.so
%endif

%files -n libpurple-protocol-xmpp
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/purple-2/libxmpp.so
%attr(755,root,root) %{_libdir}/purple-2/libjabber.so.0

%files -n libpurple-protocol-zephyr
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/purple-2/libzephyr.so

%if %{with doc}
%files doc
%defattr(644,root,root,755)
%doc doc/html/*.{html,png,css}
%endif
