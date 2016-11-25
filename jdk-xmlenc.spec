Name     : jdk-xmlenc
Version  : 0.52
Release  : 5
URL      : https://repo1.maven.org/maven2/xmlenc/xmlenc/0.52/xmlenc-0.52.jar
Source0  : https://repo1.maven.org/maven2/xmlenc/xmlenc/0.52/xmlenc-0.52.jar
Source1  : https://repo1.maven.org/maven2/xmlenc/xmlenc/0.52/xmlenc-0.52.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause
Requires: jdk-xmlenc-data
BuildRequires : javapackages-tools
BuildRequires : lxml
BuildRequires : openjdk-dev
BuildRequires : python3
BuildRequires : six

%description
No detailed description available

%package data
Summary: data components for the jdk-xmlenc package.
Group: Data

%description data
data components for the jdk-xmlenc package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/maven-poms
mkdir -p %{buildroot}/usr/share/maven-metadata
mkdir -p %{buildroot}/usr/share/java

mv %{SOURCE0} %{buildroot}/usr/share/java/xmlenc.jar
mv %{SOURCE1} %{buildroot}/usr/share/maven-poms/xmlenc.pom

# Creates metadata
python3 /usr/share/java-utils/maven_depmap.py \
-n "" \
--pom-base %{buildroot}/usr/share/maven-poms \
--jar-base %{buildroot}/usr/share/java \
%{buildroot}/usr/share/maven-metadata/xmlenc.xml \
%{buildroot}/usr/share/maven-poms/xmlenc.pom \
%{buildroot}/usr/share/java/xmlenc.jar \

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/xmlenc.jar
/usr/share/maven-metadata/xmlenc.xml
/usr/share/maven-poms/xmlenc.pom
