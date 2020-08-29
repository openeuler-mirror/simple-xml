Name:                simple-xml
Summary:             An XML serialization framework for Java
Version:             2.7.1
Release:             1
License:             ASL 2.0
Url:                 http://simple.sourceforge.net/
Source0:             http://downloads.sourceforge.net/simple/simple-xml-%{version}.tar.gz
Source1:             https://repo1.maven.org/maven2/org/simpleframework/simple-xml/%{version}/simple-xml-%{version}.pom

BuildRequires:       java-devel javapackages-local javapackages-tools ant ant-junit bea-stax
BuildRequires:       bea-stax-api junit xpp3
Requires:            bea-stax xpp3
Requires:            javapackages-tools
BuildArch:           noarch

%description
Simple is a high performance XML serialization and
configuration framework for Java. Its goal is to
provide an XML framework that enables rapid development
of XML configuration and communication systems.

%package javadoc
Summary:             Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q
rm -r javadoc/* test/report/*
find . -name "*.jar" -delete
find . -name "*.class" -delete
sed -i 's/\r//' LICENSE.txt
sed -i 's|haltonfailure="yes"|haltonfailure="no"|' test/build.xml

%build
%ant -Dlib.path=%{_javadir} all

%install
mkdir -p %{buildroot}%{_javadir}
install -m 644 jar/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar
mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 %{SOURCE1} %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap
mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr javadoc/* %{buildroot}%{_javadocdir}/%{name}

%files -f .mfiles
%license LICENSE.txt

%files javadoc
%{_javadocdir}/%{name}
%license LICENSE.txt

%changelog
* Mon Aug 3 2020 leiju <leiju4@huawei.com> - 2.7.1-1
- Package init
