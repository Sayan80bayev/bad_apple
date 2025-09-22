class Badapple < Formula
  desc "ASCII Bad Apple player for terminal"
  homepage "https://github.com/sayan80bayev/homebrew-badapple"
  url "https://github.com/sayan80bayev/homebrew-badapple/releases/download/v1.0.1/badapple-macos-x86_64.tar.gz"
  sha256 "4ce17e79de06918ceaff4ccee210ebb823f0cd9b78cd778c96eb3bd242291104"
  license "MIT"

  def install
    bin.install "badapple"
  end
end