$ErrorActionPreference = "Stop"

Write-Host "Contact Searching Application development prerequisites"
$compiler = Get-Command g++ -ErrorAction SilentlyContinue
if (-not $compiler) {
    throw "Required tool not found: g++"
}
$python = Get-Command python -ErrorAction SilentlyContinue
if (-not $python) {
    throw "Required tool not found: python"
}

g++ --version | Select-Object -First 1
python --version
Write-Host "PASS: required local tools are available."
Write-Host "This script checks prerequisites; it does not install or modify system packages."
