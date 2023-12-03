# Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted

Install-PackageProvider -Name NuGet -Force
Install-Module PSReadLine -Force

$apps = @(
@{id = "7zip.7zip" },
@{id = "Git.Git" },
@{id = "GitHub.cli" },
@{id = "Microsoft.VisualStudioCode" },
@{id = "Microsoft.WindowsTerminal" },
@{id = "Anaconda.Miniconda3" }
);

$extensions = @(
@{id = "ms-python.python" },
@{id = "ms-vscode.PowerShell" },
@{id = "MS-CEINTL.vscode-language-pack-pl" }
);

Foreach ($app in $apps) {
   Write-Host "Installing " $app.id
#   $installed = winget list --accept-source-agreements --accept-package-agreements  --id $app.id
#   if (![String]::Join("", $installed).Contains($app.id)) {
       winget install --accept-source-agreements --accept-package-agreements --id $app.id
#   }
}

#runas /trustlevel:0x20000 "conda update -n base -y conda"

Foreach ($extension in $extensions) {
   & $env:LOCALAPPDATA"\Programs\Microsoft VS Code\bin\code.cmd" --force --install-extension $extension.id
}

