{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  nativeBuildInputs = with pkgs; [
    ninja
    meson
    pkg-config
  ];
  buildInputs = with pkgs; [
    python3
    python3Packages.pip
    python3Packages.virtualenv

    # System-level deps manim-voiceover needs
    steam-run
    ffmpeg
    portaudio   # needed by some TTS backends for audio playback
    cairo
    pango
  ];

  shellHook = ''
    # Create a venv that can still see nix-installed packages (like manim)
    if [ ! -d ".venv" ]; then
      echo "Creating virtualenv..."
      python -m venv .venv --system-site-packages
    fi
    echo "boom"

    source .venv/bin/activate

    # Install manim-voiceover with your chosen TTS backend
    pip install manim "manim-voiceover[coqui]"
  '';
}