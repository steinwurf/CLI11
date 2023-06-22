#! /usr/bin/env python
# encoding: utf-8

APPNAME = "CLI11"
VERSION = "1.0.0"


def configure(conf):
    conf.set_cxx_std(11)


def build(bld):
    use_flags = []
    if bld.is_mkspec_platform("linux"):
        use_flags += ["PTHREAD"]

    # Path to the cli11 repo
    cli11_path = bld.dependency_node("cli11-source")

    # Create system include for cli11
    bld(name="cli11", export_includes=cli11_path.find_dir("include").abspath())

    if bld.is_toplevel():
        bld.program(
            features="cxx",
            source=cli11_path.ant_glob("examples/simple.cpp"),
            target="simple",
            use=["cli11"],
        )
