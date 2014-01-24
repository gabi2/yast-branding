#
# spec file for package yast2-branding-SLED
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           yast2-branding-SLED
Version:        3.1.0
Release:        0
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        COPYING
Prefix:         /usr
BuildRequires:  yast2-devtools
BuildArch:      noarch
Provides:       yast2-branding
Supplements:    packageand(yast2:branding-SLED)
Conflicts:      otherproviders(yast2-branding)
Requires:       yast2-theme-SLE
Summary:        YaST2 - SLED Branding
License:        GPL-2.0+
Group:          System/YaST

%description
YaST2 branding for the SUSE LINUX Enterprise Desktop distribution



%prep

%install
mkdir -p $RPM_BUILD_ROOT%{prefix}/share/doc/packages/yast2-branding-SLED
mkdir -p $RPM_BUILD_ROOT%{prefix}/share/YaST2/theme
cp $RPM_SOURCE_DIR/COPYING $RPM_BUILD_ROOT%{prefix}/share/doc/packages/yast2-branding-SLED
cd $RPM_BUILD_ROOT%{prefix}/share/YaST2/theme
ln -sf SLE current

%files
%defattr(644,root,root,755)
%dir %{prefix}/share/YaST2/theme
%{prefix}/share/doc/packages/yast2-branding-SLED/
%{prefix}/share/YaST2/theme/current

%changelog