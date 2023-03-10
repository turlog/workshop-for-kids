$apps = @(
@{id = "7zip.7zip" },
@{id = "Git.Git" },
@{id = "GitHub.cli" },
@{id = "Microsoft.VisualStudioCode" },
@{id = "Microsoft.WindowsTerminal" },
@{id = "Anaconda.Miniconda3" },
@{id = "MITMediaLab.Scratch.3" }
);

$extensions = @(
@{id = "ms-python.python" },
@{id = "ms-vscode.PowerShell" },
@{id = "MS-CEINTL.vscode-language-pack-pl" }
);

Foreach ($app in $apps) {
   Write-Host "Installing " $app.id
   $installed = winget list --id $app.id
   if (![String]::Join("", $installed).Contains($app.id)) {
       winget install --accept-source-agreements --accept-package-agreements --id $app.id
   }
}

runas /trustlevel:0x20000 "conda update -n base -y conda"

Foreach ($extension in $extensions) {
   & $env:LOCALAPPDATA"\Programs\Microsoft VS Code\bin\code.cmd" --force --install-extension $extension.id
}

$DesktopPath = [Environment]::GetFolderPath("Desktop")
$ws = New-Object -comObject WScript.Shell
$link = $ws.CreateShortcut("$DesktopPath\Visual Studio Code.lnk")
$link.TargetPath = "$env:LOCALAPPDATA\Programs\Microsoft VS Code\Code.exe"
$link.Arguments = "--locale pl"
$link.Save()

$repo = $ws.CreateShortcut("$DesktopPath\Repozytorium.lnk")
$repo.TargetPath = "https://github.com/turlog/workshop-for-kids"
$repo.IconLocation = "%SystemRoot%\System32\SHELL32.dll, 14"
$repo.Save()
