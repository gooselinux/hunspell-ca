Name: hunspell-ca
Summary: Catalan hunspell dictionaries
%define upstreamid 20090630
Version: 0.%{upstreamid}
Release: 2.1%{?dist}
#svn checkout svn://softcatala.org/corrector/trunk/resultats/hunspell
Source: hunspell-ca-%{upstreamid}.tar.bz2
Group: Applications/Text
URL: http://www.softcatala.org/wiki/Projectes/Corrector_ortogràfic
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: GPLv2+
BuildArch: noarch

Requires: hunspell

%description
Catalan hunspell dictionaries.

%prep
%setup -q -n hunspell

%build
tr -d '\r' < catalan.aff > ca_ES.aff
tr -d '\r' < catalan.dic > ca_ES.dic

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p ca_ES.dic ca_ES.aff $RPM_BUILD_ROOT/%{_datadir}/myspell
pushd $RPM_BUILD_ROOT/%{_datadir}/myspell/
ca_ES_aliases="ca_AD ca_FR ca_IT"
for lang in $ca_ES_aliases; do
        ln -s ca_ES.aff $lang.aff
        ln -s ca_ES.dic $lang.dic
done
popd

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_datadir}/myspell/*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.20090630-2.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20090630-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 01 2009 Caolan McNamara <caolanm@redhat.com> - 0.20090630-1
- latest version

* Wed Mar 11 2009 Caolan McNamara <caolanm@redhat.com> - 0.20090311-1
- latest version

* Tue Mar 10 2009 Caolan McNamara <caolanm@redhat.com> - 0.20090309-1
- latest version

* Tue Mar 03 2009 Caolan McNamara <caolanm@redhat.com> - 0.20090302-1
- latest version

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20081027-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Oct 28 2008 Caolan McNamara <caolanm@redhat.com> - 0.20081027-1
- latest version

* Mon Oct 20 2008 Caolan McNamara <caolanm@redhat.com> - 0.20081019-1
- latest version

* Sun Oct 05 2008 Caolan McNamara <caolanm@redhat.com> - 0.20081005-1
- latest version

* Tue Sep 30 2008 Caolan McNamara <caolanm@redhat.com> - 0.20080918-1
- latest version

* Mon Sep 15 2008 Caolan McNamara <caolanm@redhat.com> - 0.20080915-1
- latest version

* Tue Jul 08 2008 Caolan McNamara <caolanm@redhat.com> - 0.20080706-2
- Catalan is spoken in Andora, France and Italy as well

* Mon Jul 07 2008 Caolan McNamara <caolanm@redhat.com> - 0.20080706-1
- latest version

* Wed Jul 02 2008 Caolan McNamara <caolanm@redhat.com> - 0.20080620-1
- latest version

* Fri Aug 03 2007 Caolan McNamara <caolanm@redhat.com> - 0.20060508-2
- clarify license version

* Mon Jul 09 2007 Caolan McNamara <caolanm@redhat.com> - 0.20060508-1
- latest version

* Thu Dec 07 2006 Caolan McNamara <caolanm@redhat.com> - 0.20021015-1
- initial version
