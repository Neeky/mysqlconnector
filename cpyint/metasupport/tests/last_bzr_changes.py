
#
# This file is needed to find out which files were changed when in the
# Connector/Python v1.x repository.
#
# The initial data was produced using following:
#
#  for file in `bzr ls --versioned --recursive`; do
#    STAMP=`bzr log --timezone utc $file | grep timestamp: | head -n1`;
#    echo "'$file': '$STAMP',";
#  done
#

BAZAAR_CHANGES = {
    'AUTHORS': 'Sun 2012-04-22 12:23:37 +0000',
    'COPYING': 'Thu 2009-11-26 16:14:48 +0000',
    'ChangeLog': 'Thu 2014-03-13 07:46:50 +0000',
    'LICENSE_com.txt': 'Thu 2014-02-13 11:24:57 +0000',
    'MANIFEST.in': 'Tue 2013-12-03 10:01:33 +0000',
    'README': 'Thu 2014-02-13 11:24:57 +0000',
    'README_com.txt': 'Thu 2014-02-13 11:24:57 +0000',
    'docs/': 'Thu 2013-09-19 12:32:35 +0000',
    'docs/README_DOCS.txt': 'Thu 2013-09-19 12:32:35 +0000',
    'docs/mysql-connector-python.html': 'Tue 2012-07-17 18:31:32 +0000',
    'docs/mysql-connector-python.pdf': 'Tue 2012-07-17 18:31:32 +0000',
    'docs/mysql-connector-python.txt': 'Tue 2012-07-17 18:31:32 +0000',
    'docs/mysql-html.css': 'Tue 2012-07-17 18:31:32 +0000',
    'metasetupinfo.py': 'Thu 2014-03-13 07:46:50 +0000',
    'python2/': 'Thu 2014-04-03 11:25:53 +0000',
    'python2/__init__.py': 'Fri 2010-05-21 14:06:04 +0000',
    'python2/examples/': 'Mon 2013-09-02 16:40:41 +0000',
    'python2/examples/__init__.py': 'Fri 2009-11-27 15:16:00 +0000',
    'python2/examples/client.py': 'Fri 2013-02-01 12:42:21 +0000',
    'python2/examples/config.py': 'Fri 2013-02-01 12:42:21 +0000',
    'python2/examples/dates.py': 'Fri 2013-02-01 12:42:21 +0000',
    'python2/examples/engines.py': 'Fri 2013-02-01 12:42:21 +0000',
    'python2/examples/inserts.py': 'Fri 2013-02-01 12:42:21 +0000',
    'python2/examples/microseconds.py': 'Fri 2013-02-01 12:42:21 +0000',
    'python2/examples/multi_resultsets.py': 'Fri 2013-02-01 12:42:21 +0000',
    'python2/examples/prepared_statements.py': 'Wed 2013-05-01 11:28:30 +0000',
    'python2/examples/transaction.py': 'Fri 2013-02-01 12:42:21 +0000',
    'python2/examples/unicode.py': 'Fri 2013-02-01 12:42:21 +0000',
    'python2/examples/warnings.py': 'Mon 2013-09-02 16:40:41 +0000',
    'python2/mysql/': 'Thu 2014-04-03 11:25:53 +0000',
    'python2/mysql/__init__.py': 'Wed 2008-05-07 06:15:39 +0000',
    'python2/mysql/connector/': 'Thu 2014-04-03 11:25:53 +0000',
    'python2/mysql/connector/__init__.py': 'Fri 2014-02-21 10:40:37 +0000',
    'python2/mysql/connector/authentication.py': 'Fri 2014-02-21 10:40:37 +0000',
    'python2/mysql/connector/charsets.py': 'Thu 2014-02-13 11:24:57 +0000',
    'python2/mysql/connector/connection.py': 'Thu 2014-04-03 11:25:53 +0000',
    'python2/mysql/connector/constants.py': 'Fri 2014-02-21 10:40:37 +0000',
    'python2/mysql/connector/conversion.py': 'Tue 2014-01-21 09:48:59 +0000',
    'python2/mysql/connector/cursor.py': 'Mon 2014-03-10 10:07:41 +0000',
    'python2/mysql/connector/dbapi.py': 'Mon 2013-10-28 11:16:41 +0000',
    'python2/mysql/connector/errorcode.py': 'Thu 2014-02-13 11:24:57 +0000',
    'python2/mysql/connector/errors.py': 'Tue 2013-12-03 10:01:33 +0000',
    'python2/mysql/connector/locales/': 'Thu 2014-02-13 11:24:57 +0000',
    'python2/mysql/connector/locales/__init__.py': 'Mon 2013-10-28 11:16:41 +0000',
    'python2/mysql/connector/locales/eng/': 'Thu 2014-02-13 11:24:57 +0000',
    'python2/mysql/connector/locales/eng/__init__.py': 'Thu 2013-11-21 14:20:21 +0000',
    'python2/mysql/connector/locales/eng/client_error.py': 'Thu 2014-02-13 11:24:57 +0000',
    'python2/mysql/connector/network.py': 'Mon 2013-10-28 11:16:41 +0000',
    'python2/mysql/connector/pooling.py': 'Thu 2014-02-20 17:55:36 +0000',
    'python2/mysql/connector/protocol.py': 'Thu 2014-04-03 11:25:53 +0000',
    'python2/mysql/connector/utils.py': 'Thu 2013-12-12 12:49:00 +0000',
    'python23/': 'Mon 2014-03-31 10:56:26 +0000',
    'python23/__init__.py': 'Tue 2013-08-06 11:24:28 +0000',
    'python23/django/': 'Mon 2014-03-31 10:56:26 +0000',
    'python23/django/__init__.py': 'Thu 2013-09-19 12:32:35 +0000',
    'python23/django/base.py': 'Mon 2014-03-31 10:56:26 +0000',
    'python23/django/client.py': 'Thu 2013-09-19 12:32:35 +0000',
    'python23/django/compiler.py': 'Tue 2014-01-21 10:36:58 +0000',
    'python23/django/creation.py': 'Tue 2014-01-21 10:36:58 +0000',
    'python23/django/introspection.py': 'Mon 2014-03-31 10:56:26 +0000',
    'python23/django/validation.py': 'Tue 2014-01-21 10:36:58 +0000',
    'python23/fabric/': 'Thu 2014-03-13 07:46:50 +0000',
    'python23/fabric/__init__.py': 'Fri 2014-01-10 11:11:20 +0000',
    'python23/fabric/balancing.py': 'Sat 2014-01-11 07:16:48 +0000',
    'python23/fabric/caching.py': 'Thu 2014-03-06 16:26:37 +0000',
    'python23/fabric/connection.py': 'Thu 2014-03-13 07:46:50 +0000',
    'python3/': 'Thu 2014-04-03 11:25:53 +0000',
    'python3/__init__.py': 'Fri 2010-05-21 13:52:17 +0000',
    'python3/examples/': 'Mon 2013-09-02 16:40:41 +0000',
    'python3/examples/__init__.py': 'Mon 2009-12-21 15:53:20 +0000',
    'python3/examples/config.py': 'Fri 2013-02-01 12:42:21 +0000',
    'python3/examples/dates.py': 'Fri 2013-02-01 12:42:21 +0000',
    'python3/examples/engines.py': 'Fri 2013-02-01 12:42:21 +0000',
    'python3/examples/inserts.py': 'Fri 2013-02-01 12:42:21 +0000',
    'python3/examples/microseconds.py': 'Fri 2013-02-01 12:42:21 +0000',
    'python3/examples/multi_resultsets.py': 'Fri 2013-02-01 12:42:21 +0000',
    'python3/examples/prepared_statements.py': 'Wed 2013-05-01 11:28:30 +0000',
    'python3/examples/transaction.py': 'Fri 2013-02-01 12:42:21 +0000',
    'python3/examples/unicode.py': 'Fri 2013-02-01 12:42:21 +0000',
    'python3/examples/warnings.py': 'Mon 2013-09-02 16:40:41 +0000',
    'python3/mysql/': 'Thu 2014-04-03 11:25:53 +0000',
    'python3/mysql/__init__.py': 'Mon 2009-12-21 15:53:20 +0000',
    'python3/mysql/connector/': 'Thu 2014-04-03 11:25:53 +0000',
    'python3/mysql/connector/__init__.py': 'Thu 2014-02-20 17:55:36 +0000',
    'python3/mysql/connector/authentication.py': 'Fri 2014-02-21 10:40:37 +0000',
    'python3/mysql/connector/charsets.py': 'Thu 2014-02-13 11:24:57 +0000',
    'python3/mysql/connector/connection.py': 'Thu 2014-04-03 11:25:53 +0000',
    'python3/mysql/connector/constants.py': 'Fri 2014-02-21 10:40:37 +0000',
    'python3/mysql/connector/conversion.py': 'Tue 2014-01-21 09:48:59 +0000',
    'python3/mysql/connector/cursor.py': 'Mon 2014-03-10 10:07:41 +0000',
    'python3/mysql/connector/dbapi.py': 'Mon 2013-10-28 11:16:41 +0000',
    'python3/mysql/connector/errorcode.py': 'Thu 2014-02-13 11:24:57 +0000',
    'python3/mysql/connector/errors.py': 'Tue 2013-12-03 10:01:33 +0000',
    'python3/mysql/connector/locales/': 'Thu 2014-02-13 11:24:57 +0000',
    'python3/mysql/connector/locales/__init__.py': 'Mon 2013-10-28 11:16:41 +0000',
    'python3/mysql/connector/locales/eng/': 'Thu 2014-02-13 11:24:57 +0000',
    'python3/mysql/connector/locales/eng/__init__.py': 'Thu 2013-11-21 14:20:21 +0000',
    'python3/mysql/connector/locales/eng/client_error.py': 'Thu 2014-02-13 11:24:57 +0000',
    'python3/mysql/connector/network.py': 'Mon 2014-03-31 10:56:26 +0000',
    'python3/mysql/connector/pooling.py': 'Thu 2014-02-20 17:55:36 +0000',
    'python3/mysql/connector/protocol.py': 'Thu 2014-04-03 11:25:53 +0000',
    'python3/mysql/connector/utils.py': 'Thu 2013-12-12 12:49:00 +0000',
    'setup.cfg': 'Wed 2013-08-14 10:57:43 +0000',
    'setup.py': 'Fri 2013-02-01 12:42:21 +0000',
    'support/': 'Thu 2014-03-13 07:46:50 +0000',
    'support/Debian/': 'Thu 2014-03-13 07:46:50 +0000',
    'support/Debian/commercial/': 'Thu 2014-03-13 07:46:50 +0000',
    'support/Debian/commercial/changelog': 'Thu 2014-03-13 07:46:50 +0000',
    'support/Debian/commercial/compat': 'Wed 2013-08-14 10:57:43 +0000',
    'support/Debian/commercial/control': 'Thu 2014-02-13 11:24:57 +0000',
    'support/Debian/commercial/copyright': 'Thu 2014-02-13 11:24:57 +0000',
    'support/Debian/commercial/docs': 'Wed 2013-08-14 10:57:43 +0000',
    'support/Debian/commercial/postinst': 'Thu 2013-12-12 12:49:40 +0000',
    'support/Debian/commercial/postrm': 'Thu 2013-12-12 12:49:40 +0000',
    'support/Debian/commercial/rules': 'Thu 2013-12-12 12:49:40 +0000',
    'support/Debian/commercial/source/': 'Wed 2013-08-14 10:57:43 +0000',
    'support/Debian/commercial/source/format': 'Wed 2013-08-14 10:57:43 +0000',
    'support/Debian/gpl/': 'Thu 2014-03-13 07:46:50 +0000',
    'support/Debian/gpl/changelog': 'Thu 2014-03-13 07:46:50 +0000',
    'support/Debian/gpl/compat': 'Wed 2013-08-14 10:57:43 +0000',
    'support/Debian/gpl/control': 'Thu 2014-02-13 11:24:57 +0000',
    'support/Debian/gpl/copyright': 'Thu 2014-02-13 11:24:57 +0000',
    'support/Debian/gpl/docs': 'Wed 2013-08-14 10:57:43 +0000',
    'support/Debian/gpl/postinst': 'Thu 2013-12-12 12:49:40 +0000',
    'support/Debian/gpl/postrm': 'Thu 2013-12-12 12:49:40 +0000',
    'support/Debian/gpl/rules': 'Thu 2013-12-12 12:49:40 +0000',
    'support/Debian/gpl/source/': 'Wed 2013-08-14 10:57:43 +0000',
    'support/Debian/gpl/source/format': 'Wed 2013-08-14 10:57:43 +0000',
    'support/MSWindows/': 'Thu 2014-03-13 07:46:50 +0000',
    'support/MSWindows/product.wxs': 'Fri 2014-02-21 10:40:37 +0000',
    'support/MSWindows/product_com.wxs': 'Thu 2014-03-13 07:46:50 +0000',
    'support/MSWindows/upgrade_codes.json': 'Tue 2013-12-03 22:46:24 +0000',
    'support/OSX/': 'Thu 2013-12-19 10:02:26 +0000',
    'support/OSX/Description.plist': 'Fri 2013-12-13 09:58:16 +0000',
    'support/OSX/Info.plist': 'Fri 2013-12-13 09:58:16 +0000',
    'support/OSX/PkgInfo': 'Fri 2013-12-13 09:58:16 +0000',
    'support/OSX/Welcome.rtf': 'Thu 2013-12-19 10:02:26 +0000',
    'support/OSX/postflight': 'Fri 2013-12-13 09:58:16 +0000',
    'support/RPM/': 'Mon 2014-03-10 09:59:40 +0000',
    'support/RPM/connector_python.spec': 'Mon 2014-03-10 09:59:40 +0000',
    'support/RPM/connector_python_com.spec': 'Mon 2014-03-10 09:59:40 +0000',
    'support/__init__.py': 'Thu 2014-02-13 11:24:57 +0000',
    'support/distribution/': 'Thu 2014-02-13 11:24:57 +0000',
    'support/distribution/__init__.py': 'Fri 2012-06-08 08:08:06 +0000',
    'support/distribution/commands/': 'Thu 2014-02-13 11:24:57 +0000',
    'support/distribution/commands/__init__.py': 'Fri 2013-09-20 12:22:37 +0000',
    'support/distribution/commands/bdist.py': 'Thu 2014-02-13 11:24:57 +0000',
    'support/distribution/commands/build.py': 'Thu 2013-09-19 12:32:35 +0000',
    'support/distribution/commands/dist_deb.py': 'Fri 2013-09-20 12:22:37 +0000',
    'support/distribution/commands/dist_egg.py': 'Fri 2013-02-01 12:42:21 +0000',
    'support/distribution/commands/dist_msi.py': 'Fri 2013-09-20 12:22:37 +0000',
    'support/distribution/commands/dist_osx.py': 'Fri 2013-12-13 09:58:16 +0000',
    'support/distribution/commands/dist_rpm.py': 'Fri 2013-09-20 12:22:37 +0000',
    'support/distribution/commands/sdist.py': 'Thu 2013-11-21 13:34:58 +0000',
    'support/distribution/commercial.py': 'Thu 2013-11-21 13:34:58 +0000',
    'support/distribution/egg.py': 'Fri 2013-02-01 12:42:21 +0000',
    'support/distribution/opensource.py': 'Wed 2013-08-14 10:57:43 +0000',
    'support/distribution/utils.py': 'Fri 2013-09-20 12:22:37 +0000',
    'support/distribution/wix.py': 'Fri 2013-02-01 12:42:21 +0000',
    'support/django/': 'Thu 2014-02-13 11:24:57 +0000',
    'support/django/run_django_tests.py': 'Tue 2014-01-21 10:36:58 +0000',
    'support/django/test_mysqlconnector_settings.py': 'Thu 2014-02-13 11:24:57 +0000',
    'support/scripts/': 'Tue 2014-01-21 09:48:59 +0000',
    'support/scripts/mysql_charsets.py': 'Tue 2014-01-21 09:48:59 +0000',
    'support/scripts/mysql_errors.py': 'Tue 2014-01-21 09:48:59 +0000',
    'support/style/': 'Thu 2014-01-09 14:31:23 +0000',
    'support/style/pylint.rc': 'Thu 2014-01-09 14:31:23 +0000',
    'support/style/pylint_tests.rc': 'Thu 2014-01-09 14:31:23 +0000',
    'support/tests/': 'Thu 2014-02-13 11:24:57 +0000',
    'support/tests/__init__.py': 'Thu 2013-09-19 12:32:35 +0000',
    'support/tests/run.py': 'Tue 2013-03-26 17:24:30 +0000',
    'support/tests/test_distribution.py': 'Thu 2014-02-13 11:24:57 +0000',
    'support/tests/test_version.py': 'Thu 2013-12-19 10:02:26 +0000',
    'tests/': 'Thu 2014-04-03 11:25:53 +0000',
    'tests/__init__.py': 'Mon 2014-03-31 11:02:30 +0000',
    'tests/data/': 'Thu 2013-10-31 14:04:04 +0000',
    'tests/data/local_data.csv': 'Thu 2013-10-31 14:04:04 +0000',
    'tests/data/ssl/': 'Thu 2013-10-31 14:04:04 +0000',
    'tests/data/ssl/generate.sh': 'Tue 2013-03-26 17:24:30 +0000',
    'tests/data/ssl/tests_CA_cert.pem': 'Tue 2013-03-26 17:24:30 +0000',
    'tests/data/ssl/tests_CA_key.pem': 'Tue 2013-03-26 17:24:30 +0000',
    'tests/data/ssl/tests_client_cert.pem': 'Tue 2013-03-26 17:24:30 +0000',
    'tests/data/ssl/tests_client_key.pem': 'Tue 2013-03-26 17:24:30 +0000',
    'tests/data/ssl/tests_server_cert.pem': 'Tue 2013-03-26 17:24:30 +0000',
    'tests/data/ssl/tests_server_key.pem': 'Tue 2013-03-26 17:24:30 +0000',
    'tests/mysqld.py': 'Mon 2014-03-31 11:02:30 +0000',
    'tests/py2/': 'Thu 2014-04-03 11:25:53 +0000',
    'tests/py2/__init__.py': 'Thu 2013-10-31 14:04:04 +0000',
    'tests/py2/bugs.py': 'Thu 2014-04-03 11:25:53 +0000',
    'tests/py2/connection.py': 'Thu 2013-10-31 14:04:04 +0000',
    'tests/py2/cursor.py': 'Fri 2014-02-21 10:40:37 +0000',
    'tests/py2/test_bugs_future.py': 'Thu 2013-10-31 14:04:04 +0000',
    'tests/py2/test_conversion.py': 'Mon 2014-03-31 10:56:26 +0000',
    'tests/py2/test_network.py': 'Thu 2013-10-31 14:04:04 +0000',
    'tests/py2/test_protocol.py': 'Fri 2014-02-21 10:40:37 +0000',
    'tests/py2/test_utils.py': 'Thu 2013-10-31 14:04:04 +0000',
    'tests/py3/': 'Thu 2014-04-03 11:25:53 +0000',
    'tests/py3/__init__.py': 'Thu 2013-10-31 14:04:04 +0000',
    'tests/py3/bugs.py': 'Thu 2014-04-03 11:25:53 +0000',
    'tests/py3/connection.py': 'Thu 2013-10-31 14:04:04 +0000',
    'tests/py3/cursor.py': 'Fri 2014-02-21 10:40:37 +0000',
    'tests/py3/test_conversion.py': 'Mon 2014-03-31 10:56:26 +0000',
    'tests/py3/test_network.py': 'Mon 2014-03-31 10:56:26 +0000',
    'tests/py3/test_protocol.py': 'Fri 2014-02-21 10:40:37 +0000',
    'tests/py3/test_utils.py': 'Thu 2013-10-31 14:04:04 +0000',
    'tests/test_authentication.py': 'Fri 2014-02-21 10:40:37 +0000',
    'tests/test_bugs.py': 'Thu 2014-04-03 11:25:53 +0000',
    'tests/test_connection.py': 'Fri 2014-02-21 10:40:37 +0000',
    'tests/test_constants.py': 'Mon 2014-03-31 10:56:26 +0000',
    'tests/test_cursor.py': 'Tue 2014-01-21 10:35:56 +0000',
    'tests/test_django.py': 'Mon 2014-03-31 10:56:26 +0000',
    'tests/test_errorcode.py': 'Thu 2013-10-31 14:04:04 +0000',
    'tests/test_errors.py': 'Thu 2013-10-31 14:04:04 +0000',
    'tests/test_examples.py': 'Thu 2013-10-31 14:04:04 +0000',
    'tests/test_fabric.py': 'Thu 2014-03-06 16:26:37 +0000',
    'tests/test_locales.py': 'Thu 2013-10-31 14:04:04 +0000',
    'tests/test_mysql_datatypes.py': 'Thu 2013-10-31 14:04:04 +0000',
    'tests/test_pep249.py': 'Thu 2013-10-31 14:04:04 +0000',
    'tests/test_pooling.py': 'Thu 2014-02-20 17:55:36 +0000',
    'tests/test_setup.py': 'Mon 2014-03-31 10:33:01 +0000',
    'tests/test_style.py': 'Fri 2014-02-21 10:40:37 +0000',
    'unittests.py': 'Mon 2014-03-31 10:56:26 +0000',
    'version.py': 'Thu 2014-03-13 07:46:50 +0000',
}