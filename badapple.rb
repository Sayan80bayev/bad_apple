class Badapple < Formula
  desc "ASCII Bad Apple player for terminal"
  homepage "https://github.com/sayan80bayev/homebrew-badapple"
  url "https://github.com/sayan80bayev/homebrew-badapple/releases/download/v1.0.1/badapple-macos-x86_64.tar.gz"
  sha256 "445bac4931d6927a1f33ab60e80f03d103fd84d3a0600bbe09da6bae295c9a9d"
  license "MIT"

  def install
    bin.install "badapple"
  end
end