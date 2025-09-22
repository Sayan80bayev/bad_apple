class Badapple < Formula
  desc "ASCII Bad Apple player for terminal"
  homepage "https://github.com/sayan80bayev/homebrew-badapple"
  url "https://github.com/sayan80bayev/homebrew-badapple/releases/download/v1.0.1/badapple-macos-x86_64.tar.gz"
  sha256 "8a2abc8d4a9d857acfd4e7bf491be3296620392a8773e874ce9eb80a2929a7a5"
  license "MIT"

  def install
      libexec.install Dir["*"]
      bin.write_exec_script (libexec/"badapple")
  end
end