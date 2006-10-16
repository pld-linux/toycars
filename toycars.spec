Summary:	Physics-based 2D racing game
Summary(pl):	Gra wy�cigowa 2D oparta na prawach fizyki
Name:		toycars
Version:	0.3.2
Release:	2
License:	GPL v2
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/toycars/%{name}-%{version}.tar.gz
# Source0-md5:	70821d80bfc103feeeb98afb409b73aa
Source1:	%{name}.desktop
URL:		http://sourceforge.net/projects/toycars/
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Toy Cars is a physics based 2-D racer. The graphics and the interface
use SDL and OpenGL. Toy Cars is partly inspired by Micromachines and
partly by the old Atari ST game called Jupiter's Masterdrive.

%description -l pl
Toy Cars jest gr� wy�cigow� 2D opart� na prawach fizyki. Grafika i
interfejs u�ywaj� bibliotek SDL i OpenGL. Toy Cars cz�ciowo
zainspirowana zosta�a przez gr� Micromachines oraz przez star� gr�
Jupiter's Masterdrive na Atari ST.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install data/images/title.png $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
