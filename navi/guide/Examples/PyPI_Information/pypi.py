#!/usr/bin/env python

"""
pypi.py

Copyright (C) 2006 David Boddie

This file is part of PyPI Browser, a GUI browser for the Python Package Index.

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
"""

import os, urlparse, xmlrpclib


class Package:

    """Package
    
    Describes a package in the package index.
    
    Initially, the package has a name but, unless specified when created,
    no release information. Release information is added as required,
    typically by models that incrementally populate their internal structure.
    """
    
    def __init__(self, name, releases = None):
    
        self.name = name
        self.releases = releases
        self.new = True


class Release:

    """Release
    
    Describes a single release of a package.
    
    Initially, the release contains a reference to the relevant package
    and a version string. The description, unless specified on creation,
    is added as required.
    """
    
    def __init__(self, package, version, description = None):
    
        self.package = package
        self.version = version
        self.description = description


class Description:

    """Description
    
    Provides a description of a single release of a package.
    
    By default, descriptions are created with a reference to the release
    they describe and an empty set of metadata. The metadata dictionary can
    be accessed via the instance's metadata attribute.
    """
    
    template_metadata = {
            "name": None, "version": None, "stable_version": None,
            "author": None, "author_email": None, "maintainer": None,
            "maintainer_email": None, "home_page": None, "license": None,
            "summary": None, "description": None,
            "keywords": None, "platform": None, "download_url": None,
            "classifiers": None, "release_urls": None
        }

    def __init__(self, release, metadata = {}):
    
        self.release = release
        self.metadata = self.template_metadata.copy()
        
        for key in metadata.keys():
            if self.metadata.has_key(key):
                self.metadata[key] = metadata[key]
    
    def metaData(self, field):
    
        """data(self, field)
        
        Returns data corresponding to a given field in the description's
        metadata.
        """
        
        try:
            value = self.metadata[field]
        except KeyError:
            return None
        
        if field == "classifiers":
            return u", ".join(value)
        else:
            return value
    
    def setMetaData(self, field, data):
    
        if data is None:
            return
        
        elif field == u"home_page":
        
            if not urlparse.urlsplit(data)[0]:
                data = None
        
        elif field == u"download_url":
        
            pieces = urlparse.urlsplit(data)
            path = pieces[2]
            if not path or path.endswith(u".html") or path.endswith(u"/"):
                data = None
            elif u"." not in path.split(u"/")[-1]:
                data = None
            else:
                data = [u"url", data, u"packagetype", u"default"]
                urls = self.metadata[u"release_urls"]
                if not urls:
                    self.metadata[u"release_urls"] = data
                else:
                    urls.append(data)
        
        elif field == u"release_urls":
        
            # Convert the dictionary into a list for serialisation.
            lists = []
            for url_dict in data:
                lists += [(u"url", url_dict[u"url"]), (u"packagetype", url_dict[u"packagetype"])]
            
            data = reduce(lambda x, y: x + list(y), lists, [])
        
        self.metadata[field] = data


class AbstractServer:

    """AbstractServer
    
    A base class for classes representing XML-RPC interfaces to package
    indexes.
    """
    
    def __init__(self, url = None):
    
        self.url = url
    
    def name(self):
    
        if self.url:
            return urlparse.urlsplit(self.url)[1]
        else:
            return None
    
    def list_packages(self):
    
        return []

    
class PackageServer(AbstractServer):

    """PackageServer(AbstractServer)
    
    Provides an XML-RPC interface to a package index with a thin API over
    the methods exported by the remote XML-RPC server.
    """
    
    def __init__(self, url):
    
        AbstractServer.__init__(self, url)
        self.server = xmlrpclib.Server(url)
    
    def list_packages(self):
    
        """list_packages(self)
        
        Returns a sorted list of package name strings or an empty list if
        the server could not be accessed successfully.
        """
        
        try:
            names = self.server.list_packages()
            names.sort()
            return map(Package, names)
        except xmlrpclib.Error:
            return []
    
    def package_releases(self, package):
    
        """package_releases(self, package)
        
        Returns a list of version strings describing the available releases
        of the package specified by a Package object.
        
        An empty list is returned if the call was unsuccessful.
        """
        
        try:
            return map(lambda x: Release(package, x), self.server.package_releases(package.name))
        except xmlrpclib.Error:
            print "missing release:", package.name
            return []
    
    def package_stable_release(self, package):
    
        """package_stable_release(self, package)
        
        Returns a version string describing the stable release
        of the package specified by a Package object.
        
        No exception handling is performed.
        """
        
        return Release(package, self.server.package_stable_release(package.name))
    
    def release_urls(self, release):
    
        """release_urls(self, release)
        
        Returns a list of dictionaries containing download information for
        a given release specified by a Release object.
        
        If the information could not be retrieved from the server, None is
        returned.
        """
        
        try:
            return self.server.release_urls(release.package.name, release.version)
        except xmlrpclib.Error:
            return None
    
    def release_data(self, release):
    
        """release_data(self, release)
        
        Returns a Description object containing information about a given
        release specified by a Release object.
        
        If the information could not be retrieved from the server, None is
        returned.
        """
        
        try:
            description = Description(release)
            metadata = self.server.release_data(release.package.name, release.version)
            for field, data in metadata.items():
                description.setMetaData(field, data)
            return description
        except xmlrpclib.Error:
            print "missing data:", release.package.name, release.version
            return None
    
    def release_full_data(self, release):
    
        """release_full_data(self, release)
        
        Returns a Description object containing information about a given
        release specified by a Release object.
        
        If the information could not be retrieved from the server, None is
        returned.
        """
        
        try:
            description = Description(release)
            metadata = self.server.release_data(release.package.name, release.version)
            for field, data in metadata.items():
                description.setMetaData(field, data)
            
            # Add additional information about download URLs for this release
            # to the description.
            urls = self.release_urls(release)
            if urls:
                description.setMetaData("release_urls", urls)
            return description
        except xmlrpclib.Error:
            print "missing data:", release.package.name, release.version
            return None
    
    def search(self, specification, operator = "and"):
    
        """search(self, specification, operator = "and")
        
        Searches the package index using the specified operator to combine
        words in the given specification, returning a list of dictionaries
        each containing the name, version and summary of each matching
        package.
        """
        
        # Possibly add a name: Package dictionary so that we can relate the
        # descriptions returned to existing packages.
        return self.server.search(specification, operator)


class TestServer(AbstractServer):

    """TestServer(AbstractServer)
    
    A test server for simple GUI testing purposes.
    """
    
    def __init__(self):
    
        AbstractServer.__init__(self)
        
        package = Package("Test package")
        release1 = Release(package, "0.1")
        description1 = Description(release1, {
            "name": "Test package", "author": "David Boddie", "version": "0.1",
            "download_url": "file://%s" % os.path.abspath(__file__),
            "home_page": "file://"})
        release1.description = description1
        package.releases = [release1]
        
        self.packages = [package]
    
    def list_packages(self):
    
        return self.packages
    
    def package_releases(self, package):
    
        try:
            return map(lambda x: Release(package, x), self.server.package_releases(package.name))
        except xmlrpclib.Error:
            print "missing release:", package.name
            return []
    
    def package_stable_release(self, package):
    
        return Release(package, self.server.package_stable_release(package.name))
    
    def release_urls(self, release):
    
        return self.server.release_urls(release.package.name, release.version)
    
    def release_data(self, release):
    
        try:
            description = Description(release)
            metadata = self.server.release_data(release.package.name, release.version)
            for field, data in metadata.items():
                description.setMetaData(field, data)
            return description
        except xmlrpclib.Error:
            print "missing data:", release.package.name, release.version
            return None
    
    def search(self, spec, operator = "and"):
    
        return self.server.search(spec, operator)
