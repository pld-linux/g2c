Summary:	g2c - Glade to C Translator
Summary(pl):	g2c - translator z Glade do C
Name:		g2c
Version:	0.4
Release:	1
License:	GPL v2
Group:		Development/Tools
Source0:	http://telia.dl.sourceforge.net/sourceforge/g2c/%{name}-%{version}.tar.gz
Patch0:		%{name}-dirty_xml.patch
URL:		http://www.sourceforge.net/projects/g2c/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bonobo-devel >= 0.1.0
BuildRequires:	gtk+-devel
BuildRequires:	libxml-devel
Requires:	ctags
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The g2c program converts a Glade XML tree to C source code.

Glade provides C source output to a set of monolithic files. All
widgets are placed into one file, which can be difficult to manage on
large projects. This project aims to provide an alternative source
code output mechanism.

%description -l pl
Program g2c konwertuje drzewko Glade XML do kodu ¼ród³owego C.

Glade daje na wyj¶ciu ¼ród³o w C do zestawu monolitycznych plików.
Wszystkie widgety sa umieszczone w jednym pliku, który mo¿e byæ trudny
do zarz±dzania w du¿ych projektach. Celem tego projektu jest
dostarczenie alternetywnego mechanizmu dla wyj¶cia kodu ¼ród³owego.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
%{__aclocal} -I macros
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
