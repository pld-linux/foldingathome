Summary:	Folding@home client
Summary(pl):	Klient Folding@home
Name:		foldingathome
Version:	4.00
Release:	1
License:	Freeware
Group:		Applications/Science
Source0:	http://www.stanford.edu/group/pandegroup/release/FAH4Console-Linux.exe
# Source0-md5:	d8ca3f78a3fff62059b780891d4c1e06
URL:		http://folding.stanford.edu/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
ExclusiveArch:	%{ix86}

%description
Folding@Home is a distributed client computing effort by Stanford
University intended to help understand how proteins assemble or "fold".

%description -l pl
Folding@Home jest klientem projektu obliczeñ rozproszonych Uniwersytetu
Stanford maj±cym na celu pomoc w zrozumieniu jak tworz± siê bia³ka.

%install
rm -rf $RPM_BUILD_ROOT

install -D %{SOURCE0} $RPM_BUILD_ROOT%{_bindir}/foldingathome-bin

cat > $RPM_BUILD_ROOT%{_bindir}/foldingathome << EOF
#!/bin/sh
test -d \$HOME/.fah || mkdir \$HOME/.fah
cd \$HOME/.fah && %{_bindir}/foldingathome-bin "\$@"
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(755,root,root) %{_bindir}/*
