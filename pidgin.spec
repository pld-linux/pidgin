# This file does not like to be adapterized!
Summary:	A client compatible with AOL's 'Instant Messenger'
Summary(ko):	AOL �ν���Ʈ �޽����� ȣȯ�Ǵ� Ŭ���̾�Ʈ
Summary(pl):	Klient kompatybilny z AOL Instant Messenger
Summary(pt_BR):	Um cliente para o AOL Instant Messenger (AIM)
Name:		gaim
Version:	0.62
Release:	0.1
Epoch:		1
License:	GPL
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/gaim/%{name}-%{version}.tar.bz2
# Source0-md5:	7740c762271ffb623e93d5c1b382a72b
# Patch0:		%{name}-gg_logoff.patch
# Patch1:		%{name}-am_ac.patch
# Patch2:		%{name}-tw.patch
URL:		http://gaim.sourceforge.net/
BuildRequires:	ORBit-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnome-libs-devel >= 1.2.13
BuildRequires:	esound-devel
BuildRequires:	gtk+2-devel >= 2.1.0
BuildRequires:	gettext-devel
BuildRequires:	libtool
BuildRequires:	perl-devel
BuildRequires:	gnome-core-devel
BuildRequires:	gdk-pixbuf-devel
Requires:	applnk
Requires:	gaim-ui = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/X11/GNOME
%define		_prefix	/usr/X11R6

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
Gaim pozwala na rozmowy z dowoln� osob� u�ywaj�c� us�ugi AOL Instant
Messenger (mo�na si� zarejstrowa� pod adresem
http://www.aim.aol.com/). Program u�ywa wersji TOC protoko�u AOL wi�c
Twoja lista kontakt�w jest zapisana na serwerze AOL i mo�e byc
przes�ana gdziekolwiek. Gaim zawiera wiele udogodnie� dost�pnych w
kliencie AOL IM jak r�wnie� dodaje w�asne. Gaim umo�liwia tak�e dost�p
do us�ug takich jak Yahoo!, ICQ, MSN, Jabber, Napster, Zephyr, IRC
oraz Gadu-Gadu.

%description -l pt_BR
GAIM � um cliente para o AOL Instant Messenger (AIM) que usa o servi�o
tik/toc da AOL. � desenvolvido ativamente e suporta muitas das
caracter�sticas do cliente da AOL, tendo uma interface similiar.
Tamb�m oferece suporte a outros protocolos, como: ICQ, IRC, Yahoo!,
MSN, Jabber e Napster.

%package ui-gtk
Summary:	gtk+ user interface for gaim
Summary(pl):	Interfejs u�ytkownika gaim korzystaj�cy z gtk+
Group:		Applications/Communications
Provides:	gaim-ui = %{version}-%{release}

%description ui-gtk
gtk+ user interface for gaim.

%description ui-gtk -l pl
Interfejs u�ytkownika gaim korzystaj�cy z gtk+.

# %package ui-gnome
# Summary:	GNOME user interface for gaim (applet)
# Summary(pl):	Interfejs u�ytkownika gaim korzystaj�cy z GNOME (applet)
# Group:		Applications/Communications
# Provides:	gaim-ui = %{version}-%{release}

# %description ui-gnome
# GNOME user interface for gaim (applet).

# %description ui-gnome -l pl
# Interfejs u�ytkownika gaim korzystaj�cy z GNOME (applet).

%prep
%setup -qn %{name}-%{version}
# %patch0 -p1
# %patch1 -p1
# %patch2 -p1

%build
rm -f missing
%{__libtoolize}
%{__gettextize}
%{__aclocal} 
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--disable-panel \
	--enable-esd \
	--disable-nas \
	--disable-artsc \
	--disable-gnome \
	--with-gtk-prefix=/usr/X11R6 \
	--with-gdk-pixbuf-config=/usr/X11R6/bin/gdk-pixbuf-config 
%{__make} 
mv plugins/.libs/iconaway{,_standalone}.so
mv src/gaim{,_standalone}
%{__make} clean

%configure \
	--enable-panel \
	--enable-esd \
	--disable-nas \
	--disable-artsc \
	--enable-gnome \
	--with-gtk-prefix=/usr/X11R6 \
	--with-gdk-pixbuf-config=/usr/X11R6/bin/gdk-pixbuf-config 
%{__make}
	
%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Network/Communications

# NOTE: make ignores gaimdesktopdir set below.
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	gaimdesktopdir=%{_applnkdir}/Network/Communications \
	distribdesktopdir=%{_applnkdir}/Network/Communications

mv $RPM_BUILD_ROOT{%{_datadir}/applications/gaim.desktop,%{_applnkdir}/Network/Communications}

mv $RPM_BUILD_ROOT%{_libdir}/gaim/iconaway{,_applet}.so
install plugins/.libs/iconaway.so $RPM_BUILD_ROOT%{_libdir}/gaim/iconaway.so
install src/gaim_standalone $RPM_BUILD_ROOT%{_bindir}/gaim

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README* TODO HACKING doc/{CREDITS,FAQ}
%dir %{_libdir}/gaim
%attr(755,root,root) %{_libdir}/gaim/[^i]*.so
%{_pixmapsdir}/*
%{_mandir}/man?/*
%{_datadir}/sounds/%{name}/*.wav

%files ui-gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gaim
%attr(755,root,root) %{_libdir}/gaim/iconaway.so
%{_applnkdir}/Network/Communications/gaim.desktop

# %files ui-gnome
# %defattr(644,root,root,755)
# %attr(755,root,root) %{_bindir}/gaim_applet
# %attr(755,root,root) %{_libdir}/gaim/iconaway_applet.so
# %{_applnkdir}/Network/Communications/gaim_applet.desktop
# %{_sysconfdir}/CORBA/servers/*
