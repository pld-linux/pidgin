# TODO
# - files not updated
# - nas, silc/silcclient?
# - kerberos 4 with zephyr support?
# - external zephyr?
#   http://packages.qa.debian.org/z/zephyr.html
# - obsoletes for gaim
#
%bcond_without	cap		# without Contact Availability Prediction
%bcond_without	dbus		# without dbus (for pidgin-remote and others)
%bcond_without	doc		# do not generate and include documentation
%bcond_without	evolution	# compile without the Pidgin-Evolution plugin
%bcond_without	gtkspell	# without gtkspell support
%bcond_without	meanwhile	# without meanwhile support
%bcond_without	text		# don't build text UI
#
%include	/usr/lib/rpm/macros.perl
Summary:	A client compatible with AOL's 'Instant Messenger'
Summary(de.UTF-8):	Pidgin ist ein Instant Messenger
Summary(ko.UTF-8):	AOL 인스턴트 메신저와 호환되는 클라이언트
Summary(pl.UTF-8):	Klient kompatybilny z AOL Instant Messenger
Summary(pt_BR.UTF-8):	Um cliente para o AOL Instant Messenger (AIM)
Name:		pidgin
Version:	2.0.0
Release:	0.1
License:	GPL
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/pidgin/%{name}-%{version}.tar.bz2
# Source0-md5:	132355d7e236d9c2820a2668621eef43
Patch0:		%{name}-nolibs.patch
Patch1:		%{name}-dbus-dir.patch
Patch2:		%{name}-libgadu.patch
URL:		http://www.pidgin.im/
BuildRequires:	GConf2-devel >= 2.16.0
BuildRequires:	audiofile-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bind-devel
%{?with_dbus:BuildRequires:	dbus-glib-devel >= 0.71}
%{?with_evolution:BuildRequires:	evolution-data-server-devel >= 1.8.1}
BuildRequires:	gettext-autopoint
BuildRequires:	gettext-devel
BuildRequires:	gnutls-devel
BuildRequires:	gstreamer-devel >= 0.10.10
BuildRequires:	gtk+2-devel >= 2:2.10.6
%{?with_gtkspell:BuildRequires:	gtkspell-devel >= 2.0.11}
BuildRequires:	intltool
BuildRequires:	mdns-howl-devel
%{?with_meanwhile:BuildRequires:	meanwhile-devel}
BuildRequires:	libgadu-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.6.26
BuildRequires:	perl-devel
BuildRequires:	pkgconfig
BuildRequires:	python-modules
BuildRequires:	rpm-perlprov
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.177
BuildRequires:	tcl-devel
BuildRequires:	tk-devel
%{?with_text:BuildRequires:	ncurses-ext-devel}
%if %{with cap}
BuildRequires:	sqlite3-devel >= 3.3
%endif
%if %{with doc}
BuildRequires:	doxygen
BuildRequires:	graphviz
%endif
Requires(post,preun):	GConf2 >= 2.16.0
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
# weird: it *should* break after DynaLoader's version change, but it doesn't
#Requires:	perl(DynaLoader) = %(%{__perl} -MDynaLoader -e 'print DynaLoader->VERSION')
Obsoletes:	gaim-ui
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
kliencie AOL IM jak również dodaje własne. Pidgin umożliwia także dostęp
do usług takich jak Yahoo!, ICQ, MSN, Jabber, Napster, Zephyr, IRC
oraz Gadu-Gadu.

%description -l pt_BR.UTF-8
GAIM é um cliente para o AOL Instant Messenger (AIM) que usa o serviço
tik/toc da AOL. É desenvolvido ativamente e suporta muitas das
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
Summary(pl.UTF-8):   Biblioteka klienta Pidgin
Group:		Libraries
Epoch:		1

%description libs
Pidgin client library.

%description libs -l pl.UTF-8
Biblioteka klienta Pidgin.

%package devel
Summary:	Development files for Pidgin client library
Summary(pl.UTF-8):   Pliki programistyczne biblioteki klienta Pidgin
Group:		Development/Libraries
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Requires:	gtk+2-devel >= 2:2.10.6

%description devel
Development files for pidgin.

%description devel -l pl.UTF-8
Pliki programistyczne biblioteki pidgin-remote.

%package perl
Summary:	Pidgin files for Perl scripts
Summary(pl.UTF-8):   Pliki Pidgina dla skryptów w Perlu
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description perl
This package gives you ability to extend Pidgin functionality with Perl
scripts.

%description perl -l pl.UTF-8
Ten pakiet daje możliwość rozszerzania funkcjonalności Pidgina za pomocą
skryptów Perla.

%package tcl
Summary:	Pidgin files for Tcl scripts
Summary(pl.UTF-8):   Pliki Pidgina dla skryptów w Tcl-u
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description tcl
This package gives you ability to extend Pidgin functionality with Tcl
scripts.

%description tcl -l pl.UTF-8
Ten pakiet daje możliwość rozszerzania funkcjonalności Pidgina za pomocą
skryptów w Tcl-u.

%package plugin-evolution
Summary:	Plugin for Ximian Evolution integration
Summary(pl.UTF-8):   Wtyczka do integracji z Evolution
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-evolution
Provides integration with Ximian Evolution.

%description plugin-evolution -l pl.UTF-8
Wtyczka do integracji z Evolution.

%package plugin-remote
Summary:	Pidgin Remote Control
Summary(pl.UTF-8):   Zdalne sterowanie Pidginem
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-remote
This package gives Pidgin the ability to be remote-controlled through
third-party applications or through the pidgin-remote tool.

%description plugin-remote -l pl.UTF-8
Ten pakiet daje możliwość zdalnego sterowania Pidginem przez inne
aplikacje albo narzędzie pidgin-remote.

%package doc
Summary:	Pidgin documentation for developers (HTML format)
Summary(pl.UTF-8):   Dokumentacja Pidgin dla programistów (format HTML)
Group:		Documentation

%description doc
Pidgin documentation for developers (HTML format).

%description doc -l pl.UTF-8
Dokumentacja Pidgin dla programistów (format HTML).

%triggerpostun -- %{name} < 1:1.3.1-1.10
%banner -e %{name} <<EOF
The Ximian Evolution and pidgin-remote plugins have been separated to separate packages.
If you need then please install %{name}-plugin-evolution and %{name}-plugin-remote
EOF

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4macros
%{__autoheader}
%{__autoconf} || :
%{__automake}
%configure \
	--disable-nas \
	--enable-nss=no \
	--with-perl-lib=vendor \
	--%{?with_cap:en}%{!?with_cap:dis}able-cap \
	%{?with_dbus:--enable-dbus --with-dbus-session-dir=/usr/share/dbus-1/services} \
	%{!?with_dbus:--disable-dbus} \
	%{!?with_evolution:--disable-gevolution} \
	%{!?with_gtkspell:--disable-gtkspell} \
	--%{?with_text:en}%{!?with_text:dis}able-consoleui

%{__make}
%{?with_doc:%{__make} docs}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/pidgin/{,private}/*.la
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/{ca@valencia,ca_ES@valencian,my_MM}

%find_lang %{name} --with-gnome
rm -f $RPM_BUILD_ROOT{%{perl_archlib}/perllocal.pod,%{perl_vendorarch}/auto/Pidgin/{,GtkUI}/.packlist}

%if %{with dbus}
rm $RPM_BUILD_ROOT%{_bindir}/purple-client-example
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install pidgin.schemas

%preun
%gconf_schema_uninstall pidgin.schemas

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog{,.API} HACKING NEWS PLUGIN_HOWTO PROGRAMMING_NOTES README* doc/FAQ
%attr(755,root,root) %{_bindir}/pidgin
%dir %{_libdir}/pidgin
%dir %{_libdir}/pidgin/private
%if %{with cap}
%attr(755,root,root) %{_libdir}/pidgin/autoaccept.so
%attr(755,root,root) %{_libdir}/pidgin/autoreply.so
%attr(755,root,root) %{_libdir}/pidgin/buddynote.so
%attr(755,root,root) %{_libdir}/pidgin/cap.so
%endif
%attr(755,root,root) %{_libdir}/pidgin/convcolors.so
#%attr(755,root,root) %{_libdir}/pidgin/docklet.so
%attr(755,root,root) %{_libdir}/pidgin/extplacement.so
%attr(755,root,root) %{_libdir}/pidgin/pidginrc.so
%attr(755,root,root) %{_libdir}/pidgin/gestures.so
%if %{with text}
%attr(755,root,root) %{_bindir}/pidgin-text
%attr(755,root,root) %{_libdir}/pidgin/gntgf.so
%attr(755,root,root) %{_libdir}/pidgin/gnthistory.so
%attr(755,root,root) %{_libdir}/pidgin/gntlastlog.so
%attr(755,root,root) %{_libdir}/pidgin/s.so
%endif
%attr(755,root,root) %{_libdir}/pidgin/history.so
%attr(755,root,root) %{_libdir}/pidgin/iconaway.so
%attr(755,root,root) %{_libdir}/pidgin/idle.so
%attr(755,root,root) %{_libdir}/pidgin/libaim.so
%attr(755,root,root) %{_libdir}/pidgin/libbonjour.so
%attr(755,root,root) %{_libdir}/pidgin/libgg.so
%attr(755,root,root) %{_libdir}/pidgin/libicq.so
%attr(755,root,root) %{_libdir}/pidgin/libirc.so
%attr(755,root,root) %{_libdir}/pidgin/libjabber.so
%attr(755,root,root) %{_libdir}/pidgin/libmsn.so
%attr(755,root,root) %{_libdir}/pidgin/libnovell.so
%attr(755,root,root) %{_libdir}/pidgin/liboscar.so
%attr(755,root,root) %{_libdir}/pidgin/liboscar.so.*
%attr(755,root,root) %{_libdir}/pidgin/libqq.so
%{?with_meanwhile:%attr(755,root,root) %{_libdir}/pidgin/libsametime.so}
%attr(755,root,root) %{_libdir}/pidgin/libsimple.so
%attr(755,root,root) %{_libdir}/pidgin/libyahoo.so
%attr(755,root,root) %{_libdir}/pidgin/libzephyr.so
%attr(755,root,root) %{_libdir}/pidgin/log_reader.so
%attr(755,root,root) %{_libdir}/pidgin/markerline.so
%attr(755,root,root) %{_libdir}/pidgin/newline.so
%attr(755,root,root) %{_libdir}/pidgin/notify.so
%attr(755,root,root) %{_libdir}/pidgin/offlinemsg.so
%attr(755,root,root) %{_libdir}/pidgin/psychic.so
%attr(755,root,root) %{_libdir}/pidgin/relnot.so
%attr(755,root,root) %{_libdir}/pidgin/spellchk.so
%attr(755,root,root) %{_libdir}/pidgin/ssl-gnutls.so
%attr(755,root,root) %{_libdir}/pidgin/ssl-nss.so
%attr(755,root,root) %{_libdir}/pidgin/ssl.so
%attr(755,root,root) %{_libdir}/pidgin/statenotify.so
%attr(755,root,root) %{_libdir}/pidgin/ticker.so
%attr(755,root,root) %{_libdir}/pidgin/timestamp.so
%attr(755,root,root) %{_libdir}/pidgin/timestamp_format.so
%attr(755,root,root) %{_libdir}/pidgin/xmppconsole.so
%if %{with dbus}
%attr(755,root,root) %{_bindir}/pidgin-url-handler
%attr(755,root,root) %{_libdir}/pidgin/musicmessaging.so
%attr(755,root,root) %{_bindir}/pidgin-send
%attr(755,root,root) %{_bindir}/pidgin-send-async
%{_datadir}/dbus-1/services/pidgin.service
%endif
%{_sysconfdir}/gconf/schemas/pidgin.schemas
%{_datadir}/sounds/%{name}
%{_mandir}/man?/*

%{_desktopdir}/pidgin.desktop
%{_pixmapsdir}/*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpidgin.so.*.*.*
%if %{with text}
%attr(755,root,root) %{_libdir}/libgnt.so.*.*.*
%endif
%if %{with dbus}
%attr(755,root,root) %{_libdir}/libpidgin-client.so.*.*.*
%endif

%files devel
%defattr(644,root,root,755)
%if %{with dbus}
%attr(755,root,root) %{_libdir}/libpidgin-client.so
%attr(755,root,root) %{_libdir}/libpidgin.so
%{_libdir}/libpidgin-client.la
%{_libdir}/libpidgin.la
%endif
%{_aclocaldir}/*.m4
%dir %{_includedir}/pidgin
%{_includedir}/pidgin/*.h
%{_pkgconfigdir}/*
%if %{with text}
%attr(755,root,root) %{_libdir}/libgnt.so
%{_libdir}/libgnt.la
%dir %{_includedir}/pidgin/gnt
%dir %{_includedir}/gnt
%{_includedir}/pidgin/gnt/*.h
%{_includedir}/gnt/*.h
%endif

%files perl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/pidgin/private/libpidginperl.so
%attr(755,root,root) %{_libdir}/pidgin/perl.so
%{perl_vendorarch}/*.pm
%dir %{perl_vendorarch}/auto/Pidgin
%{perl_vendorarch}/auto/Pidgin/*.ix
%{perl_vendorarch}/auto/Pidgin/*.bs
%dir %{perl_vendorarch}/auto/Pidgin/GtkUI
%{perl_vendorarch}/auto/Pidgin/GtkUI/*.bs
%dir %{perl_vendorarch}/Pidgin
%{perl_vendorarch}/Pidgin/*.pm
%attr(755,root,root) %{perl_vendorarch}/auto/Pidgin/*.so
%attr(755,root,root) %{perl_vendorarch}/auto/Pidgin/GtkUI/*.so

%files tcl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/pidgin/tcl.so

%if %{with evolution}
%files plugin-evolution
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/pidgin/gevolution.so
%endif

%if %{with dbus}
%files plugin-remote
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pidgin-remote
%endif

%if %{with doc}
%files doc
%defattr(644,root,root,755)
%doc doc/html/*.{html,png,css}
%endif
