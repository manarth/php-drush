
# Drush is a command line shell and Unix scripting interface for Drupal. Drush
# core ships with lots of useful commands # for interacting with code like
# modules/themes/profiles. Similarly, it runs update.php, executes sql queries
# and DB migrations, and misc utilities like run cron or clear cache. Drush can
# be extended by 3rd party commandfiles.

Name:         php-drush
Summary:      Drush is a command line shell and Unix scripting interface for Drupal
Version:      6.6.0
Release:      1
License:      GPL
Group:        Development/Tools
URL:          http://www.drush.org/
Source:       https://github.com/drush-ops/drush/archive/%{version}.zip
BuildArch:    noarch
Packager:     Marcus Deglos <marcus@techito.co.uk>
BuildArch:    noarch
Requires:     php-cli >= 5.3.0

# Provide a custom filepath, because the source URL doesn't match the source filename.
%define buildfilepath	drush-%version

%description
Drush is a command line shell and Unix scripting interface for Drupal. Drush
core ships with lots of useful commands for interacting with code like
modules/themes/profiles. Similarly, it runs update.php, executes sql queries
and DB migrations, and misc utilities like run cron or clear cache. Drush can
be extended by 3rd party commandfiles.


# PREP stage populates the BUILD directory.
%prep
# Can't use the %setup macro, as the Source URL doesn't match the zip filename.
cd %{_builddir}
rm -rf %buildfilepath
/usr/bin/unzip %{_sourcedir}/%buildfilepath

%build
# No action required, nothing to make.
echo 'build'

# INSTALL stage populates the BUILDROOT directory.
%install
echo 'install'
echo "Buildroot is " %buildroot
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_libdir}/%buildfilepath
mkdir -p %{buildroot}%{_bindir}
cp -r %{_builddir}/%buildfilepath/.  %{buildroot}%{_libdir}/%buildfilepath
ln -s ./%buildfilepath %{buildroot}%{_libdir}/drush
ln -s %{_libdir}/drush/drush %{buildroot}%{_bindir}

%check
echo 'check'

%clean
rm -rf %{buildroot}



%files
%defattr(-,root,root)
%dir %{_libdir}/drush
%dir %{_libdir}/%buildfilepath
%{_libdir}/%buildfilepath/*
%{_libdir}/%buildfilepath/.gitignore
%{_libdir}/%buildfilepath/.travis.yml
%attr(0755, root, root) %{_bindir}/drush

