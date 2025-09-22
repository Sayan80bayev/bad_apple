class Badapple < Formula
  desc "ASCII Bad Apple player for terminal"
  homepage "https://github.com/sayan80bayev/badapple"
  url "https://github.com/user-attachments/files/22466688/badapple-macos-x86_64.tar.gz"
  sha256 "3008af0db0201c01d57ecc8259da629ea4bb4f56334dd4dc4aecac80a3c1db24"
  license "MIT"

  def install
    bin.install "badapple"
  end
end