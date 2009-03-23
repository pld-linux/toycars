# NOTE:
# There is no sound since version 0.3.4, because sound system requires FMOD Ex library to run. Everyone who wants sound can install FMOD Ex on one's own.
#
# Conditional build
%bcond_without	editors		# don't build track and vehicle editors
#
%define 	track_editor_ver	0.1.2
%define		vehicle_editor_ver	0.1.0
Summary:	Physics-based 2D racing game
Summary(pl.UTF-8):	Gra wyścigowa 2D oparta na prawach fizyki
Name:		toycars
Version:	0.3.9
Release:	1
License:	BSD
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/toycars/%{name}-%{version}.tar.gz
# Source0-md5:	6fd6baf4389007ca59fddc33c6b3e631
Source1:	http://dl.sourceforge.net/toycars/%{name}_track_editor-%{track_editor_ver}.tar.gz
# Source1-md5:	ec55e35b88cfbbba7e24f799dfe5691d
Source2:	http://dl.sourceforge.net/toycars/%{name}_vehicle_editor-%{vehicle_editor_ver}.tar.gz
# Source2-md5:	f443638a8d535b99b47316c6edca3efd
Source3:	%{name}.desktop
Patch0:		%{name}-case_brackets.patch
URL:		http://sourceforge.net/projects/toycars/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	SDL-devel >= 1.2.10
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	autoconf >= 2.61
BuildRequires:	automake
%{?with_editors:BuildRequires:	fltk-gl-devel}
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
%setup -q -a 1 -a 2
%if %{with editors}
%patch0 -p1
%endif

%if %{with editors}
# copy the same file instead of patching it again
cp src/Startline.cpp %{name}_track_editor-%{track_editor_ver}/src
%{__perl} -pi -e 's@Fl/@FL/@' %{name}_track_editor-%{track_editor_ver}/src/TrackView.cxx
%endif

%build
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%if %{with editors}
cd %{name}_track_editor-%{track_editor_ver}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

cd ..
cd %{name}_vehicle_editor-%{vehicle_editor_ver}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE3} $RPM_BUILD_ROOT%{_desktopdir}
install data/images/title.png $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png

%if %{with editors}
	install %{name}_track_editor-%{track_editor_ver}/src/%{name}_track_editor $RPM_BUILD_ROOT%{_bindir}
	install %{name}_vehicle_editor-%{vehicle_editor_ver}/src/%{name}_vehicle_editor $RPM_BUILD_ROOT%{_bindir}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
