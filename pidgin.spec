# This file does not like to be adapterized!
Summary:	A client compatible with AOL's 'Instant Messenger'
Summary(ko):	AOL ÀÎ½ºÅÏÆ® ¸Þ½ÅÀú¿Í È£È¯µÇ´Â Å¬¶óÀÌ¾ðÆ®
Summary(pl):	Klient kompatybilny z AOL Instant Messenger
Summary(pt_BR):	Um cliente para o AOL Instant Messenger (AIM)
Name:		gaim
Version:	0.65
Release:	0.1
Epoch:		1
License:	GPL
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	31c2fe5ccfb200d9be317a90fd2a4603
Patch0:		%{name}-nolibs.patch
# Patch0:		%{name}-gg_logoff.patch
# Patch1:		%{name}-am_ac.patch
# Patch2:		%{name}-tw.patch
URL:		http://gaim.sourceforge.net/
BuildRequires:	audiofile-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2.1.0
BuildRequires:	libao-devel
BuildRequires:	libtool
BuildRequires:	perl-devel
Requires:	applnk
Requires:	gaim-ui = %{version}
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
Provides:	gaim-ui = %{version}-%{release}

%description ui-gtk
gtk+ user interface for gaim.

%description ui-gtk -l pl
Interfejs u¿ytkownika gaim korzystaj±cy z gtk+.

# %package ui-gnome
# Summary:	GNOME user interface for gaim (applet)
# Summary(pl):	Interfejs u¿ytkownika gaim korzystaj±cy z GNOME (applet)
# Group:		Applications/Communications
# Provides:	gaim-ui = %{version}-%{release}

# %description ui-gnome
# GNOME user interface for gaim (applet).

# %description ui-gnome -l pl
# Interfejs u¿ytkownika gaim korzystaj±cy z GNOME (applet).

%package devel
Summary:	Development files for gaim-remote library
Summary(pl):	Pliki programistyczne biblioteki gaim-remote
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Development files for gaim-remote library.

%description devel -l pl
Pliki programistyczne biblioteki gaim-remote.

%prep
%setup -q
%patch0 -p1

%build
rm -f configure.in
%{__libtoolize}
%{__gettextize}
%{__aclocal} 
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--disable-nas

%{__make}

# no GNOME version of UI now
#mv plugins/.libs/iconaway{,_standalone}.so
#mv src/gaim{,_standalone}
#%{__make} clean

#%%configure \
#	--enable-panel \
#	--enable-esd \
#	--disable-nas \
#	--disable-artsc \
#	--enable-gnome
#
#%{__make}
	
%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

#mv $RPM_BUILD_ROOT%{_libdir}/gaim/iconaway{,_applet}.so
#install plugins/.libs/iconaway.so $RPM_BUILD_ROOT%{_libdir}/gaim/iconaway.so
#install src/gaim_standalone $RPM_BUILD_ROOT%{_bindir}/gaim

rm -f $RPM_BUILD_ROOT%{_libdir}/gaim/*.la

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README* TODO HACKING doc/{CREDITS,FAQ}
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

# %files ui-gnome
# %defattr(644,root,root,755)
# %attr(755,root,root) %{_bindir}/gaim_applet
# %attr(755,root,root) %{_libdir}/gaim/iconaway_applet.so
# %{_applnkdir}/Network/Communications/gaim_applet.desktop
# %{_sysconfdir}/CORBA/servers/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgaim-remote.so
%{_libdir}/libgaim-remote.la
%dir %{_includedir}/gaim-remote
%{_includedir}/gaim-remote/remote-socket.h
%{_includedir}/gaim-remote/remote.h
