# -artifact-events-infrastructure-infrastructure

Infrastructure layer for pythoneda-shared-artifact-changes/artifact-events-infrastructure

## How to declare it in your flake

Check the latest tag of the artifact repository: https://github.com/pythoneda-shared-artifact/artifact-events-infrastructure-artifact/tags, and use it instead of the `[version]` placeholder below.

```nix
{
  description = "[..]";
  inputs = rec {
    [..]
    pythoneda-shared-artifact--artifact-events-infrastructure = {
      [optional follows]
      url =
        "github:pythoneda-shared-artifact/artifact-events-infrastructure-artifact/[version]?dir=artifact-events-infrastructure";
    };
  };
  outputs = [..]
};
```

Should you use another PythonEDA modules, you might want to pin those also used by this project. The same applies to [https://nixos/nixpkgs](nixpkgs "nixpkgs") and [https://github.com/numtide/flake-utils](flake-utils "flake-utils").

The Nix flake is under the [https://github.com/pythoneda-shared-artifact/artifact-events-infrastructure-artifact/tree/main/artifact-events-infrastructure](artifact-events-infrastructure "artifact-events-infrastructure") folder of <https://github.com/pythoneda-shared-artifact/artifact-events-infrastructure-artifact>.

