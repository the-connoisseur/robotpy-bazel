import os
import subprocess
import sys


def main():
    workspace_root = os.environ.get("BUILD_WORKSPACE_DIRECTORY")
    if not workspace_root:
        print(
            "Error: BUILD_WORKSPACE_DIRECTORY is not set. Please run this with `bazel run`."
        )
        sys.exit(1)

    subprocess.check_call(
        [sys.executable, "-m", "black", workspace_root, "--exclude", "^bazel-[^/]+$"]
    )


if __name__ == "__main__":
    main()
