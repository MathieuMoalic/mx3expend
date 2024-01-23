{
  description = "A flake for the mx3expend project";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixpkgs-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = {
    self,
    nixpkgs,
    flake-utils,
    ...
  }:
    flake-utils.lib.eachSystem ["x86_64-linux"] (system: let
      pkgs = nixpkgs.legacyPackages.${system};
      mx3expendPythonPackage = pkgs.python3Packages.buildPythonPackage {
        pname = "mx3expend";
        version = "0.0.1";
        src = self;
        format = "pyproject";
        nativeBuildInputs = [pkgs.python3Packages.setuptools];
        propagatedBuildInputs = with pkgs.python3Packages; [numpy];
      };
    in {
      packages.mx3expend = mx3expendPythonPackage;
      defaultPackage = mx3expendPythonPackage;
    });
}
