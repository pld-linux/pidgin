# TODO
# - cleanup files; move libs to proper packages
# - subpackages for
#  - different protocols (like koptete)
#  - huge deps (mono...)
# - nas, silc/silcclient?
# - kerberos 4 with zephyr support?
# - external zephyr?
#   http://packages.qa.debian.org/z/zephyr.html
# - move mono related files to -libs?
# - add NetworkManager support
#
%bcond_without	cap		# without Contact Availability Prediction
%bcond_without	dbus		# without D-BUS (for pidgin-remote and others)
%bcond_without	doc		# do not generate and include documentation
%bcond_with	dotnet		# build with mono support
%bcond_without	evolution	# compile without the Pidgin-Evolution plugin
%bcond_without	gtkspell	# without gtkspell support
%bcond_without	meanwhile	# without meanwhile support
%bcond_without	sasl		# disable SASL support
%bcond_without	text		# don't build text UI
%bcond_without 	silc		# Build without SILC libraries
%bcond_with 	nm			# NetworkManager support (requires D-Bus)

%if %{without dbus}
%undefine	with_nm
%endif

# plain i386 is not supported; mono uses cmpxchg/xadd which require i486
%ifarch i386
%undefine	with_dotnet
%endif
#
%include	/usr/lib/rpm/macros.perl
Summary:	A client compatible with AOL's 'Instant Messenger'
Summary(de.UTF-8):	Pidgin ist ein Instant Messenger
Summary(ko.UTF-8):	AOL 인스턴트 메신저와 호환되는 클라이언트
Summary(pl.UTF-8):	Klient kompatybilny z AOL Instant Messenger
Summary(pt_BR.UTF-8):	Um cliente para o AOL Instant Messenger (AIM)
Name:		pidgin
Version:	2.5.1
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/pidgin/%{name}-%{version}.tar.bz2
# Source0-md5:	f76c269c02fafee9b45cc2a50b43b1f3
Patch0:		%{name}-nolibs.patch
Patch1:		%{name}-dbus-dir.patch
Patch2:		%{name}-libgadu.patch
Patch3:		%{name}-autoconf.patch
URL:		http://www.pidgin.im/
BuildRequires:	GConf2-devel >= 2.14.0
%{?with_nm:BuildRequires:	NetworkManager-devel}
BuildRequires:	audiofile-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	avahi-devel
BuildRequires:	nss-devel
BuildRequires:	bind-devel
%{?with_sasl:BuildRequires:	cyrus-sasl-devel}
%{?with_dbus:BuildRequires:	dbus-glib-devel >= 0.62}
%{?with_evolution:BuildRequires:	evolution-data-server-devel >= 1.6.3}
BuildRequires:	gettext-autopoint
BuildRequires:	gettext-devel
BuildRequires:	gnutls-devel
BuildRequires:	gstreamer-devel >= 0.10.10
BuildRequires:	gtk+2-devel >= 2:2.8.20
%{?with_gtkspell:BuildRequires:	gtkspell-devel >= 2.0.11}
BuildRequires:	intltool
BuildRequires:	libgadu-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.6.26
%{?with_meanwhile:BuildRequires:	meanwhile-devel}
%{?with_dotnet:BuildRequires:	mono-csharp}
%{?with_dotnet:BuildRequires:	mono-devel}
%{?with_text:BuildRequires:	ncurses-ext-devel}
BuildRequires:	perl-devel
BuildRequires:	pkgconfig
BuildRequires:	python-modules
BuildRequires:	rpm-perlprov
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.177
%{?with_silc:BuildRequires:	silc-toolkit-devel >= 1.1}
BuildRequires:	startup-notification-devel
BuildRequires:	tcl-devel
BuildRequires:	tk-devel
%if %{with cap}
BuildRequires:	sqlite3-devel >= 3.3
%endif
BuildRequires:	XFree86-devel
%if %{with doc}
BuildRequires:	doxygen
BuildRequires:	graphviz
%endif
%{?with_sasl:Requires(hint):    cyrus-sasl-digest-md5}
Requires(post,preun):	GConf2 >= 2.14.0
Requires:	%{name}-libs = %{version}-%{release}
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

%package libs
Summary:	Pidgin client library
Summary(pl.UTF-8):	Biblioteka klienta Pidgina
Group:		Libraries

%description libs
Pidgin client library.

%description libs -l pl.UTF-8
Biblioteka klienta Pidgina.

%package devel
Summary:	Development files for Pidgin client library
Summary(pl.UTF-8):	Pliki programistyczne biblioteki klienta Pidgina
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	gtk+2-devel >= 2:2.8.20
Obsoletes:	gaim-devel

%description devel
Development files for Pidgin.

%description devel -l pl.UTF-8
Pliki programistyczne biblioteki Pidgina.

%package perl
Summary:	Pidgin files for Perl scripts
Summary(pl.UTF-8):	Pliki Pidgina dla skryptów w Perlu
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	gaim-perl

%description perl
This package gives you ability to extend Pidgin functionality with
Perl scripts.

%description perl -l pl.UTF-8
Ten pakiet daje możliwość rozszerzania funkcjonalności Pidgina za
pomocą skryptów Perla.

%package tcl
Summary:	Pidgin files for Tcl scripts
Summary(pl.UTF-8):	Pliki Pidgina dla skryptów w Tcl-u
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	gaim-tcl

%description tcl
This package gives you ability to extend Pidgin functionality with Tcl
scripts.

%description tcl -l pl.UTF-8
Ten pakiet daje możliwość rozszerzania funkcjonalności Pidgina za
pomocą skryptów w Tcl-u.

%package plugin-evolution
Summary:	Plugin for Ximian Evolution integration
Summary(pl.UTF-8):	Wtyczka do integracji z Evolution
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	gaim-plugin-evolution

%description plugin-evolution
Provides integration with Ximian Evolution.

%description plugin-evolution -l pl.UTF-8
Wtyczka do integracji z Evolution.

%package plugin-remote
Summary:	Pidgin Remote Control
Summary(pl.UTF-8):	Zdalne sterowanie Pidginem
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	gaim-plugin-remote

%description plugin-remote
This package gives Pidgin the ability to be remote-controlled through
third-party applications or through the pidgin-remote tool.

%description plugin-remote -l pl.UTF-8
Ten pakiet daje możliwość zdalnego sterowania Pidginem przez inne
aplikacje albo narzędzie pidgin-remote.

%package doc
Summary:	Pidgin documentation for developers (HTML format)
Summary(pl.UTF-8):	Dokumentacja Pidgina dla programistów (format HTML)
Group:		Documentation
Obsoletes:	gaim-doc

%description doc
Pidgin documentation for developers (HTML format).

%description doc -l pl.UTF-8
Dokumentacja Pidgina dla programistów (format HTML).

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
#%patch3 -p1

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
	--disable-gnutls \
	--disable-nas \
	--enable-nss \
	%{?with_doc:--enable-dot --enable-devhelp} \
	--with-perl-lib=vendor \
	%{!?with_silc:--with-silc-includes=not_existent_directory} \
	--%{?with_cap:en}%{!?with_cap:dis}able-cap \
	%{?with_sasl:--enable-cyrus-sasl} \
	%{?with_dbus:--enable-dbus --with-dbus-session-dir=%{_datadir}/dbus-1/services} \
	%{!?with_dbus:--disable-dbus} \
	--%{?with_nm:en}%{!?with_nm:dis}able-nm \
	--%{?with_evolution:en}%{!?with_evolution:dis}able-gevolution \
	%{!?with_gtkspell:--disable-gtkspell} \
	%{?with_dotnet:--enable-mono} \
	--%{?with_text:en}%{!?with_text:dis}able-consoleui

%{__make}
%{?with_doc:%{__make} docs}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/finch/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/gnt/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/pidgin/{,private}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/purple-2/*.la
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/{ca@valencia,ca_ES@valencian,my_MM,ps}

%find_lang %{name} --with-gnome
rm -f $RPM_BUILD_ROOT{%{perl_archlib}/perllocal.pod,%{perl_vendorarch}/auto/Pidgin/{,GtkUI}/.packlist}
rm -rf $RPM_BUILD_ROOT%{_datadir}/purple/ca-certs

%if %{with dbus}
rm $RPM_BUILD_ROOT%{_bindir}/purple-client-example
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install purple.schemas

%preun
%gconf_schema_uninstall purple.schemas

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog{,.API} HACKING NEWS PLUGIN_HOWTO README*
%attr(755,root,root) %{_bindir}/pidgin
%dir %{_libdir}/pidgin
%attr(755,root,root) %{_libdir}/purple-2/autoaccept.so
%attr(755,root,root) %{_libdir}/purple-2/buddynote.so
%if %{with cap}
%attr(755,root,root) %{_libdir}/pidgin/cap.so
%endif
%if %{with dotnet}
%attr(755,root,root) %{_libdir}/purple-2/*.dll
%attr(755,root,root) %{_libdir}/purple-2/mono.so
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
%attr(755,root,root) %{_libdir}/pidgin/xmppconsole.so
%attr(755,root,root) %{_libdir}/pidgin/sendbutton.so
%if %{with text}
%attr(755,root,root) %{_bindir}/finch
%dir %{_libdir}/finch
%attr(755,root,root) %{_libdir}/finch/gntclipboard.so
%attr(755,root,root) %{_libdir}/finch/gntgf.so
%attr(755,root,root) %{_libdir}/finch/gnthistory.so
%attr(755,root,root) %{_libdir}/finch/gntlastlog.so
%attr(755,root,root) %{_libdir}/finch/grouping.so
%dir %{_libdir}/gnt
%attr(755,root,root) %{_libdir}/gnt/*.so
%endif
%dir %{_libdir}/purple-2
%{?with_dbus:%attr(755,root,root) %{_libdir}/purple-2/dbus-example.so}
%attr(755,root,root) %{_libdir}/purple-2/idle.so
%attr(755,root,root) %{_libdir}/purple-2/joinpart.so
%attr(755,root,root) %{_libdir}/purple-2/libaim.so
%attr(755,root,root) %{_libdir}/purple-2/libbonjour.so
%attr(755,root,root) %{_libdir}/purple-2/libgg.so
%attr(755,root,root) %{_libdir}/purple-2/libicq.so
%attr(755,root,root) %{_libdir}/purple-2/libirc.so
%attr(755,root,root) %{_libdir}/purple-2/libjabber.so.*
%attr(755,root,root) %{_libdir}/purple-2/libmsn.so
%attr(755,root,root) %{_libdir}/purple-2/libmyspace.so
%attr(755,root,root) %{_libdir}/purple-2/libnovell.so
%attr(755,root,root) %{_libdir}/purple-2/liboscar.so.*
%attr(755,root,root) %{_libdir}/purple-2/libqq.so
%attr(755,root,root) %{_libdir}/purple-2/libjabber.so
%attr(755,root,root) %{_libdir}/purple-2/liboscar.so

%{?with_meanwhile:%attr(755,root,root) %{_libdir}/purple-2/libsametime.so}
%{?with_silc:%attr(755,root,root) %{_libdir}/purple-2/libsilcpurple.so}
%attr(755,root,root) %{_libdir}/purple-2/libsimple.so
%attr(755,root,root) %{_libdir}/purple-2/libxmpp.so
%attr(755,root,root) %{_libdir}/purple-2/libyahoo.so
%attr(755,root,root) %{_libdir}/purple-2/libzephyr.so
%attr(755,root,root) %{_libdir}/purple-2/log_reader.so
%attr(755,root,root) %{_libdir}/purple-2/newline.so
%attr(755,root,root) %{_libdir}/purple-2/offlinemsg.so
%attr(755,root,root) %{_libdir}/purple-2/psychic.so
%attr(755,root,root) %{_libdir}/purple-2/ssl-gnutls.so
%attr(755,root,root) %{_libdir}/purple-2/ssl-nss.so
%attr(755,root,root) %{_libdir}/purple-2/ssl.so
%attr(755,root,root) %{_libdir}/purple-2/statenotify.so
%if %{with dbus}
%attr(755,root,root) %{_bindir}/purple-url-handler
%attr(755,root,root) %{_bindir}/purple-send
%attr(755,root,root) %{_bindir}/purple-send-async
%attr(755,root,root) %{_libdir}/pidgin/musicmessaging.so
%endif
%{_sysconfdir}/gconf/schemas/purple.schemas
%{_datadir}/sounds/purple
%{_mandir}/man?/*

%{_desktopdir}/pidgin.desktop
%{_pixmapsdir}/*
%{_iconsdir}/hicolor/*/apps/pidgin.*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpurple.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpurple.so.0
%if %{with dbus}
%attr(755,root,root) %{_libdir}/libpurple-client.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpurple-client.so.0
%endif
%if %{with text}
%attr(755,root,root) %{_libdir}/libgnt.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgnt.so.0
%endif

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpurple.so
%{_libdir}/libpurple.la
%dir %{_includedir}/libpurple
%{_includedir}/libpurple/*.h
%dir %{_includedir}/pidgin
%{_includedir}/pidgin/*.h
%{_pkgconfigdir}/pidgin.pc
%{_pkgconfigdir}/purple.pc
%{_aclocaldir}/purple.m4
%if %{with dbus}
%attr(755,root,root) %{_libdir}/libpurple-client.so
%{_libdir}/libpurple-client.la
%endif
%if %{with text}
%attr(755,root,root) %{_libdir}/libgnt.so
%{_libdir}/libgnt.la
%dir %{_includedir}/finch
%{_includedir}/finch/*.h
%dir %{_includedir}/gnt
%{_includedir}/gnt/*.h
%{_pkgconfigdir}/finch.pc
%{_pkgconfigdir}/gnt.pc
%endif

%files perl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/purple-2/perl.so
%{perl_vendorarch}/*.pm
%dir %{perl_vendorarch}/auto/Pidgin
%dir %{perl_vendorarch}/auto/Purple
%{perl_vendorarch}/auto/Pidgin/*.bs
%{perl_vendorarch}/auto/Purple/*.ix
%{perl_vendorarch}/auto/Purple/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Purple/Purple.so
%{perl_vendorarch}/auto/Purple/.packlist
%attr(755,root,root) %{perl_vendorarch}/auto/Pidgin/*.so

%files tcl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/purple-2/tcl.so

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

%if %{with doc}
%files doc
%defattr(644,root,root,755)
%doc doc/html/*.{html,png,css}
%endif
