Summary:	Sphere undergoing the Thurston eversion
Summary(pl.UTF-8):	Sfera podlegająca wynicowaniu Thurstona
Name:		sphereEversion
Version:	0.3.6
Release:	1
License:	unknown
Group:		X11/Applications/Graphics
Source0:	http://downloads.sourceforge.net/sf-xpaint/%{name}-%{version}.tar.bz2
# Source0-md5:	f58b1235d2828d7f53244d48716876a7
URL:		http://www.dgp.toronto.edu/~mjmcguff/eversion/
BuildRequires:	OpenGL-devel
BuildRequires:	libstdc++-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program displays a sphere undergoing the Thurston eversion.

%description -l pl.UTF-8
Ten program wyświetla sferę podlegająca wynicowaniu Thurstona.

%prep
%setup -q

%build
%{__make} \
	CCXX="%{__cxx}" \
	CFLAGS="%{rpmcxxflags} %{rpmcppflags}" \
	LIBS="%{rpmldflags} -lGL -lX11 -lm"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir},%{_pixmapsdir}}

install sphereEversion $RPM_BUILD_ROOT%{_bindir}
cp -p sphere_eversion.desktop $RPM_BUILD_ROOT%{_desktopdir}
cp -p sphere_eversion.png $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc readme.txt
%attr(755,root,root) %{_bindir}/sphereEversion
%{_desktopdir}/sphere_eversion.desktop
%{_pixmapsdir}/sphere_eversion.png
