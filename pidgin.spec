# This file does not like to be adapterized!
Summary:	A client compatible with AOL's 'Instant Messenger'
Summary(pl):	Klient kompatybilny z AOL Instant Messenger
Summary(pt_BR):	Um cliente para o AOL Instant Messenger (AIM)
Name:		gaim
Version:	0.52
Release:	1
Epoch:		1
License:	GPL
Group:		Applications/Communications
Source0:	http://prdownloads.sourceforge.net/gaim/%{name}-%{version}.tar.bz2
Patch0:		%{name}-gg_logoff.patch
URL:		http://gaim.sourceforge.net/
BuildRequires:	ORBit-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnome-libs-devel >= 1.2.13
BuildRequires:	esound-devel
BuildRequires:	gtk+-devel >= 1.2.5
BuildRequires:	gettext-devel
BuildRequires:	libtool
BuildRequires:	perl-devel
BuildRequires:	gnome-core-devel
BuildRequires:	gdk-pixbuf-devel
Requires:	applnk
Requires:	gaim-ui
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_sysconfdir	/etc/X11/GNOME
%define		_mandir		%{_prefix}/man

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
Gaim pozwala na rozmowy z dowoln± osob± u¿ywaj±c± us³ugi AOL Instant
Messenger (mo¿na siê zarejstrowaæ pod adresem
http://www.aim.aol.com/). Program u¿ywa wersji TOC protoko³u AOL wiêc
Twoja lista kontaktów jest zapisana na serwerze AOL i mo¿e byc
przes³ana gdziekolwiek. Gaim zawiera wiele udogodnieñ dostêpnych w
kliencie AOL IM jak równie¿ dodaje w³asne. Gaim umo¿liwia tak¿e dostêp
do us³ug takich jak Yahoo!, ICQ, MSN, Jabber, Napster, Zephyr, IRC
oraz Gadu-Gadu.

%description -l pt_BR
GAIM é um cliente para o AOL Instant Messenger (AIM) que usa o serviço
tik/toc da AOL. É desenvolvido ativamente e suporta muitas das
características do cliente da AOL, tendo uma interface similiar.
Também oferece suporte a outros protocolos, como: ICQ, IRC, Yahoo!,
MSN, Jabber e Napster.

%package ui-gtk
Summary:	gtk+ user interface for gaim
Summary(pl):	Interfejs u¿ytkownika gaim korzystaj±cy z gtk+
Group:		Applications/Communications
Provides:	gaim-ui

%description ui-gtk
gtk+ user interface for gaim.

%description ui-gtk -l pl
Interfejs u¿ytkownika gaim korzystaj±cy z gtk+.

%package ui-gnome
Summary:	GNOME user interface for gaim (applet)
Summary(pl):	Interfejs u¿ytkownika gaim korzystaj±cy z GNOME (applet)
Group:		Applications/Communications
Provides:	gaim-ui

%description ui-gnome
GNOME user interface for gaim (applet).

%description ui-gnome -l pl
Interfejs u¿ytkownika gaim korzystaj±cy z GNOME (applet).

%prep
%setup -q
%patch0 -p1

%build
rm  -f missing
libtoolize --copy --force
gettextize --copy --force
aclocal -I m4
autoheader
autoconf
automake -a -c
%configure \
	--disable-panel \
	--enable-esd \
	--disable-nas \
	--disable-artsc \
	--with-gnome
%{__make}
mv plugins/iconaway{,_standalone}.so
mv src/gaim{,_standalone}
%{__make} clean

%configure \
	--enable-panel \
	--enable-esd \
	--disable-nas \
	--disable-artsc \
	--with-gnome
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

# NOTE: make ignores gaimdesktopdir set below.
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	gaimdesktopdir=%{_applnkdir}/Network/Communications \
	distribdesktopdir=%{_applnkdir}/Network/Communications

mv $RPM_BUILD_ROOT{%{_datadir}/gnome/apps/Internet/gaim.desktop,%{_applnkdir}/Network/Communications}

mv $RPM_BUILD_ROOT%{_libdir}/gaim/iconaway{,_applet}.so
install plugins/iconaway_standalone.so $RPM_BUILD_ROOT%{_libdir}/gaim/iconaway.so
install src/gaim_standalone $RPM_BUILD_ROOT%{_bindir}/gaim

gzip -9nf AUTHORS ChangeLog NEWS README* TODO HACKING \
	doc/{CREDITS,FAQ}

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc {*,doc/*}.gz
%dir %{_libdir}/gaim
%attr(755,root,root) %{_libdir}/gaim/[^i]*.so
%{_pixmapsdir}/*
%{_mandir}/man?/*

%files ui-gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gaim
%attr(755,root,root) %{_libdir}/gaim/iconaway.so
%{_applnkdir}/Network/Communications/gaim.desktop

%files ui-gnome
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gaim_applet
%attr(755,root,root) %{_libdir}/gaim/iconaway_applet.so
%{_applnkdir}/Network/Communications/gaim_applet.desktop
%{_sysconfdir}/CORBA/servers/*
