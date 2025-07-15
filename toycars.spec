# NOTE:
# There is no sound since version 0.3.4, because sound system requires FMOD Ex library to run. Everyone who wants sound can install FMOD Ex on one's own.
#
Summary:	Physics-based 2D racing game
Summary(pl.UTF-8):	Gra wyścigowa 2D oparta na prawach fizyki
Name:		toycars
Version:	0.3.10
Release:	1
License:	BSD
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/toycars/%{name}-%{version}.tar.gz
# Source0-md5:	6b0b7506ee5623081e002c8690c5bc78
Source1:	%{name}.desktop
Patch0:		%{name}-gcc.patch
URL:		http://sourceforge.net/projects/toycars/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	SDL-devel >= 1.2.10
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	autoconf >= 2.61
BuildRequires:	automake
BuildRequires:	fltk-gl-devel
BuildRequires:	perl-base
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Toy Cars is a physics based 2-D racer. The graphics and the interface
use SDL and OpenGL. Toy Cars is partly inspired by Micromachines and
partly by the old Atari ST game called Jupiter's Masterdrive.

%description -l pl.UTF-8
Toy Cars jest grą wyścigową 2D opartą na prawach fizyki. Grafika i
interfejs używają bibliotek SDL i OpenGL. Toy Cars częściowo
zainspirowana została przez grę Micromachines oraz przez starą grę
Jupiter's Masterdrive na Atari ST.

%prep
%setup -q
%patch -P0 -p1
%{__perl} -pi -e 's@Fl/@FL/@' %{name}_track_editor/src/TrackView.cxx

%build
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
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
%doc AUTHORS COPYING ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
