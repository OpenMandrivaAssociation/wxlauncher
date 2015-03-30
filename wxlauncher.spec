%define debug_package	%{nil}

Name:		wxlauncher
Version:	0.9.4
Release:	2

Summary:	Cross-platform launcher for the FreeSpace 2
License:	GPLv2
Group:		Games/Strategy 
Url:		http://www.hard-light.net/forums/index.php?topic=67950.0"
Source0:	http://wxlauncher.googlecode.com/files/%{name}-%{version}.tar.gz
Source1:	wxlauncher.png
Source2:	wxlauncher.desktop
#https://wxlauncher.googlecode.com/issues/attachment?aid=930010000&name=wxlauncher_homedir.patch&token=ABZ6GAdPROo_5aMga1FoSSzNFfUdmrHNhw%3A1427549336627
Patch0:		wxlauncher_homedir.patch

BuildRequires:  cmake
BuildRequires:  wxPythonGTK-devel
BuildRequires:  wxgtku2.8-devel
BuildRequires:  pkgconfig(python)
BuildRequires:  python-setuptools
BuildRequires:  python
BuildRequires:  pkgconfig(openal)
BuildRequires:  pythonegg(markdown)
BuildRequires:  pkgconfig(sdl)
BuildRequires:  imagemagick
BuildRequires:  desktop-file-utils

%description
This is wxLauncher,a cross-platform 
launcher for the FreeSpace 2 Open engine.
Our goal is to make setting up and using 
Freespace 2 Open and its Total Conversions 
as easy as possible by providing 
an interface that is functional.

%files
%doc ReadMe.txt License.txt Thanks.txt
%{_bindir}/wxlauncher
%{_datadir}/wxlauncher/*.png
%{_datadir}/wxlauncher/*.ico
%{_datadir}/wxlauncher/onlinehelp.htb
%{_liconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_datadir}/applications/%{name}.desktop



#-------------------------------------------------
%prep
%setup -q
%patch0 -p0

%build
%cmake -DUSE_OPENAL=1 \
  -DCMAKE_INSTALL_PREFIX=/usr ../ \
  -DRESOURCES_PATH=%{_datadir}/wxlauncher \
  -DwxWidgets_CONFIG_EXECUTABLE=/usr/bin/wx-config \
  -DwxWidgets_wxrc_EXECUTABLE=/usr/bin/wxrc-2.8
  
%make

%install
%makeinstall_std -C build
# Icons
install -d -m755 %{buildroot}{%{_liconsdir},%{_iconsdir},%{_miconsdir}}
convert %{SOURCE1} -resize 48x48 %{buildroot}%{_liconsdir}/%{name}.png
convert %{SOURCE1} -resize 32x32 %{buildroot}%{_iconsdir}/%{name}.png
convert %{SOURCE1} -resize 16x16 %{buildroot}%{_miconsdir}/%{name}.png

# menu entry
install -d -m755 %{buildroot}%{_datadir}/applications
desktop-file-install %{SOURCE2} \
  --dir=%{buildroot}%{_datadir}/applications
  






