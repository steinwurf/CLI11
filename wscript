#! /usr/bin/env python
# encoding: utf-8

import os

APPNAME = 'CLI11'
VERSION = '1.0.0'


def build(bld):
    bld.env.append_unique(
        'DEFINES_STEINWURF_VERSION',
        'STEINWURF_CLI11_VERSION="{}"'.format(VERSION))

    use_flags = []
    if bld.is_mkspec_platform('linux'):
        use_flags += ['PTHREAD']

    # Path to the cli11 repo
    cli11_path = bld.dependency_node("cli11-source")

    # Create system include for cli11
    bld(name='cli11',
        export_includes=cli11_path.find_dir('include').abspath())

    if bld.is_toplevel():

        bld.program(
            features='cxx',
            source=cli11_path.ant_glob('examples/simple.cpp'),
            target='simple',
            use=['cli11'])
