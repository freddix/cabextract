Summary:	A program to extract Microsoft Cabinet files
Name:		cabextract
Version:	1.4
Release:	2
License:	GPL
Group:		Applications/Archiving
Source0:	http://www.cabextract.org.uk/%{name}-%{version}.tar.gz
# Source0-md5:	79f41f568cf1a3ac105e0687e8bfb7c0
URL:		http://www.cabextract.org.uk/cabextract-1.2.tar.gz
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libmspack-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cabinet (.CAB) files are a form of archive, which Microsoft use to
distribute their software, and things like Windows Font Packs. The
cabextract program simply unpacks such files.

%prep
%setup -q
rm -rf mspack

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-external-libmspack
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -D doc/ja/cabextract.1 $RPM_BUILD_ROOT%{_mandir}/ja/man1/cabextract.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%lang(ja) %{_mandir}/ja/man1/*

