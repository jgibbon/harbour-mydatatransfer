# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       harbour-mydatatransfer

# >> macros
# << macros

%{!?qtc_qmake:%define qtc_qmake %qmake}
%{!?qtc_qmake5:%define qtc_qmake5 %qmake5}
%{!?qtc_make:%define qtc_make make}
%{?qtc_builddir:%define _builddir %qtc_builddir}
Summary:        My Data Transfer
Version:        0.0.4
Release:        2
Group:          Qt/Qt
License:        GPLv3
Packager:       fravaccaro <fravaccaro@jollacommunity.it>
URL:            https://github.com/fravaccaro/harbour-mydatatransfer
Source0:        %{name}-%{version}.tar.bz2
Source100:      harbour-mydatatransfer.yaml
Requires:       sailfishsilica-qt5 >= 0.10.9, sailfish-version >= 3.2.0, rsync
BuildRequires:  pkgconfig(sailfishapp) >= 1.0.2
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  desktop-file-utils

%description
Backup and transfer app data, documents, music, pictures and videos on your Sailfish OS devices.


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%preun
if [ "$1" = "0" ]; then
    rm -rf /home/nemo/.local/share/%{name}
fi

%build
# >> build pre
# << build pre

%qtc_qmake5 

%qtc_make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%qmake5_install

# >> install post
# << install post

desktop-file-install --delete-original       \
  --dir %{buildroot}%{_datadir}/applications             \
   %{buildroot}%{_datadir}/applications/*.desktop

%files
%defattr(-,root,root,-)
%{_bindir}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
# >> files
# << files

%post
chmod +x /usr/share/%{name}/scripts/*.sh
