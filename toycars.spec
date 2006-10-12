Summary:	Physics-based 2D racing game
Summary(pl):	Gra wy¶cigowa 2D oparta na prawach fizyki
Name:		toycars
Version:	0.3.1
Release:	1
License:	GPL v2
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/toycars/%{name}-%{version}.tar.gz
# Source0-md5:	938a925f6eb209ac85a1d4caace8e5f3
URL:		http://sourceforge.net/projects/toycars/
BuildRequires:	SDL-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	X11-OpenGL-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Toy Cars is a physics based 2-D racer. The graphics and the interface
use SDL and OpenGL. Toy Cars is partly inspired by Micromachines and
partly by the old Atari ST game called Jupiter's Masterdrive.

%description -l pl
Toy Cars jest gr± wy¶cigow± 2D opart± na prawach fizyki. Grafika i
interfejs u¿ywaj± SDL i OpenGL. Toy Cars czê¶ciowo zainspirowana
zosta³a przez grê Micromachines oraz przez star± grê Jupiter's
Masterdrive na Atari ST.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
