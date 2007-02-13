Summary:	Folding@home client
Summary(pl.UTF-8):	Klient Folding@home
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

%description -l pl.UTF-8
Folding@Home jest klientem projektu obliczeń rozproszonych Uniwersytetu
Stanford mającym na celu pomoc w zrozumieniu jak tworzą się białka.

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
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
