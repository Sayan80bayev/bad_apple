class Badapple < Formula
  desc "ASCII Bad Apple player for terminal"
  homepage "https://github.com/sayan80bayev/homebrew-badapple"
  url "https://github.com/sayan80bayev/homebrew-badapple/releases/download/v1.0.1/badapple-macos-x86_64.tar.gz"
  sha256 "3008af0db0201c01d57ecc8259da629ea4bb4f56334dd4dc4aecac80a3c1db24"
  license "MIT"

  def install
    bin.install "badapple"
  end
end