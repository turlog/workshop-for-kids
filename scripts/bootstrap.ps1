# Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted

Install-PackageProvider -Name NuGet -Force
Install-Module PSReadLine -Force

Install-Language -Language pl-PL -CopyToSettings
Set-SystemPreferredUILanguage pl-PL
Set-SystemLanguage pl-PL

Set-Culture pl-PL
Set-WinSystemLocale -SystemLocale pl-PL
Set-WinUILanguageOverride -Language pl-PL
Set-WinUserLanguageList pl-PL -Force
Set-WinHomeLocation -GeoId 191

Invoke-WebRequest -Uri https://aka.ms/Microsoft.VCLibs.x64.14.00.Desktop.appx -OutFile Microsoft.VCLibs.x64.14.00.Desktop.appx
Add-AppxPackage Microsoft.VCLibs.x64.14.00.Desktop.appx

Invoke-WebRequest -Uri https://www.nuget.org/api/v2/package/Microsoft.UI.Xaml/2.7.3 -OutFile .\microsoft.ui.xaml.2.7.3.zip
Expand-Archive .\microsoft.ui.xaml.2.7.3.zip -Force
Add-AppxPackage .\microsoft.ui.xaml.2.7.3\tools\AppX\x64\Release\Microsoft.UI.Xaml.2.7.appx

Invoke-WebRequest -Uri https://github.com/microsoft/winget-cli/releases/download/v1.3.2691/Microsoft.DesktopAppInstaller_8wekyb3d8bbwe.msixbundle -OutFile .\Microsoft.DesktopAppInstaller_8wekyb3d8bbwe.msixbundle
Add-AppxPackage Microsoft.DesktopAppInstaller_8wekyb3d8bbwe.msixbundle

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
