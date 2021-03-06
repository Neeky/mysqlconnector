# MySQL Connector/Python - MySQL driver written in Python.
# Copyright (c) 2012, 2014, Oracle and/or its affiliates. All rights reserved.

# MySQL Connector/Python is licensed under the terms of the GPLv2
# <http://www.gnu.org/licenses/old-licenses/gpl-2.0.html>, like most
# MySQL Connectors. There are special exceptions to the terms and
# conditions of the GPLv2 as it is applied to this software, see the
# FOSS License Exception
# <http://www.mysql.com/about/legal/licensing/foss-exception.html>.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA

%define	mysql_license	Commercial
%define name 		%(python -c "import setupinfo as m; print '%s-commercial' % m.name.lower().replace('_','-')")
%define name_gpl        %(python -c "import setupinfo as m; print m.name.lower().replace('_','-')")
%define	version 	%(python -c "import setupinfo as m; print m.version")
%define summary		%(python -c "import setupinfo as m; print m.description")
%define vendor		%(python -c "import setupinfo as m; print m.author")
%define packager	Oracle and/or its affiliates Product Engineering Team <mysql-build@oss.oracle.com>

# $ rpm --showrc | grep -e _build_name_fmt -e _rpmfilename
%define _rpmfilename %%{ARCH}/%%{NAME}-%%{VERSION}%{?edition}-%%{RELEASE}.%%{ARCH}.rpm

# SuSE
%if %(test -f /etc/SuSE-release && echo 1 || echo 0)
%define susever %(rpm -qf --qf '%%{version}\\n' /etc/SuSE-release | cut -d. -f1)
%define dist   .sles%{susever}
%endif

%{!?bdist_dir: %{error:Macro bdist_dir not defined}}

%{!?py_ver:     %{expand: %%global py_ver      %%(echo `python -c "import sys; print sys.version[:3]"`)}}
%{!?py_prefix:  %{expand: %%global py_prefix   %%(echo `python -c "import sys; print sys.prefix"`)}}
%{!?py_libdir:  %{expand: %%global py_libdir   %%{expand:%%%%{py_prefix}/%%%%{_lib}/python%%%%{py_ver}}}}
%{!?python_sitelib: %{expand: %%global python_sitelib  %%{expand:%%%%{py_libdir}/site-packages}}}

%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print (get_python_lib())")}

# We do not want rpmbuild to byte compile .py files
%define __os_install_post %{___build_post}

Name:		%{name}
Version:	%{version}
Release:	1%{?dist}
Summary:	%{summary}

Group:		Development/Libraries
License:	Copyright (c) 2009, 2014, Oracle and/or its affiliates. All rights reserved.  Use is subject to license terms.  Under %{mysql_license} license as shown in the Description field.
Vendor:		%{vendor}
Packager:	%{packager}
URL:		http://www.mysql.com/
Source0:    mysql-connector-python-commercial-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch

BuildRequires:	python
Requires:	python
Conflicts:  %{name_gpl}
Provides:   %{name} = %{version}
Obsoletes:  %{name} <= %{version}, %{name_gpl} <= %{version}

%description
This is a release of MySQL Connector/Python, Oracle's dual-
license Python Driver for MySQL. For the avoidance of
doubt, this particular copy of the software is released
under a commercial license and the GNU General Public
License does not apply. MySQL Connector/Python is brought
to you by Oracle.

Copyright (c) 2009, 2014, Oracle and/or its affiliates. All rights reserved.

This distribution may include materials developed by third
parties. For license and attribution notices for these
materials, please refer to the documentation that accompanies
this distribution (see the "Licenses for Third-Party Components"
appendix) or view the online documentation at 
<http://dev.mysql.com/doc/>

%prep
%setup -q

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{python_sitelib}
%{__python} setup.py install --prefix=%{_prefix} --root %{buildroot}
find %{buildroot}%{python_sitelib}/mysql/connector -name '*.py' -delete
rm -f %{buildroot}%{python_sitelib}/mysql/__init__.py*

%clean
rm -rf ${buildroot}

%files
%defattr(-,root,root,-)
#%doc %{bdist_dir}README.txt %{bdist_dir}LICENSE.txt
#%doc %{bdist_dir}/docs/mysql-connector-python.pdf
#%doc %{bdist_dir}/docs/mysql-connector-python.html %{bdist_dir}/docs/mysql-html.css
%doc LICENSE.txt CHANGES.txt README.txt docs/*.pdf docs/*.html docs/*.css
%{python_sitelib}/mysql/connector
%{python_sitelib}/mysql_connector_python-%{version}*egg-info

%post
touch %{python_sitelib}/mysql/__init__.py

%postun
if [ $1 == 0 ];
then
    # Non empty directories will be left alone
    rmdir %{python_sitelib}/mysql/connector/locales/eng 2>/dev/null
    rmdir %{python_sitelib}/mysql/connector/locales 2>/dev/null
    rmdir %{python_sitelib}/mysql/connector/django 2>/dev/null
    rmdir %{python_sitelib}/mysql/connector/fabric 2>/dev/null
    rmdir %{python_sitelib}/mysql/connector 2>/dev/null

    # Try to remove the MySQL top package mysql/
    SUBPKGS=`ls --ignore=*.py{c,o} -m %{python_sitelib}/mysql`
    if [ "$SUBPKGS" == "__init__.py" ];
    then
        rm %{python_sitelib}/mysql/__init__.py* 2>/dev/null 1>&2
        rmdir %{python_sitelib}/mysql/ 2>/dev/null
    fi
    exit 0
fi


%changelog
* Wed Dec 17 2014 Geert Vanderkelen <geert.vanderkelen@oracle.com> - 2.0.3

- Added spec file for Connector/Python 2.0 series.
- Installing instead of copying files in %build

* Fri Mar 28 2014 Geert Vanderkelen <geert.vanderkelen@oracle.com> - 2.0.0

- Changing metasetupinfo.py to setupinfo.py.
- Fixing 'bogus' log entries.

* Fri Mar  7 2014 Peeyush Gupta <peeyush.x.gupta@oracle.com> - 1.2.1

- Added removal of the fabric folder.

* Mon Nov  4 2013 Geert Vanderkelen <geert.vanderkelen@oracle.com> - 1.1.4

- Is not possible to 'upgrade' the Commercial edition to GPL Edition.
- Added removal of the django folder.

* Fri Sep 20 2013 Geert Vanderkelen <geert.vanderkelen@oracle.com> - 1.1.2

- It is now possible to set the 'edition' variable for special releases

* Mon Feb 18 2013 Geert Vanderkelen <geert.vanderkelen@oracle.com> - 1.0.9

- 'prep' is now used to unpack the source distribution
- 'install' removes the __init__.pyc, recreated in 'post'
- 'files' now selectively includes files owned by Connector/Python
- 'post' now creates the mysql/__init__.py which does not get
  installed any longer since shared by multiple projects
- 'postun' tries to remove the top package mysql/
- Updating the copyright.

* Thu Aug 16 2012 Geert Vanderkelen <geert.vanderkelen@oracle.com>

- Name of the commercial package includes 'commercial'
- Removed 'Source' and replaced 'URL' with MySQL homepage
- Added the Packager information
- Adding documentation files

* Tue Jul 31 2012 Kent Boortz <kent.boortz@oracle.com>

- Aligned commercial and GPL spec files
- Use "python" in PATH, to be able to specify a recent enough Python
- Set sitedir, "{_rpmconfigdir}/macros.python" is missing in some distros

* Tue Jun 05 2012 Geert Vanderkelen <geert.vanderkelen@oracle.com> - 1.0.3

- Initial implementation.

