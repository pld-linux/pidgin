Summary:	A client compatible with AOL's 'Instant Messenger'
Summary(es):	Klient kompatybilny z programem AOLa 'Instant Messenger'
Name:		gaim
Version:	0.11.0pre10
Release:	1
Epoch:		0
License:	GPL
Group:		Applications/Communications
Group(de):	Applikationen/Kommunikation
Group(pl):	Aplikacje/Komunikacja
Source0:	http://prdownloads.sourceforge.net/gaim/%{name}-%{version}.tar.bz2
URL:		http://gaim.sourceforge.net/
BuildRequires:	gnome-libs-devel >= 1.2.13
BuildRequires:	gtk+-devel >= 1.2.5
BuildRequires:	ORBit-devel
BuildRequires:	gettext-devel
BuildRequires:	esound-devel
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	libtool
Prereq:		/sbin/ldconfig
Requires:	applnk
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
gaim to connect to other chat services such as Yahoo!, ICQ, and IRC.

%description -l pl
Gaim pozwala na rozmowy z dowoln± osob± u¿ywaj±c± us³ugi AOL Instant
Messenger (mo¿na siê zarejstrowaæ pod adresem
http://www.aim.aol.com/). Program u¿ywa wersji TOC protoko³u AOL wiêc
Twoja lista kontaktów jest zapisana na serwerze AOL i mo¿e byc
przes³ana gdziekolwiek. Gaim zawiera wiele udogodnieñ dostêpnych w
kliencie AOL IM jak równie¿ dodaje w³asne. Gaim umo¿liwia tak¿e dostêp
do us³ug takich jak Yahoo!, ICQ oraz IRC.

%prep
%setup -q

%build
rm missing
libtoolize --copy --force
gettextize --copy --force
aclocal -I m4
autoheader
autoconf
automake -a -c
%configure \
	--enable-gnome \
	--enable-panel \
	--disable-perl

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	gaimdesktopdir=%{_applnkdir}/Network/Communications
	
gzip -9nf AUTHORS ChangeLog NEWS README* STATUS TODO HACKING \
	doc/{CREDITS,FAQ,PROTOCOL}

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc {*,doc/*}.gz
%{_sysconfdir}/CORBA/servers/*
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/gaim
%attr(755,root,root) %{_libdir}/gaim/*
%{_applnkdir}/Network/Communications/*.desktop
%{_pixmapsdir}/*
%{_mandir}/man?/*
