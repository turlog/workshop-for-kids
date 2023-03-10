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
