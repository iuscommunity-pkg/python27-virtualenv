%global pymajor 2
%global pyminor 7
%global pyver %{pymajor}.%{pyminor}
%global iusver %{pymajor}%{pyminor}
%global __python2 %{_bindir}/python%{pyver}
%global python2_sitelib  %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")
%global python2_sitearch %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")
%global __os_install_post %{__python27_os_install_post}
%global srcname virtualenv
%global src %(echo %{srcname} | cut -c1)

Name:           python%{iusver}-%{srcname}
Version:        13.1.2
Release:        1.ius%{?dist}
Summary:        Tool to create isolated Python environments
Vendor:         IUS Community Project
Group:          Development/Languages
License:        MIT
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://pypi.python.org/packages/source/%{src}/%{srcname}/%{srcname}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  python%{iusver}-devel
BuildRequires:  python%{iusver}-setuptools
Requires:       python%{iusver}-devel
Requires:       python%{iusver}-setuptools


%description
virtualenv is a tool to create isolated Python environments. virtualenv
is a successor to workingenv, and an extension of virtual-python. It is
written by Ian Bicking, and sponsored by the Open Planning Project. It is
licensed under an MIT-style permissive license.


%prep
%setup -q -n %{srcname}-%{version}
find -name '*.py' -type f -print0 | xargs -0 sed -i '1s|python|&%{pyver}|'


%build
%{__python2} setup.py build


%install
%{__rm} -rf %{buildroot}
%{__python2} setup.py install --optimize 1 --skip-build --root %{buildroot}
%{__rm} -f %{buildroot}%{_bindir}/virtualenv
%{__rm} -f build/sphinx/html/.buildinfo


%clean
rm -rf $RPM_BUILD_ROOT


%files
%doc docs/*rst PKG-INFO AUTHORS.txt LICENSE.txt
%{python2_sitelib}/*
%attr(755,root,root) %{_bindir}/virtualenv-%{pyver}


%changelog
* Mon Aug 24 2015 Ben Harper <ben.harper@rackspace.com> - 13.1.2-1.ius
- Latest upstream

* Fri Aug 21 2015 Ben Harper <ben.harper@rackspace.com> - 13.1.1-1.ius
- Latest upstream

* Thu Jul 02 2015 Ben Harper <ben.harper@rackspace.com> - 13.1.0-1.ius
- Latest upstream

* Mon Jun 08 2015 Carl George <carl.george@rackspace.com> - 13.0.3-1.ius
- Latest upstream

* Fri May 22 2015 Carl George <carl.george@rackspace.com> - 13.0.0-1.ius
- Latest upstream

* Tue Apr 07 2015 Carl George <carl.george@rackspace.com> - 12.1.1-1.ius
- Latest upstream

* Thu Feb 05 2015 Ben Harper <ben.harper@rackspace.com> - 12.0.7-1.ius
- Latest sources from upstream

* Thu Jan 29 2015 Carl George <carl.george@rackspace.com> - 12.0.6-1.ius
- Latest upstream

* Mon Jan 05 2015 Carl George <carl.george@rackspace.com> - 12.0.5-1.ius
- Latest upstream

* Fri Dec 26 2014 Carl George <carl.george@rackspace.com> - 12.0.4-1.ius
- Latest upstream

* Fri Jun 06 2014 Carl George <carl.george@rackspace.com> - 1.11.6-2.ius
- Override __os_install_post to fix .pyc/pyo magic
- Implement python packaging best practices

* Mon May 19 2014 Ben Harper <ben.harper@rackspace.com> - 1.11.6-1.ius
- Latest sources from upstream

* Mon May 05 2014 Carl George <carl.george@rackspace.com> - 1.11.5-1.ius
- Latest sources from upstream

* Tue Feb 25 2014 Ben Harper <ben.harper@rackspace.com> - 1.11.4-1.ius
- Latest sources from upstream

* Fri Feb 21 2014 Ben Harper <ben.harper@rackspace.com> - 1.11.3-1.ius
- Latest sources from upstream

* Mon Jan 27 2014 Ben Harper <ben.harper@rackspace.com> - 1.11.2-1.ius
- Latest sources from upstream

* Tue Jan 21 2014 Ben Harper <ben.harper@rackspace.com> - 1.11.1-1.ius
- Latest sources from upstream

* Fri Jan 03 2014 Ben Harper <ben.harper@rackspace.com> - 1.11-1.ius
- Latest sources from upstream

* Fri Oct 18 2013 Ben Harper <ben.harper@rackspace.com> - 1.10.1-3.ius
- removing /usr/bin/virtualenv as it conflicts with python-virtualenv from EPEL

* Wed Oct 16 2013 Ben Harper <ben.harper@rackspace.com> - 1.10.1-2.ius
- porting from EPEL

* Thu Aug 15 2013 Steve 'Ashcrow' Milner <me@stevemilner.org> - 1.10.1-1
- Upstream upgraded pip to v1.4.1
- Upstream upgraded setuptools to v0.9.8 (fixes CVE-2013-1633)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 14 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 1.9.1-1
- Update to upstream 1.9.1 because of security issues with the bundled
  python-pip in older releases.  This is just a quick fix until a
  python-virtualenv maintainer can unbundle the python-pip package
  see: https://bugzilla.redhat.com/show_bug.cgi?id=749378

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Aug 14 2012 Steve Milner <me@stevemilner.org> - 1.7.2-1
- Update for upstream bug fixes.
- Added path for versioned binary.
- Patch no longer required.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Mar 14 2012 Steve 'Ashcrow' Milner <me@stevemilner.org> - 1.7.1.2-1
- Update for upstream bug fixes.
- Added patch for sphinx building

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 20 2011 Steve 'Ashcrow' Milner <me@stevemilner.org> - 1.7-1
- Update for https://bugzilla.redhat.com/show_bug.cgi?id=769067

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Oct 16 2010 Steve 'Ashcrow' Milner <me@stevemilner.org> - 1.5.1-1
- Added _weakrefset requirement for Python 2.7.1.
- Add support for PyPy.
- Uses a proper temporary dir when installing environment requirements.
- Add --prompt option to be able to override the default prompt prefix.
- Add fish and csh activate scripts.

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 1.4.8-4
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Tue Jul  7 2010 Steve 'Ashcrow' Milner <me@stevemilner.org> - 1.4.8-3
- Fixed EPEL installation issue from BZ#611536

* Tue Jun  8 2010 Steve 'Ashcrow' Milner <me@stevemilner.org> - 1.4.8-2
- Only replace the python shebang on the first line (Robert Buchholz)

* Fri Apr 28 2010 Steve 'Ashcrow' Milner <me@stevemilner.org> - 1.4.8-1
- update pip to 0.7
- move regen-docs into bin/
- Fix #31, make activate_this.py work on Windows (use Lib/site-packages)
unset PYTHONHOME envioronment variable -- first step towards fixing the PYTHONHOME issue; see e.g. https://bugs.launchpad.net/virtualenv/+bug/290844
- unset PYTHONHOME in the (Unix) activate script (and reset it in deactivate())
- use the activate.sh in virtualenv.py via running bin/rebuild-script.py
- add warning message if PYTHONHOME is set

* Fri Apr 2 2010 Steve 'Ashcrow' Milner <me@stevemilner.org> - 1.4.6-1
- allow script creation without setuptools
- fix problem with --relocate when bin/ has subdirs (fixes #12)
- Allow more flexible .pth file fixup
- make nt a required module, along with posix. it may not be a builtin module on jython
- don't mess with PEP 302-supplied __file__, from CPython, and merge in a small startup optimization for Jython, from Jython

* Tue Dec 22 2009 Steve 'Ashcrow' Milner <me@stevemilner.org> - 1.4.3-1
- Updated for upstream release.

* Thu Nov 12 2009 Steve 'Ashcrow' Milner <me@stevemilner.org> - 1.4.2-1
- Updated for upstream release.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Apr 28 2009 Steve 'Ashcrow' Milner <me@stevemilner.org> - 1.3.3-1
- Updated for upstream release.

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Dec 25 2008 Steve 'Ashcrow' Milner <me@stevemilner.org> - 1.3.2-1
- Updated for upstream release.

* Thu Dec 04 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.3.1-4
- Rebuild for Python 2.6

* Mon Dec  1 2008 Steve 'Ashcrow' Milner <me@stevemilner.org> - 1.3.1-3
- Added missing dependencies.

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.3.1-2
- Rebuild for Python 2.6

* Fri Nov 28 2008 Steve 'Ashcrow' Milner <me@stevemilner.org> - 1.3.1-1
- Updated for upstream release

* Sun Sep 28 2008 Steve 'Ashcrow' Milner <me@stevemilner.org> - 1.3-1
- Updated for upstream release

* Sat Aug 30 2008 Steve 'Ashcrow' Milner <me@stevemilner.org> - 1.2-1
- Updated for upstream release

* Fri Aug 29 2008 Steve 'Ashcrow' Milner <me@stevemilner.org> - 1.1-3
- Updated from review notes

* Thu Aug 28 2008 Steve 'Ashcrow' Milner <me@stevemilner.org> - 1.1-2
- Updated from review notes

* Tue Aug 26 2008 Steve 'Ashcrow' Milner <me@stevemilner.org> - 1.1-1
- Initial Version
