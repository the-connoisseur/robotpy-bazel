load("@bazel_tools//tools/build_defs/cc:action_names.bzl", "ACTION_NAMES")
load(
    "@bazel_tools//tools/cpp:cc_toolchain_config_lib.bzl",
    "feature",
    "flag_group",
    "flag_set",
    "tool_path",
)

all_cpp_compile_actions = [
    ACTION_NAMES.cpp_compile,
    ACTION_NAMES.linkstamp_compile,
    ACTION_NAMES.cpp_header_parsing,
    ACTION_NAMES.cpp_module_compile,
    ACTION_NAMES.cpp_module_codegen,
    ACTION_NAMES.clif_match,
]

all_link_actions = [
    ACTION_NAMES.cpp_link_executable,
    ACTION_NAMES.cpp_link_dynamic_library,
    ACTION_NAMES.cpp_link_nodeps_dynamic_library,
]

def _impl(ctx):
    default_linker_flags = feature(
        name = "default_linker_flags",
        enabled = True,
        flag_sets = [
            flag_set(
                actions = all_link_actions,
                flag_groups = [
                    flag_group(
                        flags = [
                            "-lstdc++",
                        ],
                    ),
                ],
            ),
        ],
    )

    default_compiler_flags = feature(
        name = "default_compiler_flags",
        enabled = True,
        flag_sets = [
            flag_set(
                actions = all_cpp_compile_actions + [
                    ACTION_NAMES.assemble,
                    ACTION_NAMES.preprocess_assemble,
                    ACTION_NAMES.c_compile,
                    ACTION_NAMES.lto_backend,
                ],
                flag_groups = [
                    flag_group(
                        flags = [
                            "--sysroot=external/_main~_repo_rules~aarch64_glibc_stable_2022-08-1",
                            "-I$SYSROOT/aarch64-buildroot-linux-gnu/include/c++/11.3.0",
                            "-I$SYSROOT/aarch64-buildroot-linux-gnu/include/c++/11.3.0/aarch64-buildroot-linux-gnu",
                            "-isystem",
                            "$SYSROOT/aarch64-buildroot-linux-gnu/sysroot/usr/include",
                            "-isystem",
                            "$SYSROOT/lib/gcc/aarch64-buildroot-linux-gnu/11.3.0/include",
                        ],
                    )
                ],
            )
        ],
    )

    features = [
        default_linker_flags,
        default_compiler_flags,
    ]

    tool_paths = [
        tool_path(
            name = "gcc",
            path = "jetson_linux/aarch64_glibc_stable_2022-08-1_gcc",
        ),
        tool_path(
            name = "ld",
            path = "jetson_linux/aarch64_glibc_stable_2022-08-1_ld",
        ),
        tool_path(
            name = "ar",
            path = "jetson_linux/aarch64_glibc_stable_2022-08-1_ar",
        ),
        tool_path(
            name = "as",
            path = "jetson_linux/aarch64_glibc_stable_2022-08-1_as",
        ),
        tool_path(
            name = "cpp",
            path = "jetson_linux/aarch64_glibc_stable_2022-08-1_cpp",
        ),
        tool_path(
            name = "nm",
            path = "jetson_linux/aarch64_glibc_stable_2022-08-1_nm",
        ),
        tool_path(
            name = "objcopy",
            path = "jetson_linux/aarch64_glibc_stable_2022-08-1_objcopy",
        ),
        tool_path(
            name = "objdump",
            path = "jetson_linux/aarch64_glibc_stable_2022-08-1_objdump",
        ),
        tool_path(
            name = "strip",
            path = "jetson_linux/aarch64_glibc_stable_2022-08-1_strip",
        ),
    ]

    return cc_common.create_cc_toolchain_config_info(
        ctx = ctx,
        features = features,
        toolchain_identifier = "jetson-linux-toolchain",
        host_system_name = "local",
        target_system_name = "orin",
        target_cpu = "orin",
        target_libc = "orin",
        compiler = "gcc",
        abi_version = "orin",
        abi_libc_version = "orin",
        tool_paths = tool_paths,
    )

cc_toolchain_config = rule(
    implementation = _impl,
    attrs = {},
    provides = [CcToolchainConfigInfo],
)
