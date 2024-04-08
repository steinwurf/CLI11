#! /usr/bin/env python
# encoding: utf-8

APPNAME = "CLI11"
VERSION = "2.0.0"


def configure(conf):
    conf.set_cxx_std(11)


def build(bld):
    use_flags = []
    if bld.is_mkspec_platform("linux"):
        use_flags += ["PTHREAD"]

    # Path to the cli11 repo
    cli11_path = bld.dependency_node("cli11-source")
    defines = []
    if (
        "clang" not in bld.env.CXX_NAME
        and "g++" in bld.env.CXX_NAME
        and int(bld.env.CC_VERSION[0]) < 9
    ):
        defines += ["CLI11_USE_FILESYSTEM=0"]
    # Create system include for cli11
    bld(
        name="cli11",
        export_includes=cli11_path.find_dir("include").abspath(),
        export_defines=defines,
    )

    if bld.is_toplevel():
        # Build the example
        bld.program(
            features="cxx",
            source=cli11_path.ant_glob("examples/simple.cpp"),
            target="simple",
            use=["cli11"],
        )
