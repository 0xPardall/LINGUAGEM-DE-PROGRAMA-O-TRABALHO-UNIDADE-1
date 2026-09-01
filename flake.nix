{
  description = "Sistema de Gestão de Notas de Alunos em Python";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
  };

  outputs = { self, nixpkgs }:
    let
      systems = [
        "x86_64-linux"
        "aarch64-linux"
        "x86_64-darwin"
        "aarch64-darwin"
      ];

      forAllSystems = nixpkgs.lib.genAttrs systems;

      pkgsFor = forAllSystems (system:
        import nixpkgs {
          inherit system;
        }
      );
    in
    {
      devShells = forAllSystems (system:
        let
          pkgs = pkgsFor.${system};
        in
        {
          default = pkgs.mkShell {
            name = "sistema-notas";

            packages = with pkgs; [
              python3
            ];

            shellHook = ''
              echo "🐍 Ambiente Python - Sistema de Gestão de Notas"
              echo
              echo "Python: $(python --version)"
              echo
              echo "Comandos:"
              echo "  python main.py  - Executar o sistema"
              echo "  python -m compileall . - Verificar sintaxe"
              echo
            '';
          };
        }
      );

      packages = forAllSystems (system:
        let
          pkgs = pkgsFor.${system};
        in
        {
          default = pkgs.writeShellApplication {
            name = "sistema-notas";

            runtimeInputs = [
              pkgs.python3
            ];

            text = ''
              exec python ${./main.py} "$@"
            '';
          };
        }
      );
    };
}
